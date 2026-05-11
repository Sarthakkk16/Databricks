# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM parquet.`/Volumes/databricksansh/bronze/autovol/copyinto/part-00000-tid-1800520145580676501-2fb00642-a896-4599-9957-2c7260f04aa7-132-1.c000.snappy.parquet`

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS databricksansh.bronze.copyintotbl

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE databricksansh.bronze.copyintotbl
# MAGIC (
# MAGIC   order_id INT,
# MAGIC   customer_id INT,
# MAGIC   order_date DATE,
# MAGIC   order_amount DOUBLE,
# MAGIC   order_status string
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC COPY INTO databricksansh.bronze.copyintotbl
# MAGIC FROM "/Volumes/databricksansh/bronze/autovol/copyinto/"
# MAGIC FILEFORMAT = PARQUET
# MAGIC FORMAT_OPTIONS ('mergeSchema'= "True")
# MAGIC COPY_OPTIONS ('mergeSchema'= "True")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM databricksansh.bronze.copyintotbl

# COMMAND ----------

    