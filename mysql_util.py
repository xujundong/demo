#coding:utf-8
import pymysql

class MysqlHelper(object):
    config = {
        "host":"192.168.206.238",
        "user":"xujundong",
        "password":"xujundong",
        "db":"platform",
        "charset":"utf8",
        "port":3307
    }

    def __init__(self):
        self.connection=None
        self.cursor=None

    #查询一条
    def getOne(self,sql):
        try:
            self.connection=pymysql.connect(**MysqlHelper.config)
            self.cursor=self.connection.cursor()
            self.cursor.execute(sql)
            emp=self.cursor.fetchone()
            return emp
        except Exception as ex:
            print(ex)
        finally:
            self.close()

    #查询全部
    def getAll(self,sql):
        try:
            self.connection=pymysql.connect(**MysqlHelper.config)
            self.cursor=self.connection.cursor()
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.close()

    #增删改
    def exeDSZ(self,sql,*args):
        try:
            self.connection=pymysql.connect(**MysqlHelper.config)
            self.cursor=self.connection.cursor()    #获取游标
            self.cursor.execute(sql,args)           #执行sql返回 sql语句执行之后影响的行数
            new_id=self.connection.insert_id()      ## 返回系统刚刚自动生成的id
            self.connection.commit()                #执行事务
            return new_id
        except Exception as ex:
            self.connection.rollback()              #回滚事务
            print(ex)
        finally:
            self.close()

    #关闭数据库，用于 finally
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()



if __name__ == '__main__':
    helper = MysqlHelper()
    #查询一条
    # print(helper.getOne("select * from aubak"))
    #查询全部，打印
    # all=helper.getAll("select * from aubak")
    # for i in range(len(all)):
    #     print(all[i])
    #插入数据
    helper.exeDSZ("insert into aubak values(%s,%s,%s,%s)","5000","测试","test","6000")
