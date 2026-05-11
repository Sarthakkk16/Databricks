# Databricks notebook source
# MAGIC %md
# MAGIC # **Volumes**

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE VOLUME databricksansh.bronze.bronze_volume
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM csv.`/Volumes/databricksansh/bronze/bronze_volume/sales/fact_sales.csv`

# COMMAND ----------

# MAGIC %md
# MAGIC # **DBUTILS**

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.ls("/Volumes/databricksansh/bronze/bronze_volume/sales/")

# COMMAND ----------

dbutils.fs.mkdirs("/Volumes/databricksansh/bronze/bronze_volume/customers")

# COMMAND ----------

dbutils.fs.cp("/Volumes/databricksansh/bronze/bronze_volume/sales/","/Volumes/databricksansh/bronze/bronze_volume/customers/",True)

# COMMAND ----------

dbutils.fs.rm("/Volumes/databricksansh/bronze/bronze_volume/customers/fact_sales.csv")

# COMMAND ----------

dbutils.fs.put("/Volumes/databricksansh/bronze/bronze_volume/customers/test.py","print(Hello Ansh Lamba)",True)

# COMMAND ----------

all_items = dbutils.fs.ls("/Volumes/databricksansh/bronze/bronze_volume/customers/")
all_items

# COMMAND ----------

file_names = [i.name for i in all_items]
file_names

# COMMAND ----------

for i in file_names:
    dbutils.fs.rm(f"/Volumes/databricksansh/bronze/bronze_volume/customers/{i}")

# COMMAND ----------

dbutils.widgets.text("par1","")

# COMMAND ----------

par1_value = dbutils.widgets.get("par1")
par1_value

# COMMAND ----------

