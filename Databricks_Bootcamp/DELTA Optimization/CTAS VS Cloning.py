# Databricks notebook source
# MAGIC %md
# MAGIC ### **CTAS**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE databricksansh.silver.ctas
# MAGIC AS 
# MAGIC SELECT * FROM databricksansh.silver.sales_enr

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM databricksansh.silver.ctas

# COMMAND ----------

# MAGIC %md
# MAGIC ### **DEEP CLONE**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE databricksansh.silver.deepclonenew
# MAGIC CLONE databricksansh.silver.sales_enr

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY databricksansh.silver.deepclone

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM databricksansh.silver.deepclone

# COMMAND ----------

# MAGIC %md
# MAGIC ### **SHALLOW CLONE**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE databricksansh.silver.shallow
# MAGIC SHALLOW CLONE databricksansh.silver.sales_enr

# COMMAND ----------

