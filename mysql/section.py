from pyspark.sql import SparkSession
import pyspark.sql.functions as funs




# 创建SparkSession
spark = SparkSession.builder.getOrCreate()

# 配置MySQL连接信息
mysql_prop = {'user': 'root',
              'password': '12345678',
              'driver': 'com.mysql.cj.jdbc.Driver'}
mysql_url = 'jdbc:mysql://huadi:3306/gaokao?useSSL = true & useUnicode = true & characterEncoding = utf-8 '

# 从MySQL读取Score_Table表的数据
score_table_df = spark.read.jdbc(url=mysql_url, table="Score_Table", properties=mysql_prop)

# 从MySQL读取Pro_Index表的数据
pro_index_df = spark.read.jdbc(url=mysql_url, table="Pro_Index", properties=mysql_prop)

score_table_df = score_table_df.withColumnRenamed("Pro_id", "ST_Pro_id")
pro_index_df = pro_index_df.withColumnRenamed("Pro_id", "PI_Pro_id")

# 对表进行内连接
joined_table = score_table_df.join(pro_index_df, score_table_df.ST_Pro_id == pro_index_df.PI_Pro_id)


# 按照学校名、专业ID和年份进行分组，并求最大值
result = joined_table.groupBy("ST_School_name", "Pro_name", "ST_Year", "ST_Local_batch_name").agg(funs.max(funs.col("ST_Min_section")))
result.show()
# # 将结果保存到HDFS中
# result.write.csv("hdfs://gaokao/Province_Section_Result.csv")

# # 将结果存入MySQL
result.write.jdbc(url=mysql_url, table="Province_Section_Result", mode="overwrite", properties=mysql_prop)