#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 2121asd:03
# @Author  : Wayne
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

from mainUI import *
from PyQt4 import QtGui


class MainWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    app.exec_()
