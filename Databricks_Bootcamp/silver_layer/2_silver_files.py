# Databricks notebook source
# MAGIC %md
# MAGIC ### **Text Files**

# COMMAND ----------

with open("/Workspace/Databricks_Bootcamp/silver_layer/file.txt","r") as f:
    content = f.read()

print(content)

# COMMAND ----------

with open("/Workspace/Databricks_Bootcamp/silver_layer/newfile.txt","w") as f:
    f.write("my_secret = '1234'")

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Python Files**

# COMMAND ----------

with open("/Workspace/Databricks_Bootcamp/silver_layer/newfile.py","w") as f:
    f.write("my_secret = '1234'")

# COMMAND ----------

import newfile

# COMMAND ----------

newfile.my_secret

# COMMAND ----------

# MAGIC %md
# MAGIC ### **JSON FILES Using Pandas [MAPPING FILES]**

# COMMAND ----------

import pandas as pd

df = pd.read_json("/Workspace/Databricks_Bootcamp/silver_layer/mappings.json")
df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Convert it into a PySpark Dataframe**

# COMMAND ----------

df_pyspark = spark.createDataFrame(df)

display(df_pyspark)

# COMMAND ----------

