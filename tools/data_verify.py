import re


class DataVerify:
    """数据校验类"""

    @staticmethod
    def check_ip(ip_addr):
        """
        IP合法性校验
        ip_addr: 要检测的IP地址
        return: 布尔值
        """
        compile_ip = re.compile(
            r"^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|"
            r"2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$"
        )
        return True if compile_ip.match(str(ip_addr)) else False

    @staticmethod
    def check_port(port):
        """
        端口合法性检测
        port: 要检测的端口
        return: 布尔值
        """
        compile_port = re.compile(
            r"^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
        )
        return True if compile_port.match(str(port)) else False
