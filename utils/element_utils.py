# encoding: utf-8
import shutil
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from utils.decorators import *
from utils.configure import *


class Instructions:
    # 定位
    find_bys = {
        'id': (AppiumBy.ID, None),
        'xpath': (AppiumBy.XPATH, None),
        'text': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'),
        'textContains': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("{}")'),
        'textStartsWith': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textStartsWith("{}")'),
        'textMatches': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("{}")'),
        'class': (AppiumBy.CLASS_NAME, None),
        'access': (AppiumBy.ACCESSIBILITY_ID, None),
        'ios_predicate': (AppiumBy.IOS_PREDICATE, None),
    }
    # 键盘代码
    key_code = {
        '0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16, 'A': 29, 'B': 30,
        'C': 31, 'D': 32, 'E': 33, 'F': 34, 'G': 35, 'H': 36, 'I': 37, 'J': 38, 'K': 39, 'L': 40, 'M': 41, 'N': 42,
        'O': 43, 'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48, 'U': 49, 'V': 50, 'W': 51, 'X': 52, 'Y': 53, 'Z': 54,
        'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38, 'k': 39, 'l': 40,
        'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48, 'u': 49, 'v': 50, 'w': 51, 'x': 52,
        'y': 53, 'z': 54, 'META_ALT_LEFT_ON': 16, 'META_ALT_MASK': 50, 'META_ALT_ON': 2, 'META_ALT_RIGHT_ON': 32,
        'META_CAPS_LOCK_ON': 1048576, 'META_CTRL_LEFT_ON':  8192, 'META_CTRL_MASK': 28672, 'META_CTRL_ON': 4096,
        'META_CTRL_RIGHT_ON': 16384, 'META_FUNCTION_ON': 8, 'META_META_LEFT_ON': 131072, 'META_META_MASK': 458752,
        'META_META_ON': 65536, 'META_META_RIGHT_ON': 262144, 'META_NUM_LOCK_ON': 2097152, 'META_SCROLL_LOCK_ON': 4194304,
        'META_SHIFT_LEFT_ON': 64, 'META_SHIFT_MASK': 193, 'META_SHIFT_ON': 1, 'META_SHIFT_RIGHT_ON': 128, 'META_SYM_ON': 4,
        'KEYCODE_APOSTROPHE': 75, 'KEYCODE_AT': 77, 'KEYCODE_BACKSLASH': 73, 'KEYCODE_COMMA': 55, 'KEYCODE_EQUALS': 70,
        'KEYCODE_GRAVE': 68, 'KEYCODE_LEFT_BRACKET': 71, 'KEYCODE_MINUS': 69, 'KEYCODE_PERIOD': 56, 'KEYCODE_PLUS': 81,
        'KEYCODE_POUND': 18, 'KEYCODE_RIGHT_BRACKET': 72, 'KEYCODE_SEMICOLON': 74, 'KEYCODE_SLASH': 76, 'KEYCODE_STAR': 17,
        'KEYCODE_SPACE': 62, 'KEYCODE_TAB': 61, 'KEYCODE_ENTER': 66, 'KEYCODE_ESCAPE': 111, 'KEYCODE_CAPS_LOCK': 115,
        'KEYCODE_CLEAR': 28, 'KEYCODE_PAGE_DOWN': 93, 'KEYCODE_PAGE_UP': 92, 'KEYCODE_SCROLL_LOCK': 116,
        'KEYCODE_MOVE_END': 123, 'KEYCODE_MOVE_HOME': 122, 'KEYCODE_INSERT': 124, 'KEYCODE_SHIFT_LEFT': 59,
        'KEYCODE_SHIFT_RIGHT': 60, 'KEYCODE_F1': 131, 'KEYCODE_F2': 132, 'KEYCODE_F3': 133, 'KEYCODE_F4': 134,
        'KEYCODE_F5': 135, 'KEYCODE_F6': 136, 'KEYCODE_F7': 137, 'KEYCODE_F8': 138, 'KEYCODE_F9': 139,
        'KEYCODE_F10': 140, 'KEYCODE_F11': 141, 'KEYCODE_F12': 142, 'KEYCODE_BACK': 4, 'KEYCODE_CALL': 5,
        'KEYCODE_ENDCALL': 6, 'KEYCODE_CAMERA': 27, 'KEYCODE_FOCUS': 80, 'KEYCODE_VOLUME_UP': 24, 'KEYCODE_VOLUME_DOWN': 25,
        'KEYCODE_VOLUME_MUTE': 164, 'KEYCODE_MENU': 82, 'KEYCODE_HOME': 3, 'KEYCODE_POWER': 26, 'KEYCODE_SEARCH': 84,
        'KEYCODE_NOTIFICATION': 83, 'KEYCODE_NUM': 78, 'KEYCODE_SYM': 63, 'KEYCODE_SETTINGS': 176, 'KEYCODE_DEL': 67,
        'KEYCODE_FORWARD_DEL': 112, 'KEYCODE_NUMPAD_0': 144, 'KEYCODE_NUMPAD_1': 145, 'KEYCODE_NUMPAD_2': 146,
        'KEYCODE_NUMPAD_3': 147, 'KEYCODE_NUMPAD_4': 148, 'KEYCODE_NUMPAD_5': 149, 'KEYCODE_NUMPAD_6': 150,
        'KEYCODE_NUMPAD_7': 151, 'KEYCODE_NUMPAD_8': 152, 'KEYCODE_NUMPAD_9': 153, 'KEYCODE_NUMPAD_ADD': 157,
        'KEYCODE_NUMPAD_COMMA': 159, 'KEYCODE_NUMPAD_DIVIDE': 154, 'KEYCODE_NUMPAD_DOT': 158, 'KEYCODE_NUMPAD_EQUALS': 161,
        'KEYCODE_NUMPAD_LEFT_PAREN': 162, 'KEYCODE_NUMPAD_MULTIPLY': 155, 'KEYCODE_NUMPAD_RIGHT_PAREN': 163,
        'KEYCODE_NUMPAD_SUBTRACT': 156, 'KEYCODE_NUMPAD_ENTER': 160, 'KEYCODE_NUM_LOCK': 143,
        'KEYCODE_MEDIA_FAST_FORWARD': 90, 'KEYCODE_MEDIA_NEXT': 87, 'KEYCODE_MEDIA_PAUSE': 127,
        'KEYCODE_MEDIA_PLAY': 126, 'KEYCODE_MEDIA_PLAY_PAUSE': 85, 'KEYCODE_MEDIA_PREVIOUS': 88,
        'KEYCODE_MEDIA_RECORD': 130, 'KEYCODE_MEDIA_REWIND': 89, 'KEYCODE_MEDIA_STOP': 86,
    }


class AppAction(ReadUtil, Instructions, Environment, RunSetup):

    def __init__(self, case_name):
        """
        初始化
        params:
            case_name: 传入用例名称，例如xxx.yml
        """
        self.driver = self._create_driver(case_name)
        self._case_datas = self.read_yml('case', case_name)
        self._task_case_data = None

    def _init_screenshot_folder(self, case_name):
        """
        创建存放运行时的异常截图
        """
        self._img_save_path = self.join_path('screenshot', case_name)
        try:
            shutil.rmtree(self._img_save_path)
        except:
            logging.warning(f"不存在文件夹 {self._img_save_path}")
        os.mkdir(self._img_save_path)

    def _create_driver(self, case_name):
        """
        创建appium driver
        return: appium driver
        """
        case_name = case_name.split('.')[0]
        self._init_screenshot_folder(case_name)
        desired_caps = {
            "platformName": self.devices_type,
            "appium:deviceName": self.test_env['deviceName'],
            "appium:appPackage": self.test_env[case_name]['appPackage'],
            "appium:appActivity": self.test_env[case_name]['appActivity'],
            "noReset": self.test_env['noReset'],
            "unicodeKeyboard": self.test_env['unicodeKeyboard'],
            "resetKeyboard": self.test_env['resetKeyboard'],
            "newCommandTimeout": self.test_env['newCommandTimeout'],
            "chromedriverExecutable": self.join_path('data', 'chromedriver.exe')
        }
        if self.devices_type == 'Android':
            options = UiAutomator2Options()
        elif self.devices_type == 'IOS':
            options = XCUITestOptions()
        else:
            raise ValueError(f'错误的设备类型{self.devices_type}，请使用Android or IOS')
        options.load_capabilities(desired_caps)
        driver = webdriver.Remote(self.test_env['server'], options=options)
        self.wait = WebDriverWait(driver, 5, 1)
        return driver

    def init_data(self, key):
        """
        获取需要测试的模块元素
        params:
            key: 存储元素的key
        """
        self._task_case_data = self._case_datas[key]

    def find_utils(self, key, find_type='element'):
        """
        元素定位
        例子:
            find_utils('元素')  单元素 非自定义
            find_utils('自定义元素|定位方式')  单元素 自定义
            find_utils('元素', find_type='elements') 多元素查找
        return: element or elements
        """
        if "|" not in key:
            if key not in self._task_case_data:
                raise KeyError(f'用例中不存在下标: {key}')
            else:
                try:
                    element, by = self._task_case_data[key].split('|')
                except:
                    raise ValueError(
                        f'此用例【{key}】写法存在错误, 请按照【用例名称: 元素|定位方式】进行填写, 当前填写情况为: {self._task_case_data[key]}')
        else:
            try:
                element, by = key.split('|')
            except:
                raise ValueError(f'写法存在错误, 请按照【元素|定位方式】格式进行填写, 当前填写情况为: {key}')

        if by not in self.find_bys:
            raise KeyError(f'不存在该定位方式: {by}, 请使用现有定位方式{list(self.find_bys.keys())}')
        else:
            by_type, element_value = self.find_bys[by]
            if element_value is not None:
                element = element_value.format(element)

        if find_type == 'element':
            return self.wait.until(lambda x: x.find_element(by=by_type, value=element))
        elif find_type == 'elements':
            return self.wait.until(lambda x: x.find_elements(by=by_type, value=element))
        else:
            raise ValueError(f'不存在该查找方式: {find_type}, 请使用现有查找方式[element, elements]')

    @retry
    def elem_click(self, element):
        """
        元素点击
        例子:
            elem_click('元素')  非自定义
            elem_click('自定义元素路径|定位方式')  自定义
        """
        self.find_utils(element).click()

    @retry
    def elem_clear(self, element):
        """
        元素文本清除
        例子:
            elem_clear('元素')  非自定义
            elem_clear('自定义元素路径|定位方式')  自定义
        """
        self.find_utils(element).clear()

    @retry
    def elem_send_keys(self, element, content):
        """
        元素输入
        例子:
            elem_send_keys('元素', '输入内容')  非自定义
            elem_send_keys('自定义元素路径|定位方法', '输入内容')  自定义
        """
        self.find_utils(element).send_keys(content)
        
    @retry
    def elem_text(self, element):
        """
        获取元素文本
        """
        return self.find_utils(element).text

    def tap(self, positions, duration):
        """
        用五个手指敲击一个特定的地方，按住特定时间
        params：
            positions:表示的x/y坐标的元组数组要敲击的手指。长度最多可以是五个。
            duration：点击的时间长度，单位为ms
        例子：
            driver.tap([(100,20),(100,60),(100,100)],500)
        """
        self.driver.tap(positions, duration)

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        """
        从一个点滑动到另一个点，持续时间可选。
        params：
            start_x:x坐标开始
            start_y：开始的y坐标
            end_x:x停止的坐标
            end_y：停止的y坐标
            duration：将滑动速度定义为从a点滑动到b点所花费的时间，单位为ms。
        例子：
            driver.swipe(100, 100, 100, 400)
        """
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def save_screenshot(self, img_name):
        """
        app截图保存
        params:
            img_name: 截图名称
        """
        self.driver.save_screenshot(f'{self._img_save_path}/{img_name}.png')

    def shake(self):
        """
        手机摇晃
        """
        self.driver.shake()

    def switch(self, page_type='web'):
        """
        用于h5和app页面的切换
        params:
            page: web or app, 默认为web
        例子:
            切换webview页面 driver.switch() or driver.switch('web')
            切换app页面 driver.switch('app')
        """
        page = 'WEBVIEW_com' if page_type == 'web' else 'NATIVE_APP'
        context_list = self.driver.contexts
        for context in context_list:
            if page in context:
                self.driver.switch_to.context(context)
                logging.info(f'页面已切换到 {context}')
                break

    def press_keycode(self, contents):
        """
        code键码
        params:
            contents: 需要输入的内容，如 '1234567890ASDAW'
        例子:
            driver.press_keycode('1234567890ASDAW')
        """
        contents = str(contents)
        for content in contents:
            self.driver.press_keycode(self.key_code[content])

    def close(self):
        """停止"""
        self.driver.close()


