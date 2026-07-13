from datetime import datetime, timedelta

# 1. Define your dynamic parameters
begin_date_str = "2025-01-01"
end_date_str = "2025-12-31"

begin_date = datetime.strptime(begin_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

# 2. Dynamically generate the list of daily S3 paths
s3_base_path = "s3://my-bucket/dataset/date="
list_of_paths = []

current_date = begin_date
while current_date <= end_date:
    # Formats the date to match your S3 folder structure (e.g., s3://.../date=2025-01-01)
    date_folder = current_date.strftime("%Y-%m-%d")
    list_of_paths.append(f"{s3_base_path}{date_folder}")
    current_date += timedelta(days=1)

# 3. Hand the entire list to Spark in ONE shot using Python's argument unpacking (*)
df = spark.read.parquet(*list_of_paths)

# 4. Proceed with your cleaning and calculations
# df_clean = df.filter(...).groupBy(...)
