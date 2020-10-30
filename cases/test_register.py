import json
import unittest

from common.confighandler import YAMLHandler
from common.excelhandler import ExcelHandler
from common.logginghandler import logger
from config.setting import config
from libs import ddt
from middleware.helper import Context
from common.requestshandler import RequestsHandler


@ddt.ddt
class TestRegister(unittest.TestCase):
    # 读取测试数据
    eh = ExcelHandler(config.data_path)
    data = eh.read_data('register')

    def setUp(self) -> None:
        self.request = RequestsHandler()

    def tearDown(self) -> None:
        self.request.close_session()
        pass

    @ddt.data(*data)
    def test_register(self, test_data):
        # 替换注册用手机号
        phone = Context().new_phone
        if '#new_phone#' in test_data['data']:
            test_data['data'] = test_data['data'].replace('#new_phone#', phone)

        res = self.request.visit(method=test_data['method'],
                                 url=config.host + test_data['url'],
                                 json=json.loads(test_data['data']),
                                 headers=json.loads(test_data['headers']))

        try:
            self.assertEqual(test_data['expected'], res['code'])
            self.eh.write_data(config.data_path, 'register', test_data['case_id'] + 1, 8, 'PASS')
        except AssertionError as e:
            logger.error('用例执行失败：{}'.format(e))
            self.eh.write_data(config.data_path, 'register', test_data['case_id'] + 1, 8, 'FAIL')
            raise e
