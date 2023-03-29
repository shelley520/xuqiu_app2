import time
from selenium.webdriver.common.by import By

from page.base_page import BasePage
# from page.market import Market
from page.search import Search


class Main(BasePage):

    def goto_search(self):
        # time.sleep(10)
        # self.find(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='自选']").click()
        # self.steps("../steps/main.yaml")
        return Search(self._driver)