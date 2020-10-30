import os
import unittest
import time

from config.setting import config
from libs.HTMLTestRunnerNew import HTMLTestRunner

loader = unittest.TestLoader()

suite = loader.discover(config.cases_path)

# 测试报告文件路径
time = int(time.time())
report_path = os.path.join(config.report_dir, 'API_AUTO_REPORT_{}.html'.format(time))

with open(report_path, mode='wb') as f:
    runner = HTMLTestRunner(f)
    runner.run(suite)
