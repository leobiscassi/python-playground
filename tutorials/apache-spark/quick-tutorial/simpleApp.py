from pyspark.sql import SparkSession

logFile = "/usr/local/spark/README.md"
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: {}, lines with b: {}".format(numAs, numBs))

spark.stop()