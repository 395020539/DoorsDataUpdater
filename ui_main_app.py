#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QFileDialog, \
    QMessageBox, QMenu, QTextBrowser, QVBoxLayout
from PySide6.QtCore import Qt, QObject, Signal, QThread, Slot, QRect
from PySide6.QtGui import QAction
from configuration_reader import MyConfig, MyPath
import json
import time


from DoorsDataUpdater import Ui_UIDoorsDataUpdater


class MyWindow(QMainWindow, Ui_UIDoorsDataUpdater):

    def __init__(self):
        super().__init__()

        self.task = None
        self.setupUi(self)
        self.retranslateUi(self)

        # 创建 QThread 对象
        self.worker = MyTask()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()

        # 连接任务的 started 信号到槽函数，禁用按钮
        self.worker.started.connect(self.on_task_started)

        # 连接任务的 finished 信号到槽函数，恢复按钮
        self.worker.finished.connect(self.on_task_finished)

        self.button_start.clicked.connect(self.worker.run)
        self.button_load.clicked.connect(self.load_cfg)
        self.button_save.clicked.connect(self.save_cfg)
        self.ButtonBrowseDataFile.clicked.connect(self.select_data_file)
        self.pushButton_check.clicked.connect(self.check_config)
        self.checkBox_psw.stateChanged.connect(self.password_display)

        # 创建菜单栏
        self.menu_bar = self.menuBar()
        menubar = self.menuBar()
        # 创建“文件”菜单
        file_menu = menubar.addMenu('文件')

        # 创建“退出”菜单项
        exit_action = QAction('退出', self)
        exit_action.triggered.connect(self.close)  # 关联退出菜单项的单击事件
        file_menu.addAction(exit_action)

        # 创建“帮助”菜单
        self.help_menu = self.menu_bar.addMenu("帮助")
        # 创建“关于”菜单项
        about_action = QAction('关于', self)
        about_action.triggered.connect(self.show_about_dialog)  # 关联关于菜单项的单击事件
        self.help_menu.addAction(about_action)

    def show_about_dialog(self):
        # 创建应用程序说明框
        about_dialog = QMessageBox()
        about_dialog.setIcon(QMessageBox.Information)
        about_dialog.setText('Doors Data Update Tool')
        about_dialog.setWindowTitle('关于')
        about_dialog.setStyleSheet("QMessageBox{min-width: 5000px;}")

        # 添加软件说明文本和网页链接
        about_dialog.setInformativeText(
            "如果您有任何问题或建议，请发送电子邮件至"
            '<a href="mailto:zhengli.yang@boschhuayu-steering.com">zhengli.yang@boschhuayu-steering.com</a>'
            "本工具详细说明请查阅"
            '<a href="https://www.baidu.com/">Baidu</a>'
        )

        about_dialog.setDetailedText('更新历史:\n'
                                     'V1.0 Beta 04/13/2023')
        about_dialog.setTextFormat(Qt.RichText)
        about_dialog.setTextInteractionFlags(Qt.TextBrowserInteraction)

        # 在网页链接上添加链接打开功能
        for text_browser in about_dialog.findChildren(QTextBrowser):
            text_browser.setOpenExternalLinks(True)

        about_dialog.exec()

    def load_cfg(self):
        print("load cfg")
        myconfig = MyConfig()
        self.project_name = myconfig.doors_project_path[1:]
        print(f"project_name is [{self.project_name}]")
        self.data_suffix = myconfig.data_suffix
        print(f"data_suffix is [{self.data_suffix}]")
        self.data_file = myconfig.data_file
        print(f"data_file is [{self.data_file}]")
        self.doors_username = myconfig.doors_username
        print(f"doors_username is [{self.doors_username}]")
        self.doors_password = myconfig.doors_password
        print(f"doors_password is [{self.doors_password}]")

        self.lineEdit_project_name.setText(self.project_name)
        self.lineEdit_data_suffix.setText(self.data_suffix)
        self.lineEdit_data_file.setText(self.data_file)
        self.lineEdit_project_name.setText(self.project_name)
        self.lineEdit_username.setText(self.doors_username)
        self.lineEdit_password.setText(self.doors_password)



    def save_cfg(self):
        mypath = MyPath()
        print("save cfg")
        self.project_name = self.lineEdit_project_name.text()
        self.data_suffix = self.lineEdit_data_suffix.text()
        self.data_file = self.lineEdit_data_file.text()
        self.doors_username = self.lineEdit_username.text()
        self.doors_password = self.lineEdit_password.text()

        try:
            with open(mypath.config_path, 'r', encoding='utf - 8') as f:
                json_data = json.load(f)
                json_data["project_name"] = self.project_name
                json_data["data_suffix"] = self.data_suffix
                json_data["doors_username"] = self.doors_username
                json_data["doors_password"] = self.doors_password
                json_data["data_file"] = self.data_file
        except Exception as e:
            print("An error occurred:", e)
        try:
            with open(mypath.config_path, 'w') as f:
                f.write(json.dumps(json_data, indent=4))
        except Exception as e:
            print("An error occurred:", e)

        QMessageBox.information(self, "提示", "已保存！")

    def run_updater(self):
        print("run updater")

    def select_data_file(self):
        print("select_data_file")
        self.data_file, _ = QFileDialog.getOpenFileName(self, "Select Data", ".", "Data(*.json);;所有文件(*)")
        if self.data_file:
            self.lineEdit_data_file.setText(self.data_file)

    def on_task_started(self):
        self.button_start.setStyleSheet("background-color: grey;border-radius: 10px;color: white")
        # 禁用按钮
        self.lineEdit_info.setText("正在运行中, 请耐心等待...请勿关闭程序")
        self.button_load.setDisabled(True)
        self.button_save.setDisabled(True)
        self.button_start.setDisabled(True)
        self.ButtonBrowseDataFile.setDisabled(True)
        self.pushButton_check.setDisabled(True)
        self.checkBox_psw.setDisabled(True)

        self.lineEdit_project_name.setDisabled(True)
        self.lineEdit_data_suffix.setDisabled(True)
        self.lineEdit_data_file.setDisabled(True)
        self.lineEdit_username.setDisabled(True)
        self.lineEdit_password.setDisabled(True)

        self.button_start.setText("正在运行")


    def on_task_finished(self):
        self.lineEdit_info.setText("运行结束.")
        QMessageBox.information(self, "提示", "更新结束！")
        self.button_start.setStyleSheet(u"QPushButton {\n"
                                        "    background-color: #4CAF50;\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #3E8E41;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #2E6739;\n"
                                        "}")

        # 恢复按钮
        self.button_load.setEnabled(True)
        self.button_save.setEnabled(True)
        self.button_start.setEnabled(True)
        self.ButtonBrowseDataFile.setEnabled(True)
        self.pushButton_check.setEnabled(True)
        self.checkBox_psw.setEnabled(True)

        self.lineEdit_project_name.setEnabled(True)
        self.lineEdit_data_suffix.setEnabled(True)
        self.lineEdit_data_file.setEnabled(True)
        self.lineEdit_username.setEnabled(True)
        self.lineEdit_password.setEnabled(True)

        self.button_start.setText("开始更新")

        # # 任务执行完毕后，清理并退出线程
        # self.worker.deleteLater()
        # self.thread.quit()
        # self.thread.wait()


    def password_display(self):
        if self.checkBox_psw.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def check_config(self):

        myconfig = MyConfig()
        error_flag, error_message = myconfig.check_my_config()

        if error_flag == 0:
            QMessageBox.information(self, "提示", "检查通过！")
        else:
            QMessageBox.information(self, "提示", error_message)



class MyTask(QObject):
    started = Signal()
    finished = Signal()

    def run(self):
        from dxl_command_sender import MyDxlCommand, DxlSender
        # 发出 started 信号以通知 UI 线程
        self.started.emit()

        t_start = time.perf_counter()
        # 在这里执行你的任务代码
        # time.sleep(5)
        # t_start = time.perf_counter()

        mydxl = MyDxlCommand()
        mysender = DxlSender(mydxl.list_dxl_command)
        mysender.send_dxl_commands()
        # print("运行中")
        # time.sleep(5)
        # print("运行结束")

        # 任务完成后发出 finished 信号
        self.finished.emit()




if __name__ == '__main__':
    app = QApplication([])
    app.setStyle("Fusion")
    window = MyWindow()
    window.show()
    app.exec()
