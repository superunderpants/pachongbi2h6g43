# coding:utf-8
import click,py_compile,os
from configparser import ConfigParser
from util.configread import config_read
from util.sqlinit import Create
@click.group()
def sub():
    pass


@click.command()
def initdb(ini="config.ini"):
    dbtype, host, port, user, passwd, dbName, charset,_ = config_read(ini)
    if dbtype == 'mysql':
        cm = Create(dbtype, host, port, user, passwd, dbName, charset)
        cm.create_db("CREATE DATABASE IF NOT EXISTS  `{}`  /*!40100 DEFAULT CHARACTER SET utf8 */ ;".format(dbName))

        cm.conn_close()
    elif dbtype == 'mssql':
        cm = Create(dbtype, host, port, user, passwd, dbName, charset)
        cm.create_db("CREATE DATABASE IF NOT EXISTS  `{}` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;".format(dbName))

        cm.conn_close()
    else:
        print('请修改当前面目录下的config.ini文件')

@click.command()
def initsql(ini="config.ini"):
    dbtype, host, port, user, passwd, dbName, charset,_ = config_read(ini)
    if dbtype == 'mysql':
        cm = Create(dbtype, host, port, user, passwd, dbName, charset)
        cm.create_db("CREATE DATABASE IF NOT EXISTS  `{}`  /*!40100 DEFAULT CHARACTER SET utf8 */ ;".format(dbName))
        with open("./db/pachongbi2h6g43.sql", encoding="utf8") as f:
            createsql = f.read()
        createsql = "DROP TABLE" + createsql.split('DROP TABLE', 1)[-1]
        cm.create_tables(createsql.split(';\n')[:-1])
        cm.conn_close()
    elif dbtype == 'mssql':
        cm = Create(dbtype, host, port, user, passwd, dbName, charset)
        cm.create_db("CREATE DATABASE IF NOT EXISTS  `{}` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;".format(dbName))
        with open("./db/mssql.sql", encoding="utf8") as f:
            createsql = f.read()
        createsql = "DROP TABLE" + createsql.split('DROP TABLE', 1)[-1]
        cm.create_tables(createsql.split(';\n')[:-1])
        cm.conn_close()
    else:
        print('请修改当前面目录下的config.ini文件')

@click.command()
def initconfig(ini="config.ini"):
    """只导入 config 表初始数据，不删除已有数据"""
    dbtype, host, port, user, passwd, dbName, charset,_ = config_read(ini)
    if dbtype == 'mysql':
        cm = Create(dbtype, host, port, user, passwd, dbName, charset)
        cm.create_db("CREATE DATABASE IF NOT EXISTS  `{}`  /*!40100 DEFAULT CHARACTER SET utf8 */ ;".format(dbName))
        use_sql = '''use `{}`;'''.format(dbName)
        cm.cur.execute(use_sql)

        config_sqls = [
            "INSERT INTO config (id, name, value, url, type) VALUES (1,'picture1','upload/picture1.jpg','',1),(2,'picture2','upload/picture2.jpg','',1),(3,'picture3','upload/picture3.jpg','',1) ON DUPLICATE KEY UPDATE value=VALUES(value);",
            "INSERT INTO config (id, name, value, url, type) VALUES (14,'deepseek','{\"key\":\"\"}','',2) ON DUPLICATE KEY UPDATE name=VALUES(name);",
            "INSERT INTO config (id, name, value, url, type) VALUES (21,'bLoginBackgroundImg','','',3),(22,'bRegisterBackgroundImg','','',3),(23,'bIndexBackgroundImg','','',3),(24,'bTopLogo','','',3),(25,'bHomeLogo','','',3),(26,'fLoginBackgroundImg','','',3),(27,'fRegisterBackgroudImg','','',3),(28,'fTopLogo','','',3) ON DUPLICATE KEY UPDATE name=VALUES(name);"
        ]
        for sql in config_sqls:
            try:
                cm.cur.execute(sql)
                cm.conn.commit()
            except Exception as e:
                print(f"Error: {e}")
        print("Config 初始数据导入完成")
        cm.conn_close()
    else:
        print('仅支持 MySQL')

sub.add_command(initdb,"initdb")
sub.add_command(initsql,"initsql")
sub.add_command(initconfig,"initconfig")
if __name__ == "__main__":
    sub()
