#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import os
from logging_maker import _MyLogger


class MyConfig:
    def __init__(self):
        mypath = MyPath()
        self.return_code, self.doors_username, self.doors_password, \
            self.doors_project_path, self.data_file, self.data_suffix \
            = self.read_config(mypath.config_path, mypath.app_dir, mypath.data_path)
        self.doors_exe_path = r'C:\Program Files (x86)\ibm\Rational\DOORS\9.5\bin\doors.exe'
        print(f"doors_exe_path = \n{self.doors_exe_path}")
        _MyLogger.log("debug", f"doors_exe_path = {self.doors_exe_path}")


    def read_config(self, config_path, app_dir, data_path):
        return_code = "0"
        doors_username = ""
        doors_password = ""
        doors_project_path = ""
        data_file = ""
        data_suffix = ""
        try:
            with open(config_path, 'r', encoding='utf - 8') as f:
                print(f)
                json_data = json.load(f)
                # print(f"json_data = \n{json_data}")
                doors_username = json_data['doors_username']
                print(f"doors_username = \n{doors_username}")
                _MyLogger.log("debug", f"doors_username = {doors_username}")
                doors_password = json_data['doors_password']
                print(f"doors_password = \n{doors_password}")
                _MyLogger.log("debug", f"doors_password = {doors_password}")
                doors_project_path = "/" + json_data['project_name']
                print(f"doors_project_path = \n{doors_project_path}")
                _MyLogger.log("debug", f"doors_project_path = {doors_project_path}")
                data_suffix = json_data['data_suffix']
                print(f"data_suffix = \n{data_suffix}")
                _MyLogger.log("debug", f"data_suffix = {data_suffix}")
                data_file = json_data['data_file']
                data_file = os.path.join(data_path, data_file)
                print(f"data_file = \n{data_file}")
                _MyLogger.log("debug", f"data_file = {data_file}")
        except Exception as e:
            print("An error occurred:", e)
            _MyLogger.log("error", ("An error occurred:", e))
            return_code = "1"
        finally:
            return return_code, doors_username, doors_password, doors_project_path, data_file, data_suffix

    def check_my_config(self):
        error_flag = 0
        error_message = ""
        e = None
        try:
            with open(self.data_file, 'r', encoding='utf - 8') as f:
                json_data = json.load(f)
        except  Exception as e:
            print("An error occurred:", e)
            _MyLogger.log("error", ("An error occurred:", e))
            error_flag = 1
            error_message = "请检查文件或路径"

        if self.doors_username == "" or not self.doors_username:
            error_flag = 1
            error_message = "无效的用户名"
        elif self.doors_password == "" or not self.doors_password:
            error_flag = 1
            error_message = "无效的密码"
        elif self.doors_project_path == "/" or not self.doors_project_path or self.doors_password == "":
            error_flag = 1
            error_message = "无效的项目名"

        return error_flag, error_message



class MyPath:
    def __init__(self):
        self.app_dir, self.config_path, self.data_path = self.get_current_path()

    def get_current_path(self):
        # 获取可执行文件的路径
        if getattr(sys, 'frozen', False):
            # 如果是打包后的 exe 文件，获取可执行文件的路径
            app_dir = os.path.dirname(sys.executable)
        else:
            # 如果是源代码，获取脚本文件所在的目录
            app_dir = os.path.dirname(os.path.abspath(__file__))
        print("app_dir = ", app_dir)
        config_path = os.path.join(app_dir, 'Config\module_cfg.json')
        print("config_path = ", config_path)
        data_path = os.path.join(app_dir, 'Data')
        print("data_path = ", data_path)
        return app_dir, config_path, data_path


if __name__ == '__main__':
    mypath = MyPath()
    print(mypath.app_dir, mypath.config_path, mypath.data_path)

    myconfig = MyConfig()
    print("doors_username: ", myconfig.doors_username)
    print("doors_password: ", myconfig.doors_password)
    print("doors_project_path: ", myconfig.doors_project_path)
    print("data_file: ", myconfig.data_file)
    print("doors_exe_path: ", myconfig.doors_exe_path)
    print("data_suffix: ", myconfig.data_suffix)


