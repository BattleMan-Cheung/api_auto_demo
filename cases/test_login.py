import json
import unittest

from common.excelhandler import ExcelHandler
from common.logginghandler import logger
from common.requestshandler import RequestsHandler
from config.setting import config
from libs import ddt
from middleware.helper import replace_tag


@ddt.ddt
class TestLogin(unittest.TestCase):
    # 读取测试数据
    eh = ExcelHandler(config.data_path)
    data = eh.read_data('login')

    def setUp(self) -> None:
        self.request = RequestsHandler()

    def tearDown(self) -> None:
        self.request.close_session()

    @ddt.data(*data)
    def test_login(self, test_data):
        # 替换测试数据中的标签
        test_data = replace_tag(test_data)

        res = self.request.visit(method=test_data['method'],
                                 url=config.host + test_data['url'],
                                 json=json.loads(test_data['data']),
                                 headers=json.loads(test_data['headers']))

        try:
            self.assertEqual(test_data['expected'], res['code'])
            self.eh.write_data(config.data_path, 'login', test_data['case_id']+1, 8, 'PASS')

        except AssertionError as e:
            logger.error('用例执行失败：{}'.format(e))
            self.eh.write_data(config.data_path, 'login', test_data['case_id'] + 1, 8, 'FAILED')
            raise e
