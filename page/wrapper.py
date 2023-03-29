import logging
import allure
from selenium.webdriver.common.by import By

def handle_black(func):
    logging.basicConfig(level=logging.DEBUG)
    def wrapper(*args,**kwargs):
        from page.base_page import BasePage
        _black_list = [
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/tv_agree']"),
            (By.XPATH, "//*[@text='取消']"),
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/tv_banner']")
        ]
        _error_num = 0
        _max_num = 3
        instance: BasePage = args[0]
        try:
            logging.info("run "+func.__name__+"\n args: \n"+repr(args)+"\n"+repr(kwargs))
            element = func(*args, **kwargs)
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
            instance.screenshot("tmp.png")
            with open("tmp.png","rb") as f:
                content = f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            logging.error("element not found,handle blacklist ")
            instance._driver.implicitly_wait(3)
            if _error_num > _max_num:
                raise e
            _error_num +=1
            print(_error_num)
            # 处理黑名单里面的弹框
            for black in _black_list:
                elements = instance._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    # break
                    return wrapper(*args,**kwargs)
            raise e
    return wrapper