# Databricks notebook source
# MAGIC %md
# MAGIC # **AUTOLOADER QUERY**

# COMMAND ----------

df = spark.readStream.format("cloudFiles")\
          .option("cloudFiles.format","csv")\
          .option("cloudFiles.schemaLocation","/Volumes/databricksansh/bronze/autovol/destination2/checkpoint/")\
          .option("cloudFiles.schemaEvolutionMode","addNewColumns")\
          .load("/Volumes/databricksansh/bronze/autovol/raw/")
          

# COMMAND ----------

df.writeStream.format("delta")\
        .outputMode("append")\
        .option("checkpointLocation","/Volumes/databricksansh/bronze/autovol/destination2/checkpoint/")\
        .trigger(once=True)\
        .option("mergeSchema",True)\
        .start("/Volumes/databricksansh/bronze/autovol/destination2/data/")

# COMMAND ----------

df = spark.read.format("delta")\
            .load("/Volumes/databricksansh/bronze/autovol/destination2/data")
display(df)

# COMMAND ----------

from pyspark.sql.functions import * 
from pyspark.sql.types import *

# COMMAND ----------

rescued_schema = StructType() \
    .add("discount", StringType()) \
    .add("payment_method", StringType())

# Parse the stringified JSON column
df = df.withColumn("rescued_struct", from_json(col("_rescued_data"), rescued_schema))

# Extract individual fields
df = df.withColumn("rescued_discount", col("rescued_struct.discount")) \
       .withColumn("rescued_payment_method", col("rescued_struct.payment_method"))

# COMMAND ----------

display(df)

# COMMAND ----------

