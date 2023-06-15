import json
import traceback

from client.redis_client import RedisClient
from core.example_task import ClientDetail, ExampleTask
from settings import CLIENT_DETAIL_TASK_CHANNEL, TASK_CHANNEL
from utils.log import Logger


class Master:
    """程序入口"""

    def run(self):
        """从队列取任务"""
        while True:
            try:
                task = RedisClient().get_queue(TASK_CHANNEL)
                if task:
                    Logger("info", f"收到任务,当前任务数据:{task}")
                    task_data = json.loads(task)
                    try:
                        ExampleTask().main(task_data)
                    except Exception as e:
                        continue
            except Exception as e:
                Logger("error", f"程序异常:{traceback.format_exc()}")


if __name__ == "__main__":
    Master().run()
