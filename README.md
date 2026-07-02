# Cloud-Based-PowerBI-MaintenanceOperationsPlanning
Digital transformation of Maintenance Operations Planning Through AWS Cloud, Power BI KPI Analytics Dashboard, and Power Automate Workflow
Here's a professional GitHub README that highlights your project in a way that's attractive to recruiters, instructors, and collaborators.

# Digital Transformation of Maintenance Operations Planning

## Cloud-Based Maintenance Planning with AWS, Power BI & Power Automate

A serverless cloud solution that automates industrial maintenance planning by combining **AWS Cloud Services**, **Python**, **Power BI**, and **Power Automate** to transform manual maintenance file management into an intelligent, scalable, and data-driven platform.

> **Author:** David Roland Gnimpieba Zanfack

---

Problem Statement and Objectives 


    1. Manual Files Management challenges for Maintenance Operations Planning


Many organizations continue to use manual file management for their planning, maintenance, budget and schedule optimization operations. These files are generally in Excel, Word, PDF, or TXT format and contain data records such as payroll, inventory, date criticality, etc. This fragmented and siloed approach leads to very time-consuming manual work, data inconsistency, operational inefficiency, and a lack of collaboration and integration of work tools.
 
       
    2. Automated Pipeline for File Ingestion and Data Transformation API

The problem here is the design and development of Pipeline and API Endpoints that automate data ingestion, storage, document transformation and maintenance operations planning reports in a structured or semi-structured database, thus enabling the replacement of manual data operations with automation and centralization of the reliable and secure information source.

    3. Intelligent Maintenance Planning 

The challenge here is the implementation and integration of algorithms for generating operational planning, taking into account organizational constraints, the automatic generation of emergency operational plans based on critical risk level, quarterly, semi-annual, and annual maintenance planning schedules, and recommendations based on equipment priority, impacted business operations, available budgets, and maintenance teams.



    4. Modern Analytics KPI Dashboard and Workflow Automation 

The current challenge is managing the large volume of data from planning operations, integrating it with modern solutions like Power BI for generating interactive dashboards for real-time reporting, managing KPIs and automating workflows with validation/approval points and automatic notification via communication channels.

The solution implements a complete digital transformation pipeline that:

* Automates maintenance data ingestion
* Generates optimized maintenance schedules
* Stores reports securely in the cloud
* Produces interactive KPI dashboards
* Automates workflow notifications



# Project Objectives

* Replace manual maintenance planning with an automated cloud solution
* Build a serverless architecture using AWS services
* Generate intelligent maintenance schedules based on business constraints
* Create real-time KPI dashboards using Power BI
* Automate maintenance workflows using Power Automate



Key Features

* AWS Serverless Architecture
* Automated File Ingestion API
* Python Maintenance Scheduling Engine
* Interactive Power BI KPI Dashboards
* Automated Email Notifications
* Secure Amazon S3 Storage
* Budget & Maintenance Analytics
* Scalable Event-Driven Processing

---

Solution Design 

From the above requirements, I proposed the following solution design. 

1. Cloud-Based Serverless Architecture deployment

On the cloud platform side, my architectural solution is based on service integration: Amazon API Gateway, AWS Lambda, and Amazon S3. The API Gateway exposes a secure endpoint that triggers Lambda functions executing Python algorithms that embody business logic. Amazon S3 serves as a centralized database; as we manage a large volume of files, it centralizes input files and also stores generated maintenance plans as outputs, providing a unified and centralized database. This serverless architecture eliminates infrastructure management constraints, improves scalability, availability, data and file security, and, most importantly, increases on-demand processing during business peaks.
2. Automated data File Ingestion and Maintenance Operations Scheduling 

The data files containing maintenance data include equipment information, maintenance history, priority levels, and budget allocations. This data is uploaded to an Amazon S3 bucket. Once uploaded, the lambda function is triggered via the endpoint API that executes the scheduling algorithm implemented in Python. This algorithm automates the generation of optimized predictive maintenance schedules based on the following constraints: maintenance intervals, equipment criticality, previous maintenance dates, and departmental budget constraints.
3. Automated Planning Report Generation and centralized Secure Storage

The scheduling engine's role is to automatically generate maintenance plans, producing as outputs the emergency operations plan (3-month), and other plans: quarterly, 6-month, annual, biannual, and overall maintenance schedule. This automated system also manages the centralized storage of output Excel files in a dedicated Amazon S3 directory. Important KPIs such as workload distribution, maintenance priorities, and budget allocation, ensuring centralized storage and traceability, are calculated and stored as output files to facilitate integration with Power BI for dashboard creation.
4. Power BI Integration for Analytics and Reporting

The integration with Power BI enables the creation of interactive and collaborative dashboards and business intelligence reports, based on generated maintenance plans and datasets stored in Amazon S3 buckets. Users can then monitor KPIs in real-time, interactive dashboards, including KPIs such as equipment criticality, maintenance workload, budget utilization, overdue operations, and scheduling trends. With Power BI, managers can also perform data-driven analyses and automatically update maintenance plans when new data or operational constraints are added to the database.
5. Power Automate Integration for Workflow Automation and notifications

Power Automate is integrated into this design to automate the business process of generating maintenance plans and notifying managers via email channels when new plans are available or updated. This integration reduces manual intervention, improves interdepartmental collaboration, and accelerates information/KPI sharing for collaborative decision-making.


# 🏗 Solution Architecture

The project integrates several cloud and analytics services into a single automated workflow.
<img width="1313" height="468" alt="image" src="https://github.com/user-attachments/assets/dbc521c4-b0e9-4da6-a4a3-90456b8578fb" />



# Technologies Used

## Cloud

* Amazon Web Services (AWS)

  * API Gateway
  * AWS Lambda
  * Amazon S3
  * IAM

## Programming

* Python
* Pandas
* NumPy
* OpenPyXL
* Matplotlib
* Seaborn

## Microsoft Power Platform

* Power BI
* Power Automate

---

# 📋 Project Workflow

<img width="486" height="538" alt="image" src="https://github.com/user-attachments/assets/7b346b5a-9b10-4c91-a64f-9b0bbf8f172f" />



## 1. Data Ingestion

Maintenance Excel files containing:

* Equipment metadata
* Maintenance history
* Department budgets
* Maintenance priorities
* Criticality levels

are uploaded to an Amazon S3 bucket.

---

## 2. API Trigger

AWS API Gateway exposes an endpoint that triggers the Lambda function whenever a new maintenance planning request is submitted.

---

## 3. Intelligent Maintenance Planning

The Python scheduling engine generates:

* Emergency Maintenance Plan (3 Months)
* Quarterly Maintenance Plan
* 6-Month Maintenance Plan
* Annual Maintenance Plan
* Biannual Maintenance Plan
* Global Maintenance Schedule

Scheduling considers:

* Equipment criticality
* Previous maintenance dates
* Maintenance intervals
* Budget constraints
* Department priorities

---

## 4. Report Generation

The system automatically produces:

* Excel maintenance schedules
* KPI datasets
* Budget summaries
* Maintenance workload reports
* Operational dashboards

All generated reports are automatically stored in Amazon S3.

---

## 5. Business Intelligence

Power BI connects directly to generated datasets to visualize:

* Equipment Criticality
* Maintenance Workload
* Budget Distribution
* Planned vs Completed Maintenance
* Upcoming Maintenance Windows
* Department KPIs
* Operational Trends

---

## 6. Workflow Automation

Power Automate automatically:

* Sends email notifications
* Shares reports
* Starts approval workflows
* Notifies maintenance managers
* Automates recurring operational processes

Solution Implementation 

1. Create IAM Role and attach S3 policy

<img width="1275" height="763" alt="image" src="https://github.com/user-attachments/assets/3bdfefb5-6b49-4ecb-ab1d-33d4eb89b9ce" />

2. Setting up AWS S3 bucket to handle maintenance operations input data

<img width="1666" height="709" alt="image" src="https://github.com/user-attachments/assets/ba3a0bc1-a6e2-4d56-8a94-62555ccc3d4e" />

3. Configure API Gateway to handle API incoming request for Lambda function

<img width="1123" height="772" alt="image" src="https://github.com/user-attachments/assets/e8838b29-219a-49e5-9360-cae6a80c7f2c" />

4. Configure the lambda function to perform the tasks and generates maintenance plans

<img width="1324" height="760" alt="image" src="https://github.com/user-attachments/assets/968f78b4-a427-40e2-ac8c-a23527f5812b" />





# 📊 Power BI Integration for Data Analytics and Dashboard

The project includes interactive Power BI dashboards such as:

* 🚨 1.  Urgent Maintenance Operations Plan Dashboard (Up to 3 Months)

<img width="1516" height="872" alt="image" src="https://github.com/user-attachments/assets/d6179de4-4a1a-4036-be40-e11597058db4" />



* 📅 6-Month Planning Dashboard 6 Months  Plan

  <img width="1516" height="872" alt="image" src="https://github.com/user-attachments/assets/7f97c41c-e80f-4a32-aceb-d0212955a8fc" />


* 📆 Annual Maintenance Planning Dashboard

<img width="1516" height="872" alt="image" src="https://github.com/user-attachments/assets/88b06270-17fd-446c-9121-225e94d2923c" />




* 📈 Global KPI Insights Dashboard



<img width="1516" height="872" alt="image" src="https://github.com/user-attachments/assets/7d992334-1ec8-4401-ae62-ce8fea69533a" />


# Power Automate Integration and mail notifications
1.  Workflow
<img width="1744" height="969" alt="image" src="https://github.com/user-attachments/assets/0aef15bf-304f-4c1d-9e64-ee959d4e6b77" />



2. Automated Mail notification1.  Workflow1.  Workflow

<img width="1060" height="719" alt="image" src="https://github.com/user-attachments/assets/a6bd6f8c-404b-418a-ab86-6e20f8d9712d" />



# 📂 Project Structure

```
Maintenance-Planning-AWS/

│
├── input/
│   └── Maintenance_Data.xlsx
│
├── output/
│   ├── 3_Month_Plan.xlsx
│   ├── Quarterly_Plan.xlsx
│   ├── 6_Month_Plan.xlsx
│   ├── Annual_Plan.xlsx
│   ├── Biannual_Plan.xlsx
│   └── KPI_Dashboard.png
│
├── lambda/
│   └── lambda_function.py
│
├── scheduling/
│   └── maintenance_scheduler.py
│
├── powerbi/
│   └── Dashboard.pbix
│
├── powerautomate/
│   └── Workflow.png
│
├── architecture/
│   └── SystemArchitecture.png
│
└── README.md
```



---

# 📈 Results

The automated platform successfully generates:

* ✅ Emergency Maintenance Plans
<img width="1680" height="588" alt="image" src="https://github.com/user-attachments/assets/24006419-2b26-40d9-a180-8bc2574a86f0" />



* ✅ Quarterly Maintenance Plans


* ✅ 6-Month Maintenance Plans

<img width="1698" height="799" alt="image" src="https://github.com/user-attachments/assets/f992e8c3-1228-46fb-b7f7-d8c59892da20" />


* ✅ Annual Maintenance Plans

<img width="1704" height="798" alt="image" src="https://github.com/user-attachments/assets/9c3e8e35-4b39-4fd9-87f9-5b94a89d84ca" />

* ✅ Biannual Maintenance Plans
* ✅ KPI Reports
* ✅ Dashboard Visualizations
* ✅ Automated Email Notifications

All outputs are automatically archived in Amazon S3 and made available for Power BI reporting.

---

# 🎓 Learning Outcomes

This project demonstrates practical implementation of:

* Cloud Computing
* Serverless Computing
* REST APIs
* Event-Driven Architecture
* Business Intelligence
* Predictive Maintenance
* Process Automation
* Digital Transformation
* Industrial Data Analytics

---

# 🚀 Future Improvements

* AI-based predictive maintenance
* Machine Learning failure prediction
* IoT sensor integration
* DynamoDB integration
* Amazon QuickSight analytics
* SMS and Microsoft Teams notifications
* Mobile maintenance application
* Multi-factory deployment

---

# 📬 Contact

**David Roland Gnimpieba Zanfack**

Cloud Computing • Data Analytics • AWS • Power Platform • Python

Feel free to connect, provide feedback, or contribute to this project.

This README is structured to showcase the project professionally on GitHub, emphasizing architecture, business value, technologies, workflow, and outcomes in a format commonly used for portfolio projects.
