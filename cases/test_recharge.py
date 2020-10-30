import unittest

from common.excelhandler import ExcelHandler
from common.requestshandler import RequestsHandler
from config.setting import config
from libs import ddt
from middleware.helper import replace_tag


@ddt.ddt
class TestRecharge(unittest.TestCase):

    eh = ExcelHandler(config.data_path)
    data = eh.read_data('recharge')

    def setUp(self) -> None:
        self.request = RequestsHandler()

    def tearDown(self) -> None:
        self.request.close_session()

    @ddt.data(*data)
    def test_recharge(self, test_data):

        test_data = replace_tag(test_data)

        print(test_data)

