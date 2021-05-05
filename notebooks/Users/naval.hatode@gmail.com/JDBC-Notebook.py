# Databricks notebook source
jdbcdf = spark.read.format("jdbc")\
        .option("driver","org.postgresql.Driver")\
        .option("url","jdbc:postgresql://database-1.cxbcj2krdbcb.us-east-1.rds.amazonaws.com/postgres")\
        .option("dbtable","public.employee_table")\
        .option("user","postgres")\
        .option("password","QazZaq123$")\
        .load()

display(jdbcdf)

# COMMAND ----------

dbutils.help()
dbutils.fs.ls("/FileStore")

# COMMAND ----------

jdbcdf.select("ename").show()

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE TABLE Student_tbl LIKE Student LOCATION '/mnt/data_files';