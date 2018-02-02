# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import fileManager as filemgr
import logger as logger
import searchUtils as seacher
import time
import DBConnect as dbHandler
import sys

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
        self.processBar = QtGui.QProgressBar(self.splitter_3)
        self.helpButton = QtGui.QPushButton(self.splitter_3)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.gridLayout.addWidget(self.splitter_3, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Click connecter
        self.searchButton.connect(self.searchButton, QtCore.SIGNAL('clicked()'), self.onSearchButtonClicked)
        self.connectButton.connect(self.connectButton, QtCore.SIGNAL('clicked()'), self.onConnectButtonClicked)
        self.helpButton.connect(self.helpButton, QtCore.SIGNAL('clicked()'), self.onhelpButtonClicked)

        # Checkbox connecter
        self.isLog.connect(self.isLog, QtCore.SIGNAL('stateChanged(int)'), self.isLogChecked)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "数据检索工具", None))
        self.dbIPAddressEdit.setText("localhost:3306")
        self.dbNameEdit.setText("lab_db.mri.detect")
        self.keyWordsLabel.setText(_translate("Dialog", "关键词    ", None))
        self.workPathLabel.setText(_translate("Dialog", "工作目录  ", None))
        self.workPathEdit.setText("D:\Documents\Lab\Wayne\Lab Data\Meniscus\半月板\半月板-image\me")
        self.dbIPAddressLabel.setText(_translate("Dialog", "数据库地址", None))
        self.dbNameLabel.setText(_translate("Dialog", "数据库名称", None))
        self.isLog.setText(_translate("Dialog", "日志记录", None))
        self.searchButton.setText(_translate("Dialog", "检索数据", None))
        self.connectButton.setText(_translate("Dialog", "连接数据库", None))
        self.helpButton.setText(_translate("Dialog", "帮助/关于", None))

    # Search button
    def onSearchButtonClicked(self):
        self.keyWords = self.keyWordsEdit.text()
        self.logStatus = self.isLog.checkState()
        self.workPath = self.workPathEdit.text()
        self.onConnectButtonClicked()
        try:
            filemg = filemgr.FileManager()
            filemg.move_file_by_index(self.keyWords, self.workPath)
            # max_counter = 0
            # max_counter=filemg.counter
            print("asddasd"+str(filemg.counter))
            if filemg.counter>0:
                self.processBar.setMinimum(0)
                self.processBar.setMaximum(filemg.counter)
                while filemg.counter > 0:
                    if filemg.counter == 0:
                        break
                    self.processBar.setValue(filemg.counter)

        except OSError:
            logger.warning("OSError")
            logger.exception(sys.stderr)
            QtGui.QMessageBox.warning(self.searchButton, "错误", "找不到工作目录")
        except Exception:
            logger.warning("Search error")
            logger.exception(sys.stderr)
            QtGui.QMessageBox.warning(self.searchButton, "错误", "检索错误，表不存在或表字段不存在")

    # DB connect button
    def onConnectButtonClicked(self):
        self.dbIp = self.dbIPAddressEdit.text()
        self.dbName = self.dbNameEdit.text()
        try:
            dbHand = dbHandler.DBConnect()
            dbHand.setUpDB(host=self.dbIp.split(":")[0], port=int(self.dbIp.split(":")[1]),
                           dbname=self.dbName.split(".")[0], schema=self.dbName.split('.')[1],
                           schemaTable=self.dbName.split('.')[2])
        except Exception:
            logger.warning("try connect " + self.dbIp + ":" + self.dbName + "error")
            logger.exception(sys.stderr)
            QtGui.QMessageBox.warning(self.connectButton, "错误", "连接数据库出错")

    # is Log check
    def isLogChecked(self):
        if self.isLog.isChecked():
            logger.stopLogging()
            logger.startLogging()
            logger.info("Start logging")
        else:
            logger.stopLogging()
            logger.info("Stop logging")

    # Help button
    def onhelpButtonClicked(self):
        QtGui.QMessageBox.information(self.helpButton, "关于", str("关键词即为我们搜索的词，支持模糊检索\n"
                                                                 "工作目录是指检索的目录，同时会在工作目录生成分类文件\n"
                                                                 "IP地址是指数据库连接地址，默认端口为3306\n"
                                                                 "数据库是指检索的数据库，默认为mysql\n"
                                                                 "日志记录将记录每次检索的日志，保存在工作目录中\n"
                                                                 "Powered by PyQT,Code by Wayne,@Waynehfut"))
