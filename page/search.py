from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Search(BasePage):
    def search(self,name):
        self._params["name"] = name
        self.steps("../steps/search.yaml")

    def select(self,name):
        self._params["value"] = name
        self.steps("../steps/search.yaml")

    def choose(self,name):
        self._params["name"] = name
        self.steps("../steps/search.yaml")

    def is_choose(self,name):
        self._params["name"] = name
        eles = self.steps("../steps/search.yaml")
        return eles

    def dis_choose(self,name):
        self._params["name"] = name
        self.steps("../steps/search.yaml")
