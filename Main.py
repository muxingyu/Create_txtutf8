# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# test

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 186)
        Dialog.setMinimumSize(QtCore.QSize(420, 186))
        Dialog.setMaximumSize(QtCore.QSize(420, 186))
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.bt_get_path = QtWidgets.QPushButton(Dialog)
        self.bt_get_path.setGeometry(QtCore.QRect(360, 40, 31, 31))
        self.bt_get_path.setObjectName("bt_get_path")
        self.bt_start = QtWidgets.QPushButton(Dialog)
        self.bt_start.setGeometry(QtCore.QRect(140, 110, 151, 31))
        self.bt_start.setObjectName("bt_start")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 160, 294, 18))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_word = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_word.setChecked(True)
        self.cb_word.setObjectName("cb_word")
        self.horizontalLayout.addWidget(self.cb_word)
        self.cb_exl = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_exl.setChecked(True)
        self.cb_exl.setObjectName("cb_exl")
        self.horizontalLayout.addWidget(self.cb_exl)
        self.cb_plp = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_plp.setChecked(True)
        self.cb_plp.setObjectName("cb_plp")
        self.horizontalLayout.addWidget(self.cb_plp)
        self.cb_pdf = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_pdf.setChecked(True)
        self.cb_pdf.setObjectName("cb_pdf")
        self.horizontalLayout.addWidget(self.cb_pdf)
        self.cb_txt = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_txt.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cb_txt.setFont(font)
        self.cb_txt.setObjectName("cb_txt")
        self.horizontalLayout.addWidget(self.cb_txt)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "批量建立UTF8格式TXT文件"))
        self.bt_get_path.setText(_translate("Dialog", "..."))
        self.bt_start.setText(_translate("Dialog", "Start"))
        self.cb_word.setText(_translate("Dialog", "Word"))
        self.cb_exl.setText(_translate("Dialog", "Excel"))
        self.cb_plp.setText(_translate("Dialog", "PowelPoint"))
        self.cb_pdf.setText(_translate("Dialog", "PDF"))
        self.cb_txt.setText(_translate("Dialog", "TXT"))

