import traceback

import pymysql
from dbutils.pooled_db import PooledDB

from pymysql import OperationalError
from pymysql.cursors import DictCursor

from utils.log import Logger


class MysqlClient:
    """mysql客户端连接"""

    def __init__(self, config):
        self.config = config
        self.retry_times = 3
        self.conn, self.cursor = self._get_mysql_conn()

    def _get_mysql_conn(self):
        """获取mysql连接"""
        for _ in range(self.retry_times):
            try:
                pool = PooledDB(**self.config, creator=pymysql)
                conn = pool.connection()
                cursor = conn.cursor(DictCursor)
            except OperationalError:
                if _ < self.retry_times - 1:
                    continue
                raise Exception(traceback.format_exc())
            else:
                return conn, cursor

    def select(self, sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            Logger("error", f"sql查询语句执行失败:{traceback.format_exc()}")
        finally:
            self.cursor.close()
            self.conn.close()
