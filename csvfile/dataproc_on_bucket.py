import pyspark
from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()
data =[(1,'ketu','98'),(1,'ketu','98')]
df=spark.createDataFrame(data,['id','name','salary'])
df.write.json("gs://nk-dataproc/pyspark_op_json.json",mode='overwrite')