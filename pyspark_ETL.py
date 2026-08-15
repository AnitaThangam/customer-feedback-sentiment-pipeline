import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg, count

# =====================================================
# Configure PySpark
# =====================================================

python_path = os.path.abspath(".venv\\Scripts\\python.exe")
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

# =====================================================
# Create Spark Session
# =====================================================

spark = (
   SparkSession.builder
    .master("local[*]")
    .appName("Customer Feedback Sentiment Pipeline")
    .getOrCreate()
)

print("\n========== Spark Started ==========")
print("Spark Version:", spark.version)

# =====================================================
# Read Dataset
# =====================================================

df = spark.read.csv(
         "data/Customer_Reviews_Amazon.csv",
    header=True,
    inferSchema=True
)

print(df.columns)

df.show(5, truncate=False)

#spark.stop()
df.printSchema()
df.show(5, truncate=False)

print("\n========== Dataset Loaded ==========")
print("Rows :", df.count())
print("Columns :", len(df.columns))

# # =====================================================
# # Rename Columns Immediately
# # =====================================================

df = (
    df.withColumnRenamed("name", "product_name")
      .withColumnRenamed("categories", "category")
      .withColumnRenamed("reviews.date", "review_date")
      .withColumnRenamed("reviews.rating", "rating")
      .withColumnRenamed("reviews.text", "review_text")
      .withColumnRenamed("reviews.title", "review_title")
)

# # =====================================================
# # Select Required Columns
# # =====================================================

df = df.select(
    "product_name",
    "brand",
    "category",
    "review_date",
    "rating",
    "review_text",
    "review_title"
)

print("\n========== Selected Columns ==========")
print(df.columns)

# # =====================================================
# # Handle Missing Values
# # =====================================================

df = df.dropna(subset=["rating"])

df = df.fillna({
    "brand": "Unknown",
    "review_text": "",
    "review_title": "No Title"
})

# # =====================================================
# # Remove Duplicates
# # =====================================================

before = df.count()

df = df.dropDuplicates()

after = df.count()

print("\n========== Duplicate Removal ==========")
print("Rows Before :", before)
print("Rows After  :", after)
print("Duplicates Removed :", before - after)

# # =====================================================
# # Create Sentiment Column
# # =====================================================

df = df.withColumn(
    "sentiment",
    when(col("rating") >= 4, "Positive")
    .when(col("rating") == 3, "Neutral")
    .otherwise("Negative")
)

print("\n========== Sample Data ==========")

df.select(
    "product_name",
    "brand",
    "rating",
    "sentiment"
).show(10, truncate=False)

# # =====================================================
# # KPI 1 - Sentiment Distribution
# # =====================================================

print("\n========== Sentiment Distribution ==========")

df.groupBy("sentiment").count().show()

# =====================================================
# KPI 2 - Average Rating by Brand
# =====================================================

print("\n========== Average Rating by Brand ==========")

df.groupBy("brand") \
    .agg(avg("rating").alias("Average_Rating")) \
    .orderBy(col("Average_Rating").desc()) \
    .show(truncate=False)

# =====================================================
# KPI 3 - Top 10 Brands
# =====================================================

print("\n========== Top 10 Brands ==========")

df.groupBy("brand") \
    .agg(count("*").alias("Total_Reviews")) \
    .orderBy(col("Total_Reviews").desc()) \
    .show(10)

# =====================================================
# Save Clean Dataset
# =====================================================

output_path = "output/clean_customer_reviews"

df.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(output_path)

print("\n========== Dataset Saved ==========")
print(output_path)

#spark.stop()

print("\n========== ETL COMPLETED SUCCESSFULLY ==========")

# =====================================================
# Select Required Columns
# =====================================================

df = df.select(
    col("product_name"),
    col("brand"),
    col("category"),
    col("review_date"),
    col("rating"),
    col("review_text"),
    col("review_title")
)

# =====================================================
# Convert Rating to Numeric
# =====================================================

from pyspark.sql.functions import isnan

df = df.withColumn("rating", col("rating").cast("double"))

# Remove invalid ratings
df = df.filter(col("rating").isNotNull())

print("\n========== Selected Columns ==========")
df.printSchema()

# =====================================================
# Handle Missing Values
# =====================================================

df = df.fillna({
    "brand": "Unknown",
    "review_text": "",
    "review_title": "No Title"
})

# =====================================================
# Remove Duplicates
# =====================================================

before = df.count()

df = df.dropDuplicates()

after = df.count()

print("\n========== Duplicate Removal ==========")
print(f"Rows Before : {before}")
print(f"Rows After  : {after}")
print(f"Duplicates Removed : {before-after}")

# =====================================================
# Create Sentiment
# =====================================================

df = df.withColumn(
    "sentiment",
    when(col("rating") >= 4, "Positive")
    .when(col("rating") == 3, "Neutral")
    .otherwise("Negative")
)

# =====================================================
# Sample Data
# =====================================================

print("\n========== Sample Data ==========\n")

df.select(
    "product_name",
    "brand",
    "rating",
    "sentiment"
).show(10, truncate=35)

# =====================================================
# Sentiment Distribution
# =====================================================

print("\n========== Sentiment Distribution ==========\n")

df.groupBy("sentiment") \
  .count() \
  .orderBy("sentiment") \
  .show(truncate=False)

# =====================================================
# Average Rating by Brand
# =====================================================

print("\n========== Average Rating by Brand ==========\n")

df.groupBy("brand") \
  .agg(avg("rating").alias("Average Rating")) \
  .orderBy(col("Average Rating").desc()) \
  .show(20, truncate=30)

# =====================================================
# Top 10 Brands
# =====================================================

print("\n========== Top 10 Brands ==========\n")

df.groupBy("brand") \
  .count() \
  .orderBy(col("count").desc()) \
  .show(10, truncate=False)

# =====================================================
# Save Dataset
# =====================================================

output_path = "output/clean_customer_reviews"

df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(output_path)

print("\n========== Dataset Saved ==========")
print(output_path)

spark.stop()

print("\n========== ETL COMPLETED SUCCESSFULLY ==========")