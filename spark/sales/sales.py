import sys
from pyspark import SparkContext

if(len(sys.argv)!=4):
	print("Provide Input File and Output Directory")
	sys.exit(0)

sc =SparkContext()
f = sc.textFile(sys.argv[1])

# Total products
temp=f.map(lambda x: (x.split(',')[7],1))
data=temp.countByKey()
dd=sc.parallelize(data.items())
dd.saveAsTextFile(sys.argv[2])

# Frequency
temp=f.map(lambda x: (x.split(',')[3],1))
data=temp.countByKey()
dd=sc.parallelize(data.items())
dd.saveAsTextFile(sys.argv[3])
