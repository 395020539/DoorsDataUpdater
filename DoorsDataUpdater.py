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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_UIDoorsDataUpdater(object):
    def setupUi(self, UIDoorsDataUpdater):
        if not UIDoorsDataUpdater.objectName():
            UIDoorsDataUpdater.setObjectName(u"UIDoorsDataUpdater")
        UIDoorsDataUpdater.resize(646, 306)
        self.button_start = QPushButton(UIDoorsDataUpdater)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(250, 180, 121, 51))
        self.button_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_start.setMouseTracking(False)
        self.button_start.setStyleSheet(u"")
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
        self.layoutWidget = QWidget(UIDoorsDataUpdater)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 70, 481, 79))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_project_name = QLabel(self.layoutWidget)
        self.label_project_name.setObjectName(u"label_project_name")
        self.label_project_name.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_project_name, 0, 0, 1, 1)

        self.lineEdit_project_name = QLineEdit(self.layoutWidget)
        self.lineEdit_project_name.setObjectName(u"lineEdit_project_name")
        self.lineEdit_project_name.setEnabled(True)
        self.lineEdit_project_name.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.lineEdit_project_name, 0, 1, 1, 1)

        self.label_data_file = QLabel(self.layoutWidget)
        self.label_data_file.setObjectName(u"label_data_file")
        self.label_data_file.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_data_file, 1, 0, 1, 1)

        self.lineEdit_data_file = QLineEdit(self.layoutWidget)
        self.lineEdit_data_file.setObjectName(u"lineEdit_data_file")
        self.lineEdit_data_file.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.lineEdit_data_file, 1, 1, 1, 1)

        self.label_data_suffix = QLabel(self.layoutWidget)
        self.label_data_suffix.setObjectName(u"label_data_suffix")
        self.label_data_suffix.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_data_suffix, 2, 0, 1, 1)

        self.lineEdit_data_suffix = QLineEdit(self.layoutWidget)
        self.lineEdit_data_suffix.setObjectName(u"lineEdit_data_suffix")
        self.lineEdit_data_suffix.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.lineEdit_data_suffix, 2, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.button_load = QPushButton(UIDoorsDataUpdater)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setGeometry(QRect(50, 40, 75, 24))
        self.button_save = QPushButton(UIDoorsDataUpdater)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(130, 40, 75, 24))
        self.ButtonBrowseDataFile = QPushButton(UIDoorsDataUpdater)
        self.ButtonBrowseDataFile.setObjectName(u"ButtonBrowseDataFile")
        self.ButtonBrowseDataFile.setGeometry(QRect(540, 100, 61, 21))

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
        self.label_project_name.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Project Name", None))
        self.lineEdit_project_name.setText("")
        self.lineEdit_project_name.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u7684\u9879\u76ee\u540d", None))
        self.label_data_file.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Update Data", None))
        self.lineEdit_data_file.setText("")
        self.lineEdit_data_file.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u8bf7\u786e\u8ba4\u9700\u8981\u66f4\u65b0\u7684\u6570\u636e", None))
        self.label_data_suffix.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Variant Suffix", None))
        self.lineEdit_data_suffix.setText("")
        self.lineEdit_data_suffix.setPlaceholderText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u8bf7\u786e\u8ba4Data\u6a21\u5757\u7684\u53d8\u4f53\u540e\u7f00", None))
        self.button_load.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Load", None))
        self.button_save.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"Save", None))
        self.ButtonBrowseDataFile.setText(QCoreApplication.translate("UIDoorsDataUpdater", u"\u6d4f\u89c8", None))
    # retranslateUi

