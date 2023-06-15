# -*- coding: utf-8 -*-

from utils.log import Logger


class ExampleTask:
    """获取客户端详情"""

    def main(self, task_data):
        try:
            pass
        except Exception as e:
            return Logger("error", f"任务失败:{e}\n任务数据:{task_data}")
