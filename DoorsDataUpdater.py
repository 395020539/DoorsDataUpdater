# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DoorsDataUpdater.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_UIDoorsDataUpdater(object):
    def setupUi(self, UIDoorsDataUpdater):
        if not UIDoorsDataUpdater.objectName():
            UIDoorsDataUpdater.setObjectName(u"UIDoorsDataUpdater")
        UIDoorsDataUpdater.resize(650, 383)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UIDoorsDataUpdater.sizePolicy().hasHeightForWidth())
        UIDoorsDataUpdater.setSizePolicy(sizePolicy)
        UIDoorsDataUpdater.setMinimumSize(QSize(650, 310))
        UIDoorsDataUpdater.setMaximumSize(QSize(650, 383))
        self.button_start = QPushButton(UIDoorsDataUpdater)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(250, 270, 121, 51))
        self.button_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_start.setMouseTracking(False)
        self.button_start.setStyleSheet(u"font: 15pt \"\u534e\u5149\u7c97\u5706_CNKI\";\n"
"color: rgb(0, 170, 0);")
        self.lineEdit_info = QLineEdit(UIDoorsDataUpdater)
        self.lineEdit_info.setObjectName(u"lineEdit_info")
        self.lineEdit_info.setEnabled(False)
        self.lineEdit_info.setGeometry(QRect(190, 330, 241, 31))
        self.lineEdit_info.setStyleSheet(u"background-color: rgb(248, 255, 239);\n"
"color: rgb(170, 0, 0);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border: none;")
        self.lineEdit_info.setAlignment(Qt.AlignCenter)
        self.lineEdit_info.setReadOnly(False)
        self.lineEdit_ver = QLineEdit(UIDoorsDataUpdater)
        self.lineEdit_ver.setObjectName(u"lineEdit_ver")
        self.lineEdit_ver.setEnabled(False)
        self.lineEdit_ver.setGeometry(QRect(520, 360, 113, 20))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(False)
        self.lineEdit_ver.setFont(font)
        self.lineEdit_ver.setStyleSheet(u"font: 700 6pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border: none;")
        self.lineEdit_ver.setAlignment(Qt.AlignCenter)
        self.button_load = QPushButton(UIDoorsDataUpdater)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setGeometry(QRect(70, 220, 72, 24))
        self.button_load.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        self.button_save = QPushButton(UIDoorsDataUpdater)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(147, 220, 72, 24))
        self.button_save.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        self.pushButton_check = QPushButton(UIDoorsDataUpdater)
        self.pushButton_check.setObjectName(u"pushButton_check")
        self.pushButton_check.setGeometry(QRect(500, 220, 71, 24))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton_check.setFont(font1)
        self.layoutWidget = QWidget(UIDoorsDataUpdater)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(71, 101, 506, 107))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_data_file = QLabel(self.layoutWidget)
        self.label_data_file.setObjectName(u"label_data_file")
        self.label_data_file.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_data_file, 0, 0, 1, 1)

        self.label_project_name = QLabel(self.layoutWidget)
        self.label_project_name.setObjectName(u"label_project_name")
        self.label_project_name.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_project_name, 1, 0, 1, 1)

        self.label_data_suffix = QLabel(self.layoutWidget)
        self.label_data_suffix.setObjectName(u"label_data_suffix")
        self.label_data_suffix.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_data_suffix, 2, 0, 1, 1)

        self.label_username = QLabel(self.layoutWidget)
        self.label_username.setObjectName(u"label_username")

        self.gridLayout.addWidget(self.label_username, 3, 0, 1, 1)

        self.lineEdit_username = QLineEdit(self.layoutWidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.gridLayout.addWidget(self.lineEdit_username, 3, 1, 1, 1)

        self.label_password = QLabel(self.layoutWidget)
        self.label_password.setObjectName(u"label_password")

        self.gridLayout.addWidget(self.label_password, 3, 2, 1, 1)

        self.lineEdit_password = QLineEdit(self.layoutWidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_password, 3, 3, 1, 1)

        self.checkBox_psw = QCheckBox(self.layoutWidget)
        self.checkBox_psw.setObjectName(u"checkBox_psw")

        self.gridLayout.addWidget(self.checkBox_psw, 3, 4, 1, 1)

        self.ButtonBrowseDataFile = QPushButton(self.layoutWidget)
        self.ButtonBrowseDataFile.setObjectName(u"ButtonBrowseDataFile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ButtonBrowseDataFile.sizePolicy().hasHeightForWidth())
        self.ButtonBrowseDataFile.setSizePolicy(sizePolicy1)
        self.ButtonBrowseDataFile.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.ButtonBrowseDataFile, 0, 4, 1, 1)

        self.lineEdit_data_file = QLineEdit(self.layoutWidget)
        self.lineEdit_data_file.setObjectName(u"lineEdit_data_file")
        self.lineEdit_data_file.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_data_file, 0, 1, 1, 3)

        self.lineEdit_project_name = QLineEdit(self.layoutWidget)
        self.lineEdit_project_name.setObjectName(u"lineEdit_project_name")
        self.lineEdit_project_name.setEnabled(True)
        self.lineEdit_project_name.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_project_name, 1, 1, 1, 4)

        self.lineEdit_data_suffix = QLineEdit(self.layoutWidget)
        self.lineEdit_data_suffix.setObjectName(u"lineEdit_data_suffix")
        self.lineEdit_data_suffix.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_data_suffix, 2, 1, 1, 4)


        self.retranslateUi(UIDoorsDataUpdater)

        QMetaObject.connectSlotsByName(UIDoorsDataUpdater)
    # setupUi

    def retranslateUi(self, UIDoorsDataUpdater):
        UIDoorsDataUpdater.setWindowTitle(QCoreApplication.translate("UIDoorsDataUpdater", u"DoorsDataUpdater", None))
#if QT_CONFIG(whatsthis)
        self.button_start.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.button_start.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u5f00\u59cb\u66f4\u65b0", None))
        self.lineEdit_info.setText("")
        self.lineEdit_info.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u7b49\u5f85\u8fd0\u884c... ...", None))
        self.lineEdit_ver.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Ver: 1.0 beta", None))
#if QT_CONFIG(tooltip)
        self.button_load.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u52a0\u8f7d\u914d\u7f6e\u6587\u4ef6</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_load.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Load", None))
#if QT_CONFIG(tooltip)
        self.button_save.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u4fdd\u5b58\u914d\u7f6e\u6587\u4ef6</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_save.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Save", None))
        self.pushButton_check.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Check", None))
#if QT_CONFIG(tooltip)
        self.label_data_file.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#aa0000;\">\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u5165Doors\u7684\u6570\u636e\u6587\u4ef6\uff08.json\uff09</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_data_file.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Update Data", None))
#if QT_CONFIG(tooltip)
        self.label_project_name.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u7684Doors\u9879\u76ee\u540d\u79f0</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_project_name.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Project Name", None))
#if QT_CONFIG(tooltip)
        self.label_data_suffix.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">\u8bf7\u786e\u8ba4Doors Data\u6a21\u5757\u7684\u53d8\u4f53\u540e\u7f00\uff08\u5982\u6709\uff09</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_data_suffix.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Variant Suffix", None))
        self.label_username.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"DoorsUser", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"Doors Username", None))
        self.label_password.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"DoorsPassword", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"Doors Password", None))
        self.checkBox_psw.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Display", None))
#if QT_CONFIG(tooltip)
        self.ButtonBrowseDataFile.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p>\u6d4f\u89c8\u9009\u62e9\u6570\u636e\u6587\u4ef6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonBrowseDataFile.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u6d4f\u89c8", None))
        self.lineEdit_data_file.setText("")
        self.lineEdit_data_file.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u7684\u6570\u636e", None))
        self.lineEdit_project_name.setText("")
        self.lineEdit_project_name.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u7684\u9879\u76ee\u540d", None))
        self.lineEdit_data_suffix.setText("")
        self.lineEdit_data_suffix.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u8bf7\u786e\u8ba4Data\u6a21\u5757\u7684\u53d8\u4f53\u540e\u7f00", None))
    # retranslateUi

