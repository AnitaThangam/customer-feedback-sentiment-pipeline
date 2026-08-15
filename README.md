# Cloud-Based Customer Feedback Analytics & Sentiment Intelligence Pipeline

## Overview

An end-to-end customer feedback analytics pipeline built using Python, PySpark, Snowflake, SQL, and Power BI to transform raw Amazon customer reviews into analytics-ready data.

## Business Problem

Customer review data can be difficult to process and analyze at scale. This project builds an automated data pipeline to clean customer review data, perform sentiment classification, store curated data in Snowflake, and generate business insights using SQL and Power BI.

## Tech Stack

- Python
- PySpark
- Pandas
- SQL
- Snowflake
- Power BI
- DAX
- Git & GitHub

## Project Pipeline

Raw Customer Reviews  
↓  
PySpark ETL  
↓  
Data Cleaning & Transformation  
↓  
Duplicate Removal & Missing Value Handling  
↓  
Sentiment Classification  
↓  
Snowflake Data Warehouse  
↓  
SQL Analytics  
↓  
Power BI Dashboard

## Key Features

- Processed 34,627+ customer reviews
- Built PySpark ETL transformations
- Cleaned and standardized customer review data
- Removed duplicate records
- Implemented rating-based sentiment classification
- Loaded curated data into Snowflake
- Developed SQL analytics and business KPIs
- Prepared data for Power BI dashboarding

## Sentiment Classification

| Rating | Sentiment |
|---|---|
| 4–5 | Positive |
| 3 | Neutral |
| 1–2 | Negative |

## SQL Analytics

The project analyzes:

- Total Reviews
- Average Rating
- Sentiment Distribution
- Brand Performance
- Product Performance
- Category Trends
- Monthly Review Trends
- Highest and Lowest Rated Brands

## Project Structure

```text
customer-feedback-sentiment-pipeline/
│
├── data/
├── src/
│   ├── pyspark_ETL.py
│   └── snowflake_queries.sql
│
├── dashboard/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
