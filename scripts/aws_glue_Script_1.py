import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import current_date
import random

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# ✅ Output path
output_path = "s3://datalakebg/output/students/"

# ✅ Generate Student Data
names = ["Alice", "Bob", "John", "Ravi", "Mike", "Sara"]
countries = ["IN", "US", "UK", "CA"]

data = []

for i in range(1, 101):  # 100 records
    data.append((
        i,
        random.choice(names),
        random.choice(countries),
        random.randint(18, 25)
    ))

# ✅ Create DataFrame
df = spark.createDataFrame(data, ["student_id", "name", "country", "age"])

# ✅ Add registration_date column

df = df.withColumn("registration_date", current_date())

# ✅ Write partitioned data to S3
df.write \
    .mode("overwrite") \
    .partitionBy("registration_date") \
    .parquet(output_path)

print("✅ Student Data Generated & Stored Successfully")


job.commit()