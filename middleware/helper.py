from random import randint
from jsonpath import jsonpath
from common.confighandler import yaml_data
from common.dbhandler import MySQLHandler
from common.requestshandler import RequestsHandler
from config.setting import config


def login():
    data = {"mobile_phone": yaml_data['test_account']['user'], 'pwd': yaml_data['test_account']['pwd']}
    headers = {"X-lemonban-Media-Type": "lemonban.v2"}

    res = RequestsHandler().visit(method='POST',
                                  url=config.host + '/member/login',
                                  json=data,
                                  headers=headers)
    return res


class Context:
    res = login()

    @property
    def new_phone(self):
        """返回随机生成且未被注册的手机号"""
        numb = '155'
        cursor = MySQLHandler()
        while True:
            for i in range(8):
                numb += str(randint(0, 9))
            res = cursor.query('select * from member where mobile_phone=%s;', numb)
            if not res:
                break
        cursor.close()
        return numb

    @property
    def exist_phone(self):
        """返回已被注册的手机号"""
        cursor = MySQLHandler()
        res = cursor.query('select mobile_phone from member order by reg_time desc limit 1;')
        cursor.close()
        return res['mobile_phone']

    @property
    def token(self):
        """返回测试账号登录并且拼接后的token值"""
        token_type = jsonpath(self.res, '$..token_type')[0]
        token_value = jsonpath(self.res, '$..token')[0]
        return ' '.join([token_type, token_value])


if __name__ == '__main__':
    context = Context()
    print(context.token)
    print(context.exist_phone)
    print(context.new_phone)

