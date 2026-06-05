import configparser
import re
import json
import os
import mysql.connector
from django.http import JsonResponse
from hdfs import InsecureClient
from pyhive import hive
import csv
from util.configread import config_read
from util.CustomJSONEncoder import CustomJsonEncoder
from util.codes import normal_code, system_error_code
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format
import shutil
# 获取当前文件路径的根目录
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

m_username = "Administrator"
hadoop_client = InsecureClient('http://localhost:9870', user='hadoop')

dbtype, host, port, user, passwd, dbName, charset,hasHadoop = config_read(os.path.join(parent_directory,"config.ini"))

#将mysql里的相关表转成hive库里的表
def migrate_to_hive():

    mysql_conn = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=passwd,
        database=dbName
    )
    cursor = mysql_conn.cursor()

    hive_conn = hive.Connection(
        host='localhost',
        port=10000,
        username=m_username,
    )
    hive_cursor = hive_conn.cursor()
    #创建Hive数据库（如果不存在）
    hive_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbName}")
    hive_cursor.execute(f"USE {dbName}")

    autohome_table_path=f'/user/hive/warehouse/{dbName}.db/autohome'
    #删除已有的hive表
    if hadoop_client.status(autohome_table_path,strict=False):
        hadoop_client.delete(autohome_table_path, recursive=True)
    # 在Hive中删除表
    autohome_drop_table_query = f"""DROP TABLE autohome"""
    hive_cursor.execute(autohome_drop_table_query)
    cursor.execute("SELECT * FROM autohome")
    autohome_column_info = cursor.fetchall()
    #将数据写入 CSV 文件
    autohome_path = os.path.join(parent_directory, "autohome.csv")
    with open(autohome_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        # 写入数据行
        for row in autohome_column_info:
            clean_row = [str(field).replace('\t', '').replace('\n', '') for field in row]  # 把每个字段的 \t 替换为空
            writer.writerow(clean_row)
    autohome_spakr_clear(autohome_path)
    cursor.execute("DESCRIBE autohome")
    autohome_column_info = cursor.fetchall()
    create_table_query = "CREATE TABLE IF NOT EXISTS autohome ("
    for column, data_type, _, _, _, _ in autohome_column_info:
        match = re.match(r'(\w+)(\(\d+\))?', data_type)
        mysql_type = match.group(1)
        hive_data_type = get_hive_type(mysql_type)
        create_table_query += f"{column} {hive_data_type}, "
    autohome_create_table_query = create_table_query[:-2] + ") row format delimited fields terminated by '\t'"
    hive_cursor.execute(autohome_create_table_query)
    # 上传映射文件
    autohome_hdfs_csv_path = f'/user/hive/warehouse/{dbName}.db/autohome'
    hadoop_client.upload(autohome_hdfs_csv_path, autohome_path)
    xingyezixun_table_path=f'/user/hive/warehouse/{dbName}.db/xingyezixun'
    #删除已有的hive表
    if hadoop_client.status(xingyezixun_table_path,strict=False):
        hadoop_client.delete(xingyezixun_table_path, recursive=True)
    # 在Hive中删除表
    xingyezixun_drop_table_query = f"""DROP TABLE xingyezixun"""
    hive_cursor.execute(xingyezixun_drop_table_query)
    cursor.execute("SELECT * FROM xingyezixun")
    xingyezixun_column_info = cursor.fetchall()
    #将数据写入 CSV 文件
    xingyezixun_path = os.path.join(parent_directory, "xingyezixun.csv")
    with open(xingyezixun_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        # 写入数据行
        for row in xingyezixun_column_info:
            clean_row = [str(field).replace('\t', '').replace('\n', '') for field in row]  # 把每个字段的 \t 替换为空
            writer.writerow(clean_row)
    xingyezixun_spakr_clear(xingyezixun_path)
    cursor.execute("DESCRIBE xingyezixun")
    xingyezixun_column_info = cursor.fetchall()
    create_table_query = "CREATE TABLE IF NOT EXISTS xingyezixun ("
    for column, data_type, _, _, _, _ in xingyezixun_column_info:
        match = re.match(r'(\w+)(\(\d+\))?', data_type)
        mysql_type = match.group(1)
        hive_data_type = get_hive_type(mysql_type)
        create_table_query += f"{column} {hive_data_type}, "
    xingyezixun_create_table_query = create_table_query[:-2] + ") row format delimited fields terminated by '\t'"
    hive_cursor.execute(xingyezixun_create_table_query)
    # 上传映射文件
    xingyezixun_hdfs_csv_path = f'/user/hive/warehouse/{dbName}.db/xingyezixun'
    hadoop_client.upload(xingyezixun_hdfs_csv_path, xingyezixun_path)
    cursor.close()
    mysql_conn.close()
    hive_cursor.close()
    hive_conn.close()

#转换成hive的类型
def get_hive_type(mysql_type):
    type_mapping = {
        'INT': 'INT',
        'BIGINT': 'BIGINT',
        'FLOAT': 'FLOAT',
        'DOUBLE': 'DOUBLE',
        'DECIMAL': 'DECIMAL',
        'VARCHAR': 'STRING',
        'TEXT': 'STRING',
    }
    if isinstance(mysql_type, str):
        mysql_type = mysql_type.upper()
    return type_mapping.get(str(mysql_type), 'STRING')

#执行hive查询
def hive_query():
    # 连接到Hive服务器
    conn = hive.Connection(host='localhost', port=10000, username=m_username,database=dbName)
    # 创建一个游标对象
    cursor = conn.cursor()
    try:

        #定义Hive查询语句
        zuozhe_query = "SELECT COUNT(*) AS total, zuozhe FROM autohome GROUP BY zuozhe"
        # 执行Hive查询语句
        cursor.execute(zuozhe_query)
        # 获取查询结果
        zuozhe_results = cursor.fetchall()
        zuozhe_json_list=[]
        for row in zuozhe_results:
            zuozhe_json_list.append({"zuozhe":row[1],"total":row[0]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "autohome_groupzuozhe.json"), 'w', encoding='utf-8') as f:
            json.dump(zuozhe_json_list, f, ensure_ascii=False, indent=4)


        #定义Hive查询语句
        zixunfenlei_query = "SELECT COUNT(*) AS total, zixunfenlei FROM xingyezixun GROUP BY zixunfenlei"
        # 执行Hive查询语句
        cursor.execute(zixunfenlei_query)
        # 获取查询结果
        zixunfenlei_results = cursor.fetchall()
        zixunfenlei_json_list=[]
        for row in zixunfenlei_results:
            zixunfenlei_json_list.append({"zixunfenlei":row[1],"total":row[0]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "xingyezixun_groupzixunfenlei.json"), 'w', encoding='utf-8') as f:
            json.dump(zixunfenlei_json_list, f, ensure_ascii=False, indent=4)


        #定义Hive查询语句
        fabushijian_query = "SELECT COUNT(*) AS total, fabushijian FROM xingyezixun GROUP BY fabushijian"
        # 执行Hive查询语句
        cursor.execute(fabushijian_query)
        # 获取查询结果
        fabushijian_results = cursor.fetchall()
        fabushijian_json_list=[]
        for row in fabushijian_results:
            fabushijian_json_list.append({"fabushijian":row[1],"total":row[0]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "xingyezixun_groupfabushijian.json"), 'w', encoding='utf-8') as f:
            json.dump(fabushijian_json_list, f, ensure_ascii=False, indent=4)

        where = ' WHERE 1 = 1 '
        title_query = f'''SELECT `title`, ROUND(SUM(`liulan`), 2) AS `total`
            FROM autohome {where} GROUP BY `title`'''
        #执行Hive查询语句
        cursor.execute(title_query)
        # 获取查询结果
        title_results = cursor.fetchall()
        title_json_list=[]
        for row in title_results:
            title_json_list.append({"title":row[0],"total":row[1]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "autohome_valuetitleliulan.json"), 'w', encoding='utf-8') as f:
            json.dump(title_json_list, f, ensure_ascii=False, indent=4)
        where = ' WHERE 1 = 1 '
        zixunbiaoti_query = f'''SELECT `zixunbiaoti`, ROUND(SUM(`clicknum`), 2) AS `total`
            FROM xingyezixun {where} GROUP BY `zixunbiaoti`'''
        #执行Hive查询语句
        cursor.execute(zixunbiaoti_query)
        # 获取查询结果
        zixunbiaoti_results = cursor.fetchall()
        zixunbiaoti_json_list=[]
        for row in zixunbiaoti_results:
            zixunbiaoti_json_list.append({"zixunbiaoti":row[0],"total":row[1]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "xingyezixun_valuezixunbiaoticlicknum.json"), 'w', encoding='utf-8') as f:
            json.dump(zixunbiaoti_json_list, f, ensure_ascii=False, indent=4)
        where = ' WHERE 1 = 1 '
        zixunbiaoti_query = f'''SELECT `zixunbiaoti`, ROUND(SUM(`storeupnum`), 2) AS `total`
            FROM xingyezixun {where} GROUP BY `zixunbiaoti`'''
        #执行Hive查询语句
        cursor.execute(zixunbiaoti_query)
        # 获取查询结果
        zixunbiaoti_results = cursor.fetchall()
        zixunbiaoti_json_list=[]
        for row in zixunbiaoti_results:
            zixunbiaoti_json_list.append({"zixunbiaoti":row[0],"total":row[1]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "xingyezixun_valuezixunbiaotistoreupnum.json"), 'w', encoding='utf-8') as f:
            json.dump(zixunbiaoti_json_list, f, ensure_ascii=False, indent=4)
        pass
    except Exception as e:
         print(f"An error occurred: {e}")
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()

#spark数据清洗和预处理
def autohome_spakr_clear(csvpath):
    try:
        #创建Spark会话
        spark = SparkSession.builder.appName("pachongbi2h6g43").getOrCreate()
        df = spark.read.csv(csvpath, header=False, inferSchema=True)
        df = df.toDF(
            "id",
            "addtime",
            "title",
            "imgurl",
            "neirong",
            "xqurl",
            "zuozhe",
            "fbtime",
            "alltext",
            "liulan",
            "fbaddress",
            "thumbsupnum",
            "crazilynum",
            "clicktime",
            "clicknum",
            "discussnum",
            "totalscore",
            "storeupnum",
        )
        #显示原始数据
        df.show()
        #1.删除空值
        df_cleaned = df.dropna()
        #2.去除重复行
        df_cleaned = df_cleaned.dropDuplicates()
        df_cleaned = df_cleaned.withColumn("addtime", date_format(col("addtime"), 'yyyy-MM-dd HH:mm:ss'))
        df_cleaned = df_cleaned.withColumn("clicktime", date_format(col("clicktime"), 'yyyy-MM-dd HH:mm:ss'))
        #显示清洗后的数据
        df_cleaned.show()
        #保存清洗后的数据
        print(type(df_cleaned))
        output_path = 'autohome_output_dir'  # 输出的目录
        df_cleaned.coalesce(1).write.csv(output_path, header=False, mode="overwrite")
        #手动移动生成的 CSV 文件到目标路径，并重命名
        for filename in os.listdir(output_path):
            if filename.startswith("part-") and filename.endswith(".csv"):
                shutil.move(os.path.join(output_path, filename), csvpath)
        #清理临时目录
        shutil.rmtree(output_path)
        #停止Spark会话
        spark.stop()
    except Exception as e:
        print("e:",e)
#spark数据清洗和预处理
def xingyezixun_spakr_clear(csvpath):
    try:
        #创建Spark会话
        spark = SparkSession.builder.appName("pachongbi2h6g43").getOrCreate()
        df = spark.read.csv(csvpath, header=False, inferSchema=True)
        df = df.toDF(
            "id",
            "addtime",
            "zixunbiaoti",
            "fengmian",
            "zixunfenlei",
            "faburen",
            "fabushijian",
            "jianjie",
            "zixunneirong",
            "thumbsupnum",
            "crazilynum",
            "clicktime",
            "clicknum",
            "discussnum",
            "totalscore",
            "storeupnum",
        )
        #显示原始数据
        df.show()
        #1.删除空值
        df_cleaned = df.dropna()
        #2.去除重复行
        df_cleaned = df_cleaned.dropDuplicates()
        df_cleaned = df_cleaned.withColumn("addtime", date_format(col("addtime"), 'yyyy-MM-dd HH:mm:ss'))
        df_cleaned = df_cleaned.withColumn("fabushijian", date_format(col("fabushijian"), 'yyyy-MM-dd'))
        df_cleaned = df_cleaned.withColumn("clicktime", date_format(col("clicktime"), 'yyyy-MM-dd HH:mm:ss'))
        #显示清洗后的数据
        df_cleaned.show()
        #保存清洗后的数据
        print(type(df_cleaned))
        output_path = 'xingyezixun_output_dir'  # 输出的目录
        df_cleaned.coalesce(1).write.csv(output_path, header=False, mode="overwrite")
        #手动移动生成的 CSV 文件到目标路径，并重命名
        for filename in os.listdir(output_path):
            if filename.startswith("part-") and filename.endswith(".csv"):
                shutil.move(os.path.join(output_path, filename), csvpath)
        #清理临时目录
        shutil.rmtree(output_path)
        #停止Spark会话
        spark.stop()
    except Exception as e:
        print("e:",e)
    # hive分析
def shive_analyze(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        try:
            migrate_to_hive()
            hive_query()
            return JsonResponse(msg, encoder=CustomJsonEncoder)
        except Exception as e:
            msg['code'] = system_error_code
            msg['msg'] = f"发生错误：{e}"
            return JsonResponse(msg, encoder=CustomJsonEncoder)



