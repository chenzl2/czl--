from functools import wraps
import logging
import datetime
import time


def retry(function=None, repeat=3, interval=1, is_retry=True):
    def check(func):
        @wraps(func)
        def wrapped(self, *args, **kwargs):
            logging.info(f'执行方法: {func.__name__}, 参数: {args, kwargs}')
            if is_retry:
                for i in range(1, repeat+1):
                    try:
                        return func(self, *args, **kwargs)
                    except KeyError as k:
                        logging.error(k)
                        self.close()
                    except ValueError as v:
                        logging.error(v)
                        self.close()
                    except Exception as e:
                        logging.warning(f'方法: {func.__name__} 重试 {i} 次')
                        if i == repeat:
                            self.save_screenshot(datetime.datetime.now().strftime('%Y%m%d%H%M'))
                            logging.error(f'三次重试均失败, 测试停止, 异常: {e}')
                            self.close()
                    time.sleep(interval)
            else:
                return func(self, *args, **kwargs)
        return wrapped

    if function is not None:
        return check(function)
    else:
        return check
