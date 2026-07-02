import json
import os
import datetime
from dateutil.relativedelta import relativedelta
import time
import pandas as pd
import awswrangler as wr
# import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import boto3
import io
from urllib.parse import urlparse
# Step 2: Import libraries

# S3 paths (via Lambda env vars)

INPUT_PATH = "s3://maintenance-operations-bucket/INPUT-MaintenanceOperationsData/maintenance_Operations_Input_Data.xlsx"          # e.g. s3://my-bucket/Maintenance_Operations_Input_Modified.xlsx
OUTPUT_PREFIX = "s3://maintenance-operations-bucket/OUTPUT-MaintenanceOperationsResults/"    # e.g. s3://my-bucket/outputs/



def generate_schedule(df,budget_df, interval_label, interval_months):
    today = pd.to_datetime(datetime.date.today())
    due_date = df['Effective_Last_Maintenance'] + pd.to_timedelta(interval_months * 30, unit='D')

    filtered = df[
        (df['Recommended_Interval'].str.lower() == interval_label.lower()) &
        (due_date <= today + pd.DateOffset(months=interval_months))
    ]

    # Apply budget constraint
    merged = pd.merge(filtered, budget_df, on='Department', how='left')
    merged['Estimated_Cost'] = 1000  # Example cost per equipment
    merged = merged[merged['Remaining_Budget'] >= merged['Estimated_Cost']]

    # Prioritize by criticality and risk
    result = merged.sort_values(by=['Criticality_Level', 'Risk_Impact'], ascending=[False, False])
    return result


def lambda_handler(event, context):
    # Step 1: Parse S3 bucket and object key
    parsed_url = urlparse(INPUT_PATH)
    bucket_name = parsed_url.netloc
    key = parsed_url.path.lstrip('/')

    # Step 2: Download the file from S3
    # s3 = boto3.client('s3')
    output_folder = 'OUTPUT-MaintenanceOperationsResults/'
    s3_output_bucket = bucket_name  # same bucket as input
    s3_client = boto3.client('s3')

    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        file_content = response['Body'].read()
        excel_io = io.BytesIO(file_content)

        # Step 3: Read Excel sheets into DataFrames
        equipment_df = pd.read_excel(excel_io, sheet_name='Equipment_List', engine='openpyxl')
        excel_io.seek(0)  # Reset stream position for each read
        maintenance_logs_df = pd.read_excel(excel_io, sheet_name='Maintenance_Logs', engine='openpyxl')
        excel_io.seek(0)
        maintenance_priorities_df = pd.read_excel(excel_io, sheet_name='Maintenance_Priorities', engine='openpyxl')
        excel_io.seek(0)
        budget_df = pd.read_excel(excel_io, sheet_name='Budget_Allocation', engine='openpyxl')

        # Step 4: Display previews
        print(f"\nFile '{key}' uploaded and loaded successfully.\n")
        print("Equipment List Preview:")
        print(equipment_df.head())

        print("\nMaintenance Logs Preview:")
        print(maintenance_logs_df.head())

        print("\nMaintenance Priorities Preview:")
        print(maintenance_priorities_df.head())

        print("\nBudget Allocation Preview:")
        print(budget_df.head())
        # Step 4: Merge Equipment with Priorities and Logs
        equipment_priority_df = pd.merge(equipment_df, maintenance_priorities_df, on='Equipment_ID', how='left')

        # Add latest log date for fallback if Last_Maintenance_Date is missing
        latest_log = maintenance_logs_df.groupby('Equipment_ID')['Date'].max().reset_index()
        latest_log.columns = ['Equipment_ID', 'Last_Log_Date']

        equipment_priority_df = pd.merge(equipment_priority_df, latest_log, on='Equipment_ID', how='left')

        # Calculate the effective last maintenance date
        equipment_priority_df['Effective_Last_Maintenance'] = equipment_priority_df['Last_Maintenance_Date'].fillna(
            equipment_priority_df['Last_Log_Date']
        )

        # Generate  scheduled Plans
        plans = {}
        plans['3_month'] = generate_schedule(equipment_priority_df,budget_df, '3 months', 3)
        plans['quarterly'] = generate_schedule(equipment_priority_df,budget_df, 'Quarterly', 3)
        plans['6_month'] = generate_schedule(equipment_priority_df,budget_df, '6 Months', 6)
        plans['annual'] = generate_schedule(equipment_priority_df,budget_df, 'Annual', 12)
        plans['biannual'] = generate_schedule(equipment_priority_df,budget_df, 'Biannual', 24)

        # Save and upload each plan
        for plan_name, df in plans.items():
            if df.empty:
                continue  # skip empty plans
            output_key = f'{output_folder}{plan_name}_maintenance_plan.xlsx'
            with io.BytesIO() as buffer:
                df.to_excel(buffer, index=False)
                buffer.seek(0)
                s3_client.put_object(Bucket=s3_output_bucket, Key=output_key, Body=buffer.getvalue())
                print(f"Uploaded: {output_key}")

        # Generate and upload global plan
        global_plan = pd.concat(plans.values(), ignore_index=True).drop_duplicates()
        if not global_plan.empty:
            global_key = f'{output_folder}global_maintenance_plan.xlsx'
            with io.BytesIO() as buffer:
                global_plan.to_excel(buffer, index=False)
                buffer.seek(0)
                s3_client.put_object(Bucket=s3_output_bucket, Key=global_key, Body=buffer.getvalue())
                print(f"Uploaded: {global_key}")
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
    print("Mainteance Results susscessfully stored in S3 Bucket ")
    return {
                'statusCode': 200,
                'body': 'Excel file processed successfully.'
    }
