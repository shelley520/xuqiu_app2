import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):

    # _package = "com.xueqiu.android"
    # _activity = ".view.WelcomeActivityAlias"
    _package = yaml.safe_load(open("../configuration.yaml"))['caps']['package']
    _activity = yaml.safe_load(open("../configuration.yaml"))['caps']['activity']
    def start(self):
        if self._driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "R9AMB1GXZKJ"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            caps["skipServerInstallation"] = True
            caps["skipDeviceInitialization"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        else:
            self._driver.start_activity(self._package,self._activity)
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)

