# encoding:utf-8

import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Main import Ui_Dialog


class mywindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.bt_get_path.clicked.connect(self.get_path)
        self.bt_start.clicked.connect(self.start)

    def sum_cb(self):
        filetype = []
        cb = ['exl', 'pdf', 'plb', 'txt', 'word']
        if(self.cb_pdf.isChecked()):
            filetype.append('.pdf')
        if(self.cb_exl.isChecked()):
            filetype.append('.xls')
            filetype.append('.xlsx')
        if(self.cb_plp.isChecked()):
            filetype.append('.ppt')
            filetype.append('.pptx')
        if(self.cb_word.isChecked()):
            filetype.append('.doc')
            filetype.append('.docx')
        if (self.cb_txt.isChecked()):
            filetype.append('.txt')
        if filetype:
            return filetype
        else:
            QtWidgets.QMessageBox.warning(self, "Message", "     未选择任何处理格式!!!     ", QMessageBox.Yes)

    def start(self):
        filetype = self.sum_cb()
        if os.path.exists(self.lineEdit.text()):
            for dirpath, dirnames, filenames in os.walk(self.lineEdit.text()):
                for file in filenames:
                    newfilename = dirpath + '\\' + os.path.splitext(file)[0] + '.txt'
                    if(os.path.splitext(file)[1] in filetype):
                        print(newfilename)
                        with open(newfilename, 'w', encoding='utf-8') as f:
                            f.write('样例abc')
            QtWidgets.QMessageBox.information(self, "Message", "     新建完成!!!     ", QMessageBox.Yes)
        else:
            QtWidgets.QMessageBox.warning(self, "Message", "     请先选择证据库路径!!!     ", QMessageBox.Yes)

    def get_path(self):
        get_dir = QtWidgets.QFileDialog.getExistingDirectory(self, u'选择证据文件目录', './')
        get_dir = get_dir.replace('/', '\\')
        self.lineEdit.setText(get_dir)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
