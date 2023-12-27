# Databricks notebook source
# MAGIC %run /GeekCoders/Utlilities

# COMMAND ----------

# MAGIC %py
# MAGIC insert_query="select count(*) from mart_geekcoders.dim_uniquecarrier group by code having count(*)>1"
# MAGIC insert_test_cases("mart_geekcoders",1,"Check if code is duplicated in the dim_uniquecarrier or not ",insert_query,0)

# COMMAND ----------

# MAGIC %py
# MAGIC insert_query="select count(*) from mart_geekcoders.dim_airport group by code having count(*)>1"
# MAGIC insert_test_cases("mart_geekcoders",2,"Check if code is duplicated in the dim_airport or not ",insert_query,0)
