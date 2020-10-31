import logging

from common.confighandler import YAMLHandler, yaml_data
from config.setting import Config


class LoggingHandler(logging.Logger):

    def __init__(self,
                 name='YGG',
                 level='WARNING',
                 file=None,
                 fmt='%(asctime)s  %(filename)s:%(lineno)d  %(name)s - %(levelname)s：%(message)s'):
        super().__init__(name)

        self.setLevel(level)

        fmt = logging.Formatter(fmt)

        if file:
            file_handler = logging.FileHandler(file, encoding='utf8')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


logger = LoggingHandler(name=yaml_data['logger']['name'],
                        level=yaml_data['logger']['level'],
                        fmt=yaml_data['logger']['fmt'],
                        file=Config().log_dir + yaml_data['logger']['file'])


if __name__ == '__main__':
    logger.error('焕友要努力努力再努力呀！你可是个有梦想的人！')
