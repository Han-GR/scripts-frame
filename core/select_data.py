from client.mysql_client import MysqlClient
from settings import MYSQL_CONFIG


class SelectData:
    """数据查询工具类"""

    @staticmethod
    def select_example():
        """查询示例"""
        sql = """SELECT * FROM table WHERE id=10000"""
        result = MysqlClient(MYSQL_CONFIG).select(sql)
        return result
