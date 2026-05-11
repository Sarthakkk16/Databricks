# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM databricksansh.silver.stores_enr

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Mapping Table**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE databricksansh.silver.rls_mapping
# MAGIC (
# MAGIC   user_id STRING,
# MAGIC   region STRING 
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO databricksansh.silver.rls_mapping 
# MAGIC VALUES
# MAGIC ("anshlambaaz@gmail.com","east"),
# MAGIC ("lovelamba@gmail.com","west"),
# MAGIC ("lovelovelamba@gmail.com",'south'),
# MAGIC ('lovemelamba@gmail.com','north')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT EXISTS
# MAGIC (SELECT * FROM databricksansh.silver.rls_mapping
# MAGIC WHERE 
# MAGIC user_id = current_user() AND
# MAGIC region = 'west')

# COMMAND ----------

# MAGIC %md
# MAGIC ### **CREATE RLS FUNCTION**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION databricksansh.silver.rls_func(p_region STRING)
# MAGIC RETURNS BOOLEAN 
# MAGIC RETURN 
# MAGIC EXISTS
# MAGIC (SELECT * FROM databricksansh.silver.rls_mapping
# MAGIC WHERE 
# MAGIC user_id = current_user() AND
# MAGIC region = lower(p_region))

# COMMAND ----------

# MAGIC %md
# MAGIC ### **APPLYING FUNCTION ON REGION COLUMN**

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE databricksansh.silver.stores_enr
# MAGIC SET ROW FILTER databricksansh.silver.rls_func ON (region)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM databricksansh.silver.stores_enr

# COMMAND ----------

