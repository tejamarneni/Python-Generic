'''
Loading Data from S3 Bucket to Snowflake Table using PySpark
This script uses PySpark to read data from an S3 bucket and load it into a Snowflake table.
Prerequisites
Apache Spark installed and configured
PySpark installed (pip install pyspark)
Snowflake Spark Connector installed (pip install snowflake-connector-python)
AWS S3 bucket with necessary credentials (access key ID, secret access key)
Sample Script
Python'''

--------------------------------------------------------------------------------------------------------------------------------------------------------
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Spark configuration
spark = SparkSession.builder \
    .appName("S3 to Snowflake") \
    .config("spark.jars.packages", "net.snowflake:snowflake-jdbc:3.13.10,net.snowflake:spark-snowflake_2.12:2.9.0") \
    .config("spark.driver.extraClassPath", "/path/to/snowflake/jdbc/driver.jar") \
    .getOrCreate()

# S3 configuration
s3_access_key_id = "your_access_key_id"
s3_secret_access_key = "your_secret_access_key"
s3_bucket_name = "your_bucket_name"
s3_object_key = "your_object_key.csv"

# Snowflake configuration
snowflake_account = "your_account_name"
snowflake_user = "your_username"
snowflake_password = "your_password"
snowflake_warehouse = "your_warehouse_name"
snowflake_database = "your_database_name"
snowflake_schema = "your_schema_name"
snowflake_table_name = "your_table_name"

# Read data from S3
df = spark.read.csv(f"s3a://{s3_bucket_name}/{s3_object_key}", header=True, inferSchema=True)

# Write data to Snowflake
df.write.format("net.snowflake.spark.snowflake") \
    .options(
        sfAccount=snowflake_account,
        sfUser=snowflake_user,
        sfPassword=snowflake_password,
        sfWarehouse=snowflake_warehouse,
        sfDatabase=snowflake_database,
        sfSchema=snowflake_schema,
        sfTable=snowflake_table_name
    ) \
    .option("dbtable", snowflake_table_name) \
    .mode("append") \
    .save()

# Stop Spark session
spark.stop()
'''
Replace the placeholders with your actual S3 and Snowflake credentials, bucket names, object keys, and table names.
Notes
Make sure to install the Snowflake Spark Connector and add the Snowflake JDBC driver to your Spark configuration.
Adjust the sfTable option to match your Snowflake table name.'''
This script assumes a simple CSV file structure. If your file has a more complex structure, you may need to modify the read.csv options accordingly.
