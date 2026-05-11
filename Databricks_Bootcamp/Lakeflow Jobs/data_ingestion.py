# Databricks notebook source
dbutils.widgets.text("folder_name","")
dbutils.widgets.text("parent_folder_name","")

# COMMAND ----------

folder_name = dbutils.widgets.get("folder_name")
parent_folder_name = dbutils.widgets.get("parent_folder_name")

# COMMAND ----------

df = spark.read.format("csv")\
            .option("header", "true")\
            .option("inferSchema", "true")\
            .load(f"/Volumes/databricksansh/bronze/bronze_volume/{folder_name}/")

# COMMAND ----------

df.write.format("delta")\
        .mode("overwrite")\
        .save(f"/Volumes/databricksansh/bronze/jobvolume/{parent_folder_name}/{folder_name}/")

# COMMAND ----------

