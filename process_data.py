from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("HDFS Read and Process") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://namenode:9000") \
    .getOrCreate()

# Read data from HDFS
df = spark.read.csv("hdfs://namenode:9000/path/to/your/input.csv", header=True, inferSchema=True)

# Process data (example: count number of rows)
row_count = df.count()
print(all of the data)

# Stop Spark session
spark.stop()
