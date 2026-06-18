from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Paths
input_path = "s3://datalakebg/input/raw_data/"
output_path = "s3://datalakebg/output/res_output/"

# Read data
df = spark.read.option("header", "true").csv(input_path)

# Transformation
from pyspark.sql.functions import col
df_transformed = df.withColumn(
    "amount_with_tax", col("amount").cast("double") * 1.1
)

# Write partitioned output
df_transformed.write.mode("overwrite") \
    .partitionBy("country") \
    .parquet(output_path)