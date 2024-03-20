from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import lit


spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_Tutorial')\
        .getOrCreate()


data_schema_product = [
               StructField('product', StringType()),
            ]

data_schema_category = [
               StructField('category', StringType()),
            ]

data_schema_category_product = [
               StructField('category', StringType()),
               StructField('product', StringType()),
            ]

product_struc = StructType(fields=data_schema_product)
category_struc = StructType(fields=data_schema_category)
category_product_struc = StructType(fields=data_schema_category_product)

data = spark.read.csv(
    'product.csv',
    sep=';',
    header=True,
    schema=product_struc
)
data2 = spark.read.csv(
    'category.csv',
    sep=';',
    header=True,
    schema=category_struc
)
data3 = spark.read.csv(
    'category_product.csv',
    sep=';',
    header=True,
    schema=category_product_struc
)


data2.printSchema()
data3.select(['category', 'product']).show()
uniq_product = data3.select('product').distinct()
list_products_with_category = tuple([i.product for i in uniq_product.take(uniq_product.count())])
print(list_products_with_category)
res_data = data.where(f'product NOT IN {list_products_with_category}')
res_data = res_data.withColumn('category', lit('None'))
res_data = data3.unionByName(res_data)
res_data.show()

