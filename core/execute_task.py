# -*- coding: utf-8 -*-
import json
import traceback

from client.redis_client import RedisClient
from core.example_task import ExampleTask
from settings import TASK_CHANNEL
from utils.log import Logger


class ExecuteTask:
    """程序入口"""

    def main(self):
        """将任务发送到待检测队列"""
        try:
            task = RedisClient().get_queue(TASK_CHANNEL)
            if task:
                Logger("info", f"收到任务,当前任务数据:{task}")
                task_data = json.loads(task)
                try:
                    ExampleTask().main(task_data)
                except Exception as e:
                    pass
        except Exception as e:
            Logger("error", f"程序异常:{traceback.format_exc()}")
