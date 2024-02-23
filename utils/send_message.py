import json
import requests
import hmac
import hashlib
import base64
import time
import urllib.parse
from utils.configure import Environment, RunSetup
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendMessage(Environment, RunSetup):

    def __init__(self, content):
        self._content = content

    def _send_dingding(self):
        # 详细配置 https://blog.csdn.net/codename_cys/article/details/107850101
        webhook = self.dingding['webhook']  # 钉钉机器人webhook
        timestamp = str(round(time.time() * 1000))
        secret = self.dingding['secret']  # 钉钉机器人秘钥
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = webhook+'&timestamp='+timestamp+'&sign='+sign
        headers = {'Content-Type': 'application/json'}
        data = {
            "msgtype": "actionCard",
            "actionCard": {
                "title": '自动化测试',
                "text": self._content.replace('\n', '\n\n'),
                "btnOrientation": "0",
                "singleTitle": "点击查看报告",
                "singleURL": self.report_url  # 报告地址
            },
            "isAtAll": True}  # 这是判断是否要全员艾特
        requests.post(url, data=json.dumps(data), headers=headers)

    def _send_email(self):
        file_content = open(self.report_path, "rb").read()

        msg = MIMEMultipart('mixed')
        msg["From"] = self.email['user']
        msg["To"] = Header(','.join(self.email['to_user']), 'utf-8')
        msg["subject"] = Header(self.email['subject'], 'utf-8')

        msg_text = MIMEText(self._content, _subtype='plain', _charset="utf8")
        msg.attach(msg_text)
        file_msg = MIMEApplication(file_content)
        file_msg.add_header('content-disposition', 'attachment', filename=self.email['file_name'])
        msg.attach(file_msg)
        # 邮箱服务器地址和端口
        smtp_s = smtplib.SMTP_SSL(host=self.email['host'], port=self.email['port'])
        # 发送方邮箱账号和授权码
        smtp_s.login(user=self.email['user'], password=self.email['pwd'])
        smtp_s.sendmail(self.email['user'], self.email['to_user'], msg.as_string())

    def _send_wechat(self):
        content = self._content + f'\n  测试报告，点击查看>>[测试报告入口]({self.report_url})'
        # 企业微信机器人 webhook 地址和密钥
        webhook_url = self.wechat['webhook']
        # 构建请求头部
        headers = {'Content-Type': 'application/json'}
        # 构建请求数据
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }
        requests.post(webhook_url, headers=headers, data=json.dumps(data)).json()

    def send(self):
        self._send_dingding() if self.dingding_send else None
        self._send_email() if self.email_send else None
        self._send_wechat() if self.wechat_send else None


if __name__ == '__main__':
    SendMessage('test').send()