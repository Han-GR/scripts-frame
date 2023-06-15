import datetime

from dateutil import parser


class TimeOperation:
    """时间操作类"""

    @staticmethod
    def time_to_timestamp(time_str):
        """
        时间字符串转换为时间戳
        time_str: 要转换的时间字符串
        return: 时间戳
        """
        datetime_obj = parser.parse(time_str)  # 将时间字符串转换为datetime对象
        timestamp = datetime_obj.timestamp()  # 转换为时间戳
        return int(timestamp)

    @staticmethod
    def timestamp_to_time(timestamp, time_format="%Y-%m-%d %H:%M:%S"):
        """
        时间戳转化为时间格式
        timestamp: 要转换的时间戳
        time_format: 输出的时间格式,默认 %Y-%m-%d %H:%M:%S
        return: 时间字符串
        """
        datetime_obj = datetime.datetime.fromtimestamp(timestamp)  # 将时间戳转换为datetime对象
        time_str = datetime_obj.strftime(time_format)  # 将datetime对象转换为指定格式的字符串
        return time_str
