import sys
import traceback

from utils.log import Logger


def handle_exception(exc_type, exc_value, exc_traceback):
    """全局异常捕获"""
    if issubclass(exc_type, KeyboardInterrupt):
        return sys.__excepthook__(exc_type, exc_value, exc_traceback)

    err_detail = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    Logger("critical", f"意外的错误:{err_detail}")
    sys.__excepthook__(exc_type, exc_value, exc_traceback)
