from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Read Parquet from S3") \
    .getOrCreate()

# Set AWS S3 credentials
aws_access_key_id = "YOUR_AWS_ACCESS_KEY_ID"
aws_secret_access_key = "YOUR_AWS_SECRET_ACCESS_KEY"

# Set S3 bucket and object key
s3_bucket_name = "your-bucket-name"
s3_object_key = "path/to/your/parquet/file.parquet"

# Read the Parquet file from S3
df = spark.read.parquet(f"s3a://{s3_bucket_name}/{s3_object_key}")

# Print the schema of the DataFrame
df.printSchema()

# Show the first few rows of the DataFrame
df.show()

# Stop the SparkSession
spark.stop()
