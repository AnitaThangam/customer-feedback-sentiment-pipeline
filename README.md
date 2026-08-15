# Cloud-Based Customer Feedback Analytics & Sentiment Intelligence

## 📌 Project Overview

This project implements an end-to-end customer feedback analytics pipeline using PySpark, Snowflake, SQL, and Power BI.

The objective is to process customer review data, clean and transform the dataset, classify customer sentiment based on ratings, perform analytical queries, and prepare the data for business intelligence reporting.

## 🏗️ Architecture

Customer Reviews CSV
        ↓
PySpark ETL
        ↓
Data Cleaning & Transformation
        ↓
Sentiment Classification
        ↓
Clean CSV Dataset
        ↓
Snowflake Cloud Data Warehouse
        ↓
SQL Analysis
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
- NumPy
- Git & GitHub

## 🔄 ETL Pipeline

The PySpark pipeline performs:

1. Dataset ingestion
2. Schema inspection
3. Column selection
4. Column renaming
5. Missing-value handling
6. Duplicate removal
7. Sentiment classification
8. Data quality checks
9. KPI generation
10. Export of cleaned dataset

## 😊 Sentiment Classification

Customer sentiment is classified using review ratings:

| Rating | Sentiment |
|--------|-----------|
| 4–5 | Positive |
| 3 | Neutral |
| 1–2 | Negative |

## 📊 Analytics

The project includes SQL analysis for:

- Sentiment distribution
- Average rating by brand
- Top brands by review volume
- Customer feedback analysis
- Product-level review insights

## ☁️ Cloud Data Warehouse

The cleaned customer review dataset is loaded into Snowflake for scalable cloud-based storage and analytical querying.

Database:

`CUSTOMER_FEEDBACK_DB`

Schema:

`ANALYTICS`

Table:

`CUSTOMER_REVIEWS`

## 📈 Business Intelligence

The processed dataset is prepared for Power BI to build an executive dashboard containing:

- Total Reviews
- Average Rating
- Positive / Neutral / Negative Reviews
- Sentiment Distribution
- Brand Performance
- Customer Feedback Trends

## 📂 Repository Structure

```text
├── dashboard/
├── data/
├── screenshots/
├── .gitignore
├── README.md
├── SQL ANALYSIS.sql
├── pyspark_ETL.py
└── requirements.txt
