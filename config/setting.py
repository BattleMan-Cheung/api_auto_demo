import os
import time


class Config:
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # log文件夹路径
    log_dir = os.path.join(root_path, 'log')

    # # log文件夹路径
    # log_path = os.path.join(log_dir, 'log.txt')

    # 配置文件夹路径
    config_dir = os.path.join(root_path, 'config')

    # yaml配置文件路径
    yaml_config_path = os.path.join(config_dir, 'config.yaml')

    # Excel测试数据文件路径
    data_path = os.path.join(root_path, r'data\cases.xlsx')

    # 测试用例脚本文件夹
    cases_path = os.path.join(root_path, 'cases')

    # 测试报告文件夹路径
    report_dir = os.path.join(root_path, 'report')
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)




class DevConfig(Config):
    # 开发环境IP地址
    host = 'http://120.78.128.25:8766/futureloan'


config = DevConfig()

if __name__ == '__main__':
    print(config.time)
