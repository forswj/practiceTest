# coding=utf-8
import pymysql
import kafka


class SqlOperation(object):
    # Mysqldb 提供了connect 方法来与数据库的连接，
    def __init__(self, host='10.0.0.0', port=36000, dbName='auto', user='username01', password='word001'):
        self.db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=dbName, charset='utf8')
        # 创建一个游标对象，通过游标对象来进行数据的增删改查。
        self.cursor = self.db.cursor()

    # 调用该对象的close() 方法来关闭数据库。
    def __del__(self):
        self.db.close()

    # 对数据进行相关增删改查，建议做查询时，使用该方法
    def execute(self, sql):
        self.cursor.execute(sql)

    # 获取全部查询结果
    def fetchall(self):
        return self.cursor.fetchall()

    # 获取多行查询结果
    def fetchmany(self, size):
        return self.cursor.fetchmany(size)

    # 获取查询结果一行数据
    def fetchone(self):
        return self.cursor.fetchone()

    # 对于需要提交commit操作使用该方法：eg：插入，修改，删除
    def execute_commit(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            print("插入表失败，失败原因为：", e)
            # 发生错误时回滚
            self.db.rollback()

    def commit(self):
        self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.close()