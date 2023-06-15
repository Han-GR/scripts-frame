import logging
import os
from logging import handlers

from settings import LOG_PATH, LOG_LEVEL
from utils.ding_robot import RobotMessage


class Logger:
    """日志封装,支持钉钉告警(取消注释即可)"""

    # 日志级别关系映射
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }

    def __init__(self, level, msg):
        os.makedirs(LOG_PATH, exist_ok=True)  # 按配置生成log文件夹
        self.fmt = "%(asctime)s - %(levelname)s: %(message)s"
        self.level = level
        self._add_logger("runtime.log")
        self._write_log(msg)
        if self.level == "error":
            # 错误日志额外记录
            self._add_logger("error.log")
            self._write_log(msg)
            # RobotMessage().send_msg(msg)
        elif self.level == "critical":
            self._add_logger("critical.log")
            self._write_log(msg)
            # RobotMessage().send_msg(msg)

    def _add_logger(self, filename):
        self.logger = logging.getLogger(LOG_PATH + filename)
        format_str = logging.Formatter(self.fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations[LOG_LEVEL])  # 设置日志级别
        # 如果没有handlers再添加，否则会重复写入！！！
        if not self.logger.handlers:
            self.th = handlers.TimedRotatingFileHandler(
                filename=LOG_PATH + filename,
                when="D",
                backupCount=5,
                interval=2,
                encoding="utf-8",
            )
            self.th.setFormatter(format_str)  # 设置文件里写入的格式
            self.logger.addHandler(self.th)

    def _write_log(self, msg):
        getattr(self.logger, self.level, "error")(msg)
