# Databricks notebook source
# MAGIC %md
# MAGIC # Volumes

# COMMAND ----------

# MAGIC %sql 
# MAGIC
# MAGIC drop volume if exists databricksar.bronze.bronze_volume;
# MAGIC create volume databricksar.bronze.bronze_volume

# COMMAND ----------

dbutils.fs.mkdirs("/Volumes/databricksar/bronze/bronze_volume/sales")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from csv.`/Volumes/databricksar/bronze/bronze_volume/sales/fact_sales.csv`;

# COMMAND ----------

# MAGIC %md
# MAGIC # DBUTILS

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.ls("/Volumes/databricksar/bronze/bronze_volume/sales/")

# COMMAND ----------

dbutils.fs.mkdirs("/Volumes/databricksar/bronze/bronze_volume/customers")

# COMMAND ----------

dbutils.fs.cp("/Volumes/databricksar/bronze/bronze_volume/sales/","/Volumes/databricksar/bronze/bronze_volume/customers/", True)

# COMMAND ----------

dbutils.fs.rm("/Volumes/databricksar/bronze/bronze_volume/customers/fact_sales")

# COMMAND ----------

dbutils.fs.put("/Volumes/databricksar/bronze/bronze_volume/customers/text.txt","text")

# COMMAND ----------

dbutils.fs.rm("/Volumes/databricksar/bronze/bronze_volume/customers/fact_sales.csv")

# COMMAND ----------

all_items = dbutils.fs.ls("/Volumes/databricksar/bronze/bronze_volume/customers/")
all_items

# COMMAND ----------

file_names = [i.name for i in all_items]
file_names

# COMMAND ----------

for i in file_names:
    dbutils.fs.rm("/Volumes/databricksar/bronze/bronze_volume/customers/(i)")

# COMMAND ----------

dbutils.widgets.text("para1","")

# COMMAND ----------

para_value = dbutils.widgets.get("para1")
para_value

# COMMAND ----------

