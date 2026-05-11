# Databricks notebook source
# MAGIC %md
# MAGIC ### **CREATE THE MASK FUNCTIONS**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION databricksansh.silver.dynamic_mask(p_email STRING)
# MAGIC RETURN CASE WHEN is_account_group_member('developers') THEN p_email ELSE '***' END;

# COMMAND ----------

# MAGIC %md
# MAGIC ### **APPLYING MASK**

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE databricksansh.silver.customers_enr
# MAGIC ALTER COLUMN email SET MASK databricksansh.silver.dynamic_mask

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM databricksansh.silver.customers_enr

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM databricksansh.silver.stores_enr

# COMMAND ----------

