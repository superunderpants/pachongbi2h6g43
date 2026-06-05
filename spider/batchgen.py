# 批量生成数据
import configparser
import os
import random

import pymysql
import pymssql
from pymysql.cursors import DictCursor


# 数据库连接
def db_connect():
    config = configparser.ConfigParser()
    _project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config.read(os.path.join(_project_root, 'config.ini'), encoding='utf-8-sig')

    if config.has_section('sql'):
        type = config.get('sql', 'type')
        host = config.get('sql', 'host')
        port = config.getint('sql', 'port')
        user = config.get('sql', 'user')
        password = config.get('sql', 'passwd')
        database = config.get('sql', 'db')
    elif config.has_section('db'):
        type = config.get('db', 'type')
        host = config.get('db', 'host')
        port = config.getint('db', 'port')
        user = config.get('db', 'user')
        password = config.get('db', 'password')
        database = 'pachongbi2h6g43'
    else:
        raise RuntimeError("config.ini is missing both [sql] and [db] sections")

    if type == 'mysql':
        connect = pymysql.connect(host=host, port=port, db=database, user=user, passwd=password, charset='utf8mb4', cursorclass=DictCursor)
    else:
        connect = pymssql.connect(host=host, user=user, password=password, database=database, cursorclass=DictCursor)
    return connect

def batch(tablename):
    connect = db_connect()
    cursor = connect.cursor()
    cursor.execute("show tables;")
    tables = [cursor.fetchall()]
    # 获取原有记录
    cursor.execute("SELECT * FROM "+tablename)
    records = cursor.fetchall()
    for _ in range(20000):
        # 随机选择一条原有记录
        new_data={}
        for key in records[0].keys():
            if key !="id":
                original_record = random.choice(records)
                new_data[key] = original_record[key]
        # 插入新记录
        placeholders = ', '.join(['%s'] * len(new_data))
        columns = ', '.join(new_data.keys())
        sql = "INSERT INTO "+tablename+f" ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, list(new_data.values()))

    connect.commit()
    cursor.close()
    connect.close()

if __name__ == "__main__":
    batch('autohome')
