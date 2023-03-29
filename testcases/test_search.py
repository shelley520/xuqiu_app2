import pytest
import yaml
from testcases.test_base import TestBase


class TestMain(TestBase):
    # @pytest.mark.parametrize("name",yaml.safe_load(open("./test_search.yaml",encoding="utf-8")))
    @pytest.mark.parametrize("inputsearch,value,name",[('alibaba','BABA','阿里巴巴')])
    def test_main(self,inputsearch,value,name):
        self.search = self.app.start().main().goto_search()
        self.search.search(inputsearch)
        self.search.select(value)
        self.search.choose(name)
        assert self.search.is_choose(name)
        self.search.dis_choose(name)


    # def teardown(self):
    #     name = '阿里巴巴'
    #     self.search.dis_choose(name)


