# Step 1: Install necessary libraries
!pip install pandas openpyxl


import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import os
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files


# Step 2: Load all required sheets into separate DataFrames
#       : Prompt the user to upload the file from local disk
print("Please upload the 'Maintenance_Operations_Input_Modified.xlsx' file.")
uploaded = files.upload()

# Step 3: Extract the filename from the uploaded file
#       : Read the sheets into separate DataFrames
file_name = list(uploaded.keys())[0]

try:

    equipment_df = pd.read_excel(file_name, sheet_name='Equipment_List')
    maintenance_logs_df = pd.read_excel(file_name, sheet_name='Maintenance_Logs')
    maintenance_priorities_df = pd.read_excel(file_name, sheet_name='Maintenance_Priorities')
    budget_df = pd.read_excel(file_name, sheet_name='Budget_Allocation')

    print(f"\n File '{file_name}' uploaded and loaded successfully.\n")
    print(" Equipment List Preview:")
    print(equipment_df.head())

    print("\n Maintenance Logs Preview:")
    print(maintenance_logs_df.head())

    print("\n Maintenance Priorities Preview:")
    print(maintenance_priorities_df.head())

    print("\n Budget Allocation Preview:")
    print(budget_df.head())

except Exception as e:
    print(f" Error reading Excel file: {e}")




# Step 4: Merge Equipment with Priorities and Logs
# First, merge priorities with equipment list
equipment_priority_df = pd.merge(equipment_df, maintenance_priorities_df, on='Equipment_ID', how='left')

# Add latest log date for fallback if Last_Maintenance_Date is missing
latest_log = maintenance_logs_df.groupby('Equipment_ID')['Date'].max().reset_index()
latest_log.columns = ['Equipment_ID', 'Last_Log_Date']

equipment_priority_df = pd.merge(equipment_priority_df, latest_log, on='Equipment_ID', how='left')

# Use Last_Maintenance_Date or fallback to last log date
equipment_priority_df['Effective_Last_Maintenance'] = equipment_priority_df['Last_Maintenance_Date'].fillna(
    equipment_priority_df['Last_Log_Date']
)

# Step 5: Define Schedule Function
def generate_schedule(df, interval_label, interval_months):
    today = pd.to_datetime(datetime.date.today())
    next_maintenance_due = df['Effective_Last_Maintenance'] + pd.to_timedelta(interval_months * 30, unit='D')
    filtered = df[(df['Recommended_Interval'].str.lower() == interval_label.lower()) &
                  (next_maintenance_due <= today + pd.DateOffset(months=interval_months))]

    # Apply budget constraint
    merged = pd.merge(filtered, budget_df, on='Department', how='left')
    merged['Estimated_Cost'] = 1000  # Assume default cost per equipment
    merged = merged[merged['Remaining_Budget'] >= merged['Estimated_Cost']]

    # Optional: Apply criticality or risk filter
    result = merged.sort_values(by=['Criticality_Level', 'Risk_Impact'], ascending=[False, False])
    return result

# Step 6: Generate Individual Plans
plans = {}

plans['3_month'] = generate_schedule(equipment_priority_df, '3 months', 3)
plans['quarterly'] = generate_schedule(equipment_priority_df, 'Quarterly', 3)
plans['6_month'] = generate_schedule(equipment_priority_df, '6 Months', 6)
plans['annual'] = generate_schedule(equipment_priority_df, 'Annual', 12)
plans['biannual'] = generate_schedule(equipment_priority_df, 'Biannual', 24)

# Step 7: Save each plan to Excel
for plan_name, df in plans.items():
    filename = f'{plan_name}_maintenance_plan.xlsx'
    df.to_excel(filename, index=False)
    print(f"Saved: {filename}")

# Step 8: Generate Global Maintenance Plan
global_plan = pd.concat(plans.values(), ignore_index=True).drop_duplicates()
global_plan.to_excel('global_maintenance_plan.xlsx', index=False)
print("Saved: global_maintenance_plan.xlsx")


# Step 3: Compute Dashboard Metrics
metrics = {}

# Equipment Metrics
metrics['Total Equipment'] = equipment_df['Equipment_ID'].nunique()
metrics['Active Equipment'] = (equipment_df['Status'] == 'Active').sum()
metrics['Inactive Equipment'] = (equipment_df['Status'] == 'Inactive').sum()

# Criticality Distribution
criticality_dist = equipment_df['Criticality_Level'].value_counts()

# Maintenance Types
maintenance_types = maintenance_logs_df['Maintenance_Type'].value_counts()

# Downtime
metrics['Average Downtime (hrs)'] = round(maintenance_logs_df['Downtime (hrs)'].mean(), 2)
metrics['Total Downtime (hrs)'] = round(maintenance_logs_df['Downtime (hrs)'].sum(), 2)

# Budget Utilization
budget_df['Utilization (%)'] = (budget_df['Budget_Used'] / budget_df['Annual_Budget']) * 100

# Step 4: Create Dashboard Charts
plt.figure(figsize=(15, 10))

# Equipment Status
plt.subplot(2, 2, 1)
equipment_df['Status'].value_counts().plot(kind='bar', color=['green', 'red'])
plt.title('Equipment Status')
plt.ylabel('Count')

# Criticality Level
plt.subplot(2, 2, 2)
sns.barplot(x=criticality_dist.index, y=criticality_dist.values, palette='coolwarm')
plt.title('Criticality Distribution')
plt.ylabel('Count')

# Maintenance Type
plt.subplot(2, 2, 3)
sns.barplot(x=maintenance_types.index, y=maintenance_types.values, palette='viridis')
plt.title('Maintenance Type Distribution')
plt.ylabel('Count')

# Budget Utilization
plt.subplot(2, 2, 4)
sns.barplot(data=budget_df, x='Department', y='Utilization (%)', palette='Set2')
plt.title('Budget Utilization by Department')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("maintenance_dashboard.png")
plt.show()

# Step 5: Export Metrics to Excel
metrics_df = pd.DataFrame(list(metrics.items()), columns=['Metric', 'Value'])
metrics_df.to_excel("maintenance_metrics.xlsx", index=False)

# Step 6: Download Files
files.download("maintenance_metrics.xlsx")
files.download("maintenance_dashboard.png")
