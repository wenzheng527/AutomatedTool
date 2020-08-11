# coding=utf-8

'''
使用Python创建数据库
'''

import pymysql
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',charset='utf8')
cursor=conn.cursor()
cursor.execute('SELECT VERSION()')

data = cursor.fetchone()
print('database version:%s' % data)

cursor.execute('show databases')
databases_list = list(cursor.fetchall())
print('数据库了列表为：%s' % str(databases_list))

cursor.execute('DROP DATABASE IF EXISTS TESTDB')
cursor.execute('create database TESTDB')
cursor.execute('use testdb')
# 使用execute()方法执行SQL，如果表存在则将其删除
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

# 使用预处理语句创建表
sql = """CREATE TABLE `employee` (
  `first_name` varchar(255) DEFAULT NULL COMMENT '姓',
   `last_name` varchar(255) DEFAULT NULL COMMENT '名',
   `age` int(11) DEFAULT NULL COMMENT '年龄',
   `sex` varchar(255) DEFAULT NULL COMMENT '性别',
   `income` varchar(255) DEFAULT NULL COMMENT '收入'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)

insert = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Wen', 'Zheng', 20, 'M', 2000)"""
try:
    # 执行SQL语句
    cursor.execute(insert)
    # 提交事务到数据库执行
    conn.commit()  # 事务是访问和更新数据库的一个程序执行单元
except:
    # 如果发生错误则执行回滚操作
    conn.rollback()

update = 'UPDATE employee SET age = age + 5 WHERE sex = "M"'

# 异常处理
try:
    # 执行SQL语句
    cursor.execute(update)
    # 提交到数据库执行
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()

# SQL语句：查询
sql = "SELECT * FROM employee WHERE income > 1000 "
# 异常处理
try:
     # 执行SQL语句
     cursor.execute(sql)
     # 获取所有的记录列表
     results = cursor.fetchall()
     # 遍历列表
     for row in results:
         # 打印列表元素
         print(row)
         # 姓
         first_name = row[0]
         # 名
         last_name = row[1]
         # 年龄
         age = row[2]
         # 性别
         sex = row[3]
         # 收入
         income = row[4]
         # 打印列表元素
         print(first_name, last_name, age, sex, income)
except:
     print('Uable to fetch data!')

delete = 'DELETE FROM employee WHERE age >20'

 # 异常处理
# try:
#     # 执行SQL语句
#     cursor.execute(delete)
#     # 提交到数据库执行
#     conn.commit()
# except:
#     # 发生错误时回滚
#     conn.rollback()

print(conn)
print(cursor)
cursor.close()
conn.close()