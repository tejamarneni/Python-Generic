from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName("DataAuditExample").getOrCreate()

# Sample data containing hidden strings in a numeric column
data = [
    ("101", "Freight", "1250.45"),
    ("102", "Fuel", "420.00"),
    ("103", "Maintenance", "85.50"),
    ("104", "Freight", "Pending_Review"), # The hidden string
    ("105", "Storage", "310.25"),
    ("106", "Fuel", "N/A")                 # Another hidden string
]

schema = StructType([
    StructField("Tx_ID", StringType(), True),
    StructField("Category", StringType(), True),
    StructField("Amount", StringType(), True) # Read as String to be safe
])

df = spark.createDataFrame(data, schema)


# Filter for anything that is NOT a clean number/decimal
# The regex r"^\d+(\.\d+)?$" means: starts with digits, optionally ends with a dot and more digits
dirty_records = df.filter(
    ~F.col("Amount").rlike(r"^\d+(\.\d+)?$") & 
    F.col("Amount").isNotNull()
)

print("AUDIT ALERT: Found the following corrupt string values hiding in your numeric column:")
dirty_records.select("Tx_ID", "Category", "Amount").show()
