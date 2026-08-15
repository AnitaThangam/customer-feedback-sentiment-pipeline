# Data

## Dataset

This project uses an Amazon customer reviews dataset containing customer feedback and product information.

The dataset includes fields such as:

- Product Name
- Brand
- Category
- Review Date
- Rating
- Review Text
- Review Title

## Data Processing

The raw dataset was processed using PySpark.

The ETL pipeline performs:

1. Data ingestion
2. Column selection
3. Column renaming
4. Missing-value handling
5. Duplicate removal
6. Sentiment classification
7. Data quality checks
8. Export of the cleaned dataset

## Processed Data

The cleaned dataset is used for:

- Snowflake data warehousing
- SQL analysis
- Power BI reporting

## Dataset Availability

The raw CSV dataset is not included in this repository to keep the repository lightweight and avoid redistributing the source dataset.

The complete transformation logic is available in:

`pyspark_ETL.py`
