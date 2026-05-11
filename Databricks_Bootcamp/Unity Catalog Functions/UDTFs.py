# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION databricksansh.bronze.udtf(p_para INT)
# MAGIC RETURNS TABLE 
# MAGIC RETURN 
# MAGIC (
# MAGIC   SELECT * FROM databricksansh.SILVER.sales_enr WHERE total_amount > p_para
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM databricksansh.bronze.udtf(100)

# COMMAND ----------

