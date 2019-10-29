import pymysql as pm
conn=pm.connect(host="192.168.206.238",user="xujundong",password="xujundong",db="platform",port=3307)
cursor=conn.cursor()
cursor.execute("select * from aubak")
#获取一行数据
# emp=cursor.fetchall()
# print(emp)
#获取全部数据
all=cursor.fetchall()
print(all)
conn.close()
