# Cloud-Based Customer Feedback Analytics & Sentiment Intelligence

## 📌 Project Overview

An end-to-end customer feedback analytics pipeline designed to transform raw Amazon customer review data into actionable business insights.

The project uses PySpark for data cleaning and transformation, Snowflake for cloud-based data storage and SQL analytics, and Power BI for executive-level visualization.

## 🏗️ Architecture

Raw Customer Reviews
        ↓
PySpark ETL
        ↓
Cleaned Customer Data
        ↓
Snowflake Cloud Data Warehouse
        ↓
SQL Analytics
        ↓
Power BI Dashboard

## 🛠️ Technologies Used

- Python
- PySpark
- SQL
- Snowflake
- Power BI
- DAX
- Pandas
- Git & GitHub

## 🔄 ETL Pipeline

1. Loaded Amazon customer review dataset using PySpark.
2. Selected relevant customer review attributes.
3. Renamed columns for analytics-friendly naming.
4. Handled missing values.
5. Removed duplicate records.
6. Created sentiment classification using customer ratings.
7. Generated sentiment distribution and brand-level KPIs.
8. Exported the cleaned dataset for cloud analytics.
9. Loaded the processed dataset into Snowflake.

## 📊 Key Analytics

- Sentiment Distribution
- Average Rating by Brand
- Top Brands by Review Count
- Customer Review Analysis
- Product and Category Analysis

## 📁 Project Structure

```text
├── dashboard/
├── data/
├── screenshots/
├── .gitignore
├── README.md
├── SQL ANALYSIS.sql
├── pyspark_ETL.py
└── requirements.txt
