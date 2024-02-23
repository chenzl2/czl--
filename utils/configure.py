# encoding: utf-8
import os
import yaml
import configparser


class ReadUtil:

    PATH = os.path.dirname(os.path.dirname(__file__))

    def read_yml(self, *args):
        file_path = self.join_path(*args)
        with open(file_path) as f:
            return yaml.safe_load(f)

    def read_ini(self, *args):
        file_path = self.join_path(*args)
        config = configparser.ConfigParser()
        config.read(file_path)
        return config

    def join_path(self, *args):
        return os.path.join(self.PATH, *args)


_read_util = ReadUtil()
_pytest = _read_util.read_ini('pytest.ini')
_config = _read_util.read_yml('config.yml')


class RunSetup:
    """获取pytest.ini配置值"""
    devices_type = _pytest.get('runSetup', 'devices_type')
    email_send = int(_pytest.get('runSetup', 'email_send'))
    dingding_send = int(_pytest.get('runSetup', 'dingding_send'))
    wechat_send = int(_pytest.get('runSetup', 'wechat_send'))


class Environment:
    """获取config.yml配置值"""
    email = _config['EmailConfig']
    dingding = _config['DingdingConfig']
    wechat = _config['WeChatConfig']
    report_url = _config['ReportUrl']
    mysql = _config['MysqlConfig']
    test_env = _config['Environment']
    report_template = _config['ReportTemplate']
    report_path = _read_util.join_path(email['report_path'])
