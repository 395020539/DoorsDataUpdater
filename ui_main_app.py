#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QFileDialog,QMessageBox, QMenu,QTextBrowser,QVBoxLayout
from PySide6.QtCore import Qt, QObject, Signal, QThread, Slot,QRect
from PySide6.QtGui import QAction
from configuration_reader import MyConfig, MyPath
import json



from DoorsDataUpdater import Ui_UIDoorsDataUpdater

class MyWindow(QMainWindow, Ui_UIDoorsDataUpdater):

    def __init__(self):
        super().__init__()

        self.task = None
        self.setupUi(self)
        self.retranslateUi(self)

        self.button_load.clicked.connect(self.load_cfg)
        self.button_save.clicked.connect(self.save_cfg)
        self.button_start.clicked.connect(self.run_updater)
        self.ButtonBrowseDataFile.clicked.connect(self.select_data_file)



    def load_cfg(self):
        print("load cfg")
        myconfig = MyConfig()
        self.project_name = myconfig.doors_project_path[1:]
        print(f"project_name is [{self.project_name}]")
        self.data_suffix = myconfig.data_suffix
        print(f"data_suffix is [{self.data_suffix}]")
        self.data_file = myconfig.data_file
        print(f"data_file is [{self.data_file}]")

        self.lineEdit_project_name.setText(self.project_name)
        self.lineEdit_data_suffix.setText(self.data_suffix)
        self.lineEdit_data_file.setText(self.data_file)


    def save_cfg(self):
        mypath = MyPath()
        print("save cfg")

        try:
            with open(mypath.config_path, 'r', encoding='utf - 8') as f:
                json_data = json.load(f)
                json_data["project_name"] = self.project_name
                json_data["data_suffix"] = self.data_suffix
                json_data["data_file"] = self.data_file
        except Exception as e:
            print("An error occurred:", e)
        try:
            with open(mypath.config_path, 'w') as f:
                f.write(json.dumps(json_data,indent=4))
        except Exception as e:
            print("An error occurred:", e)


    def run_updater(self):
        print("run updater")

    def select_data_file(self):
        print("select_data_file")
        self.data_file, _ = QFileDialog.getOpenFileName(self, "Select Data", ".", "Data(*.json);;所有文件(*)")
        if self.data_file:
            self.lineEdit_data_file.setText(self.data_file)





if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()