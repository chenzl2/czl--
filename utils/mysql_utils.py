from warnings import filterwarnings
import pymysql
import logging
from utils.configure import Environment
from pymysql.cursors import DictCursor

# 忽略 Mysql 告警信息
filterwarnings("ignore", category=pymysql.Warning)


class MysqlDB(Environment):

    def __init__(self, db_name):
        # 建立数据库连接
        self.conn = pymysql.connect(
            host=self.mysql['host'],
            user=self.mysql['user'],
            password=self.mysql['pwd'],
            port=self.mysql['port'],
            db=db_name,
            charset='utf8'
        )

        # 使用 cursor 方法获取操作游标，得到一个可以执行sql语句，并且操作结果为字典返回的游标
        self.cur = self.conn.cursor(cursor=DictCursor)

    def __del__(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

    def query(self, sql, state="all"):
        """
            查询
            :param sql:
            :param state:  all 是默认查询全部
            :return:
            """
        try:
            self.cur.execute(sql)

            if state == "all":
                # 查询全部
                data = self.cur.fetchall()
            else:
                # 查询单条
                data = self.cur.fetchone()
            return data
        except AttributeError as error:
            logging.error(f"操作失败, 失败原因: {error}")
            raise

    def execute(self, sql):
        """
            更新 、 删除、 新增
            :param sql:
            :return:
            """
        try:
            # 使用 execute 操作 sql
            rows = self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
            return rows
        except AttributeError as error:
            logging.error(f"操作失败, 失败原因: {error}")
            # 如果事务异常，则回滚数据
            self.conn.rollback()
            raise


if __name__ == '__main__':
    mysql_util = MysqlDB('new_schema')
    # b = mysql_util.execute("update students set studentname='晓鹏' where id=1")

    # b = mysql_util.execute("delete from students where studentname='晓鹏'")
    b = mysql_util.query("select * from students")
    print(b)
