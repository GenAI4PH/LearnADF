from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("App").getOrCreate()

path = r"C:\Users\keyur\Desktop\Marketing 2026\PySpark Tutorial\pyspark-glue-tutorial-main\pyspark-glue-tutorial-main\customers.csv"

df = spark.read.

df.printSchema()