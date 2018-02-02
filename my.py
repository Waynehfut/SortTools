# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import FileManager as filemgr

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(388, 180)
        Dialog.setMinimumSize(QtCore.QSize(388, 180))
        Dialog.setMaximumSize(QtCore.QSize(388, 180))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 388, 180))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_6 = QtGui.QSplitter(self.widget)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))

        # Key words
        self.keyWordsLabel = QtGui.QLabel(self.splitter_6)
        self.keyWordsLabel.setObjectName(_fromUtf8("searchWord"))
        self.keyWordsEdit = QtGui.QLineEdit(self.splitter_6)
        self.keyWordsEdit.setObjectName(_fromUtf8("destPath_5"))

        self.gridLayout.addWidget(self.splitter_6, 0, 0, 1, 1)
        self.splitter_5 = QtGui.QSplitter(self.widget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))

        # Work path
        self.workPathLabel = QtGui.QLabel(self.splitter_5)
        self.workPathLabel.setObjectName(_fromUtf8("keyWordsLabel_4"))
        self.workPathEdit = QtGui.QLineEdit(self.splitter_5)
        self.workPathEdit.setObjectName(_fromUtf8("destPath_3"))

        self.gridLayout.addWidget(self.splitter_5, 1, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))

        # DB Ip address
        self.dbIPAddressLabel = QtGui.QLabel(self.splitter)
        self.dbIPAddressLabel.setObjectName(_fromUtf8("keyWordsLabel_2"))
        self.dbIPAddressEdit = QtGui.QLineEdit(self.splitter)
        self.dbIPAddressEdit.setObjectName(_fromUtf8("destPath"))

        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 1)
        self.splitter_4 = QtGui.QSplitter(self.widget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))

        self.dbNameLabel = QtGui.QLabel(self.splitter_4)
        self.dbNameLabel.setObjectName(_fromUtf8("keyWordsLabel_3"))
        self.dbNameEdit = QtGui.QLineEdit(self.splitter_4)
        self.dbNameEdit.setObjectName(_fromUtf8("destPath_2"))

        self.gridLayout.addWidget(self.splitter_4, 3, 0, 1, 1)
        self.splitter_2 = QtGui.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))

        self.connectButton = QtGui.QPushButton(self.splitter_2)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.searchButton = QtGui.QPushButton(self.splitter_2)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))

        self.gridLayout.addWidget(self.splitter_2, 4, 0, 1, 1)
        self.splitter_3 = QtGui.QSplitter(self.widget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.isLog = QtGui.QCheckBox(self.splitter_3)
        self.isLog.setObjectName(_fromUtf8("isLog"))
        self.isReport = QtGui.QCheckBox(self.splitter_3)
        self.isReport.setObjectName(_fromUtf8("isReport"))
        self.isStrict = QtGui.QCheckBox(self.splitter_3)
        self.isStrict.setObjectName(_fromUtf8("isStrict"))
        self.helpButton = QtGui.QPushButton(self.splitter_3)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.gridLayout.addWidget(self.splitter_3, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # Click connecter
        self.searchButton.connect(self.searchButton, QtCore.SIGNAL('clicked()'), self.onsearchButtonClicked)
        self.connectButton.connect(self.connectButton, QtCore.SIGNAL('clicked()'), self.onconnectButtonClicked)
        self.helpButton.connect(self.helpButton, QtCore.SIGNAL('clicked()'), self.onhelpButtonClicked)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "数据检索工具", None))
        self.keyWordsLabel.setText(_translate("Dialog", "关键词    ", None))
        self.workPathLabel.setText(_translate("Dialog", "工作目录  ", None))
        self.dbIPAddressLabel.setText(_translate("Dialog", "数据库地址", None))
        self.dbNameLabel.setText(_translate("Dialog", "数据库名称", None))
        self.isLog.setText(_translate("Dialog", "日志记录", None))
        self.isReport.setText(_translate("Dialog", "结果报告", None))
        self.isStrict.setText(_translate("Dialog", "严格模式", None))
        self.searchButton.setText(_translate("Dialog", "检索数据", None))
        self.connectButton.setText(_translate("Dialog", "连接数据库", None))
        self.helpButton.setText(_translate("Dialog", "帮助/关于", None))

    def onsearchButtonClicked(self):
        self.keyWords = self.keyWordsEdit.text()
        self.workPath = self.workPathEdit.text()
        self.dbIp = self.dbIPAddressEdit.text()
        self.dbName = self.dbNameEdit.text()
        print(self.keyWords, '-', self.workPath, '-', self.dbIp, '-', self.dbName)
        filemgr.FileManager.move_file_by_index(self.keyWords, self.workPath)

    def onconnectButtonClicked(self):
        print(1)

    def onhelpButtonClicked(self):
        QtGui.QMessageBox.information(self.helpButton, "关于", str("以下是简单的帮助说明：\n"
                                                                 "关键词即为我们搜索的词，支持模糊检索\n"
                                                                 "工作目录是指检索的目录，同时会在工作目录生成分类文件\n"
                                                                 "IP地址是指数据库连接地址，默认端口为3306\n"
                                                                 "数据库是指检索的数据库，默认为mysql\n"
                                                                 "日志记录将记录每次检索的日志，保存在工作目录中\n"
                                                                 "结果报告将记录检索的统计信息，保存在工作目录中\n"
                                                                 "严格模式将仅检索关键词，不检索近似词\n"
                                                                 "Powered by PyQT,Code by Wayne,@Waynehfut"))
