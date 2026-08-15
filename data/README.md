# Data

The project uses an Amazon customer reviews dataset containing product information, brands, categories, ratings, review text, review titles, and review dates.

The raw dataset is not included in this repository because of file-size and dataset distribution considerations.

## Data Flow

```text
Raw Amazon Customer Reviews
        ↓
PySpark ETL
        ↓
Cleaned & Transformed Data
        ↓
Snowflake
        ↓
SQL Analytics
        ↓
Power BI
