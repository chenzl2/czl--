# encoding: utf-8
import time

import pytest
from utils.element_utils import *

# from Python.app_auto_test.utils.element_utils import AppAction


@pytest.mark.heard
class TestHeard:

    def setup_class(self):

        self.driver = AppAction('heard.yml')

    def setup_method(self, method):
        self.driver.init_data(method.__name__)

    def test_login(self):
        # 啊哈哈哈我修改了这块
        self.driver.elem_click('隐私政策-同意')
        self.driver.elem_click('协议')
        self.driver.elem_click('手机号登录')
        self.driver.elem_send_keys('手机号', '12365498701')
        self.driver.elem_send_keys('密码', '123456')
        self.driver.elem_click('同意阅读协议')
        self.driver.elem_click('登录按钮')
        # time.sleep(5)
        self.driver.elem_click('不再提示是否绑定微信')
        self.driver.elem_click('小学版')
        # self.driver.elem_click('不再提示是否绑定微信')
        # self.driver.elem_click('同意获取WIFI设备位置')
        # self.driver.elem_click('仅使用期间允许')

    def test_create_task(self):

        self.driver.elem_click('我的')
        self.driver.elem_click('创建任务')
        # self.driver.elem_click('new UiSelector().text("创建任务")|text')
        now_time = datetime.datetime.now()
        self.driver.elem_send_keys('任务标题', f'{now_time.month}月{now_time.day}日陈老师布置的任务')
        self.driver.elem_click('任务内容')
        self.driver.elem_click('我的收藏')
        self.driver.elem_click('默认分组')
        self.driver.elem_click('选中第一个专题')
        self.driver.elem_click('确定')
        self.driver.elem_click('再次确认')
        self.driver.elem_click('选择孩子')
        students = self.driver.find_utils('全部孩子', 'elements')
        for elem in students:
            elem.click()
        self.driver.elem_click('点击确定')
        self.driver.elem_click('学习要求导语')
        self.driver.elem_click('发布')
        self.driver.elem_click('返回')
    #
    # def test_care_teacher(self):
    #     self.driver.elem_click('我的')
    #     self.driver.elem_click('我的教师')
    #     self.driver.elem_click('添加关注')
    #     self.driver.elem_click('搜索框')
    #     self.driver.press_keycode('13237508238')
    #     self.driver.elem_click('确认搜索')
    #     self.driver.elem_click('关注')
    #     self.driver.elem_click('孩子关注')
    #     self.driver.elem_click('确定')
    #     self.driver.elem_click('返回')
    #     self.driver.elem_click('再次返回')
    #
    # def test_add_child(self):
    #     self.driver.elem_click('管理')
    #     self.driver.elem_click('家庭管理')
    #     self.driver.elem_click('添加孩子')
    #     self.driver.elem_click('点击头像')
    #     self.driver.elem_click('弹窗中选择从相册选择')
    #     self.driver.elem_click('同意')
    #     self.driver.elem_click('允许')
    #     # self.driver.elem_click('选择图片')
    #     pictures = self.driver.find_utils('选择图片','elements')
    #     pictures[17].click()
    #     self.driver.elem_click('点击完成')
    #     self.driver.elem_send_keys('学生姓名', '小陈')
    #     self.driver.elem_send_keys('所在学校', '金山谷学校')
    #     self.driver.elem_click('所在学段')
    #     self.driver.elem_click('请选择学段')
    #     self.driver.elem_click('所在年级')
    #     self.driver.elem_click('请选择年级')
    #     self.driver.elem_click('所在班级')
    #     self.driver.elem_click('请选择班级')
    #     self.driver.elem_click('保存')
    #     self.driver.elem_click('返回')
    #     self.driver.elem_click('返回')
    #
    # def test_answer_tinglian_task(self):
    #     self.driver.elem_click('首页')
    #     self.driver.elem_click('语文听练')
    #     self.driver.elem_click('取消弹窗')
    #     courses = self.driver.find_utils('一年级','elements')
    #     courses[0].click()
    #     self.driver.elem_click('第一单元')
    #     self.driver.elem_click('识字1天地人')
    #     self.driver.elem_click('基础知识')
    #     self.driver.elem_click('手机听练1')
    #     self.driver.elem_click('手机听练2')
    #
    #     # elements = ['对', '下一题', '对', '下一题', '对', '下一题','对', '下一题', '对', '下一题', '对', '下一题', '对', '下一题', '对', '下一题']
    #     # for element in elements:
    #     #     self.driver.elem_click(element)
    #
    #     for i in range(8):
    #         self.driver.elem_click('对')
    #         self.driver.elem_click('下一题')
    #
    #     self.driver.elem_click('单选题')
    #     self.driver.elem_click('完成')
    #     self.driver.elem_click('查看解析')
    #     self.driver.elem_click('返回')
    #
    # def test_parents_assign_task(self):
    #     self.driver.elem_click('布置任务')
    #     self.driver.elem_click('选择孩子')
    #     all_students = self.driver.find_utils('勾选全部孩子', 'elements')
    #     for elem in all_students:
    #         elem.click()
    #     self.driver.elem_click('确定')
    #     self.driver.elem_send_keys('学习要求导语','孩子们要认真完成任务哦！！！')
    #     self.driver.elem_click('保存')
    #     self.driver.elem_click('返回')
    #     self.driver.elem_click('返回')
    #     self.driver.elem_click('返回')
    #     self.driver.elem_click('最后返回')
    #
    # def test_see_download_errors(self):
    #     self.driver.elem_click('错题巩固')
    #     self.driver.elem_click('下载错题')
    #     self.driver.elem_click('同意获取存储权限')
    #     self.driver.elem_click('允许访问媒体')
    #     self.driver.elem_click('确定下载')
    #     self.driver.elem_click('完成')
    #     self.driver.elem_click('返回')
    #

    def test_homepage_tinglian_task(self):
        self.driver.elem_click('待完成')
        self.driver.elem_click('手机听练')
        self.driver.back()








