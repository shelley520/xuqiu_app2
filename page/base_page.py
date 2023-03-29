import inspect
import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from page.wrapper import handle_black


class BasePage:

    _params = {}

    _driver:WebDriver = None
    def __init__(self,driver:WebDriver =None):
        self._driver = driver
        self._max_num = 3
        # self._driver.implicitly_wait(10)

    def set_implicitly(self,time):
        self._driver.implicitly_wait(time)

    @handle_black
    def finds(self,locator,value):
        elements:list
        if isinstance(locator,tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator,value)
        return elements

    @handle_black
    def find(self,locator,value):

        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def steps(self,path):
        with open(path,'rb') as f:
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key,value in self._params.items():
            # raw = raw.replace(f'${{{key}}}',value)
            raw = raw.replace('${'+key+'}',value)
        steps = json.loads(raw)
        # print(steps)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action :
                   self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len>0" == action:
                    eles = self.finds(step["by"],step["locator"])
                    return len(eles) > 0


    def screenshot(self,name):
        self._driver.save_screenshot(name)