# -*-coding:utf-8-*-
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","lhuibin","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute() 方法执行 SQL，如果表存在则删除
#cursor.execute("DROP TABLE IF EXISTS TEST")
 
# 使用预处理语句创建表
'''
sql = """CREATE TABLE TEST (
         Coin_Name  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         lhuibin INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
 
cursor.execute(sql)
'''
# SQL 插入语句
#sql = """INSERT INTO TEST(Coin_Name,
#         LAST_NAME, lhuibin, SEX, INCOME)
#         VALUES ('Mac', 'Mohan', 20, 'M', 21000)"""
# SQL 更新语句
#sql = "UPDATE TEST SET lhuibin = lhuibin + 1 WHERE SEX = '%c'" % ('M')
	# SQL 查询语句
	sql = "SELECT * FROM COIN \
	       WHERE Coin_Name = '%s'" % Coin_Name
	try:
	   # 执行SQL语句
	   cursor.execute(sql)
	   # 获取所有记录列表
	   results = cursor.fetchall()
	   for row in results:
	      fname = row[0]
	      lname = row[1]
	      age = row[2]
	      sex = row[3]
	      income = row[4]
	       # 打印结果
	      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
	             (fname, lname, age, sex, income ))
	except:
	   print ("Error: unable to fetch data")
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

# 关闭数据库连接
db.close()