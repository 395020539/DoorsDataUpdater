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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_UIDoorsDataUpdater(object):
    def setupUi(self, UIDoorsDataUpdater):
        if not UIDoorsDataUpdater.objectName():
            UIDoorsDataUpdater.setObjectName(u"UIDoorsDataUpdater")
        UIDoorsDataUpdater.resize(650, 310)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UIDoorsDataUpdater.sizePolicy().hasHeightForWidth())
        UIDoorsDataUpdater.setSizePolicy(sizePolicy)
        UIDoorsDataUpdater.setMinimumSize(QSize(650, 310))
        UIDoorsDataUpdater.setMaximumSize(QSize(650, 310))
        self.button_start = QPushButton(UIDoorsDataUpdater)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(250, 190, 121, 51))
        self.button_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_start.setMouseTracking(False)
        self.button_start.setStyleSheet(u"font: 15pt \"\u521b\u827a\u7e41\u7c97\u5706\";\n"
"color: rgb(0, 170, 0);")
        self.lineEdit_info = QLineEdit(UIDoorsDataUpdater)
        self.lineEdit_info.setObjectName(u"lineEdit_info")
        self.lineEdit_info.setEnabled(False)
        self.lineEdit_info.setGeometry(QRect(190, 250, 241, 31))
        self.lineEdit_info.setStyleSheet(u"background-color: rgb(248, 255, 239);\n"
"color: rgb(170, 0, 0);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border: none;")
        self.lineEdit_info.setAlignment(Qt.AlignCenter)
        self.lineEdit_info.setReadOnly(False)
        self.lineEdit_ver = QLineEdit(UIDoorsDataUpdater)
        self.lineEdit_ver.setObjectName(u"lineEdit_ver")
        self.lineEdit_ver.setEnabled(False)
        self.lineEdit_ver.setGeometry(QRect(520, 280, 113, 20))
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
        self.button_load.setGeometry(QRect(70, 60, 75, 24))
        self.button_load.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        self.ButtonBrowseDataFile = QPushButton(UIDoorsDataUpdater)
        self.ButtonBrowseDataFile.setObjectName(u"ButtonBrowseDataFile")
        self.ButtonBrowseDataFile.setGeometry(QRect(520, 100, 61, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ButtonBrowseDataFile.sizePolicy().hasHeightForWidth())
        self.ButtonBrowseDataFile.setSizePolicy(sizePolicy1)
        self.ButtonBrowseDataFile.setAutoFillBackground(False)
        self.button_save = QPushButton(UIDoorsDataUpdater)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(170, 60, 75, 24))
        self.button_save.setStyleSheet(u"font: 700 9pt \"Microsoft YaHei UI\";")
        self.layoutWidget = QWidget(UIDoorsDataUpdater)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 100, 441, 74))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_data_file = QLabel(self.layoutWidget)
        self.label_data_file.setObjectName(u"label_data_file")
        self.label_data_file.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_data_file, 0, 0, 1, 1)

        self.lineEdit_data_file = QLineEdit(self.layoutWidget)
        self.lineEdit_data_file.setObjectName(u"lineEdit_data_file")
        self.lineEdit_data_file.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_data_file, 0, 1, 1, 1)

        self.label_project_name = QLabel(self.layoutWidget)
        self.label_project_name.setObjectName(u"label_project_name")
        self.label_project_name.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_project_name, 1, 0, 1, 1)

        self.lineEdit_project_name = QLineEdit(self.layoutWidget)
        self.lineEdit_project_name.setObjectName(u"lineEdit_project_name")
        self.lineEdit_project_name.setEnabled(True)
        self.lineEdit_project_name.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_project_name, 1, 1, 1, 1)

        self.label_data_suffix = QLabel(self.layoutWidget)
        self.label_data_suffix.setObjectName(u"label_data_suffix")
        self.label_data_suffix.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_data_suffix, 2, 0, 1, 1)

        self.lineEdit_data_suffix = QLineEdit(self.layoutWidget)
        self.lineEdit_data_suffix.setObjectName(u"lineEdit_data_suffix")
        self.lineEdit_data_suffix.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit_data_suffix, 2, 1, 1, 1)

        self.line = QFrame(UIDoorsDataUpdater)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(40, 170, 561, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(UIDoorsDataUpdater)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(40, 40, 561, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(UIDoorsDataUpdater)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(30, 50, 20, 131))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(UIDoorsDataUpdater)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(590, 50, 20, 131))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

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
        self.lineEdit_ver.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Ver: 1.1 beta", None))
#if QT_CONFIG(tooltip)
        self.button_load.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u52a0\u8f7d\u914d\u7f6e\u6587\u4ef6</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_load.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Load", None))
#if QT_CONFIG(tooltip)
        self.ButtonBrowseDataFile.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p>\u6d4f\u89c8\u9009\u62e9\u6570\u636e\u6587\u4ef6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonBrowseDataFile.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u6d4f\u89c8", None))
#if QT_CONFIG(tooltip)
        self.button_save.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u4fdd\u5b58\u914d\u7f6e\u6587\u4ef6</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_save.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Save", None))
#if QT_CONFIG(tooltip)
        self.label_data_file.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#aa0000;\">\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u5165Doors\u7684\u6570\u636e\u6587\u4ef6\uff08.json\uff09</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_data_file.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Update Data", None))
        self.lineEdit_data_file.setText("")
        self.lineEdit_data_file.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u7684\u6570\u636e", None))
#if QT_CONFIG(tooltip)
        self.label_project_name.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u7684Doors\u9879\u76ee\u540d\u79f0</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_project_name.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Project Name", None))
        self.lineEdit_project_name.setText("")
        self.lineEdit_project_name.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u7684\u9879\u76ee\u540d", None))
#if QT_CONFIG(tooltip)
        self.label_data_suffix.setToolTip(QCoreApplication.translate("UIDoorsDataUpdater", u"<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">\u8bf7\u786e\u8ba4Doors Data\u6a21\u5757\u7684\u53d8\u4f53\u540e\u7f00\uff08\u5982\u6709\uff09</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_data_suffix.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Variant Suffix", None))
        self.lineEdit_data_suffix.setText("")
        self.lineEdit_data_suffix.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u8bf7\u786e\u8ba4Data\u6a21\u5757\u7684\u53d8\u4f53\u540e\u7f00", None))
    # retranslateUi

