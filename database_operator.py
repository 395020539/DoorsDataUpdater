#!/usr/bin/python
# -*- coding: utf-8 -*-


import sqlite3
import time
from configuration_reader import MyPath
from logging_maker import _MyLogger


class DataBaseOperator:
    def __init__(self):
        print("init Object")

    # 连接到数据库
    def connect(self):
        mypath = MyPath()
        db_path = mypath.data_path + "\SysEngDataDB.db"
        print(f"db_path = {db_path}")
        _MyLogger.log("debug", f"db_path = {db_path}")
        conn = None
        attempts = 0
        while attempts < 3:
            try:
                conn = sqlite3.connect(db_path)
                break
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")
                _MyLogger.log("error", f"Error connecting to database: {e}")
                attempts += 1
                time.sleep(1)
        return conn

    # 关闭游标和连接
    def close_connection(self, conn):
        if conn:
            conn.close()

    # 查询路径
    def query_path(self, data_name, module_name):
        conn = self.connect()
        result = ""
        if conn:
            # 创建一个游标对象
            cursor = conn.cursor()
            sql = """select data_path from data_module_info where data_name = '{}' and module_name like '{}'""" \
                .format(data_name, module_name)
            try:
                cursor.execute(sql)
                result = cursor.fetchall()[0][0]
            except Exception as e:
                print(f"Error querying data: {e}")
                _MyLogger.log("error", f"Error querying data: {e}")
        else:
            print("Failed to connect to database.")
            _MyLogger.log("error", "Failed to connect to database.")
        self.close_connection(conn)
        return result


if __name__ == '__main__':
    mydatabase = DataBaseOperator()
    data_path = mydatabase.query_path("Energy_Impact_Reduced", "LSS")
    print(data_path)
