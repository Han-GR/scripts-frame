# -*- coding: utf-8 -*-
import argparse
import sys

from core.execute_task import ExecuteTask
from utils.global_except_catch import handle_exception


def run(count):
    """
    项目启动入口
    :param count: 一次性获取的任务数
    :return:
    """
    for _ in range(count):
        ExecuteTask().main()


def parse_args():
    description = "redis任务队列消费"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-c", type=int, help="一次性获取的任务数")
    count = parser.parse_args().c or 1
    return run(count)


if __name__ == '__main__':
    sys.excepthook = handle_exception  # 全局捕获未知异常
    parse_args()
