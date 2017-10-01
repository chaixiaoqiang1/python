#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "my_tp5")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 创建数据表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""


# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('34242', '2342342', 20, 'M', 2000)"""

try:
    # 执行sql语句 增删改查都用同一方法（增删改增加事务机制）
    rs = cursor.execute(sql)
    # print(rs)
    # 提交到数据库执行
    db.commit()
except:  # 如果发生错误则回滚
    db.rollback()
