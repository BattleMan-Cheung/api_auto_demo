import pymysql
from pymysql.cursors import DictCursor

from common.confighandler import yaml_data


class MySQLHandler:

    def __init__(self):
        self.conn = pymysql.connect(host=yaml_data['db']['host'], port=yaml_data['db']['port'],
                                    user=yaml_data['db']['user'], password=yaml_data['db']['pwd'],
                                    database=yaml_data['db']['database'],
                                    charset='utf8', cursorclass=DictCursor)
        self.cursor = self.conn.cursor()

    def query(self, sql, *args, one=True):
        self.cursor.execute(sql, args)
        self.conn.commit()
        if not one:
            return self.cursor.fetchall()
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()
