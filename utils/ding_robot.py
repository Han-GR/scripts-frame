import base64
import hashlib
import hmac
import time
import urllib.parse

from settings import ROBOT_SECRET, ROBOT_TOKEN
from utils.net_request import NetRequest


class RobotMessage:
    """钉钉机器人发送消息警报"""

    def __init__(self):
        self.secret = ROBOT_SECRET
        self.token = ROBOT_TOKEN

    def get_sign(self):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode("utf-8")
        string_to_sign = "{}\n{}".format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode("utf-8")
        hmac_code = hmac.new(
            secret_enc, string_to_sign_enc, digestmod=hashlib.sha256
        ).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return timestamp, sign

    def send_msg(self, text):
        timestamp, sign = self.get_sign()
        headers = {"Content-Type": "application/json;charset=utf-8"}
        robot_url = f"https://oapi.dingtalk.com/robot/send?access_token={self.token}&timestamp={timestamp}&sign={sign}"
        json_text = {"msgtype": "text", "text": {"content": text}}
        NetRequest().post(robot_url, headers=headers, json=json_text)
