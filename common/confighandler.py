from configparser import ConfigParser

import yaml

from config.setting import config


class YAMLHandler:
    '''YAML文件操作'''

    def __init__(self, file, encoding='utf-8'):
        self.file = file
        self.encoding = encoding

    def read(self):
        with open(self.file, encoding=self.encoding) as f:
            data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return data

    def write(self, data):
        with open(self.file, mode='w', encoding=self.encoding) as f:
            yaml.dump(data, f, allow_unicode=True)


class iniHandler(ConfigParser):
    '''ini文件操作'''

    def __init__(self, file, encoding='utf-8'):
        super().__init__()
        self.read(file, encoding=encoding)


yaml_data = YAMLHandler(config.yaml_config_path).read()

if __name__ == '__main__':
    print(yaml_data)
