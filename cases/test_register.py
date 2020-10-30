import json
import unittest

from common.excelhandler import ExcelHandler
from common.logginghandler import logger
from config.setting import config
from libs import ddt
from middleware.helper import replace_tag
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

    @ddt.data(*data)
    def test_register(self, test_data):

        # 替换测试数据中的标签
        test_data = replace_tag(test_data)
        # 发生请求
        res = self.request.visit(method=test_data['method'],
                                 url=config.host + test_data['url'],
                                 json=json.loads(test_data['data']),
                                 headers=json.loads(test_data['headers']))

        try:
            # 断言code业务码
            self.assertEqual(test_data['expected'], res['code'])
            # 用例执行结果回写至Excel
            self.eh.write_data(config.data_path, 'register', test_data['case_id'] + 1, 8, 'PASS')
        except AssertionError as e:
            # 日志记录
            logger.error('用例执行失败：{}'.format(e))
            # 用例执行结果回写至Excel
            self.eh.write_data(config.data_path, 'register', test_data['case_id'] + 1, 8, 'FAILED')
            raise e
