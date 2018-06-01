# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIIndicatorConfig.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UIIndicatorConfig(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxBasics = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxBasics.setGeometry(QtCore.QRect(10, 10, 231, 281))
        self.groupBoxBasics.setObjectName("groupBoxBasics")
        self.tableViewBasics = QtWidgets.QTableView(self.groupBoxBasics)
        self.tableViewBasics.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.tableViewBasics.setObjectName("tableViewBasics")
        self.groupBoxReport = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxReport.setGeometry(QtCore.QRect(240, 10, 231, 281))
        self.groupBoxReport.setObjectName("groupBoxReport")
        self.tableViewReport = QtWidgets.QTableView(self.groupBoxReport)
        self.tableViewReport.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.tableViewReport.setObjectName("tableViewReport")
        self.groupBoxProfilt = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxProfilt.setGeometry(QtCore.QRect(470, 10, 231, 281))
        self.groupBoxProfilt.setObjectName("groupBoxProfilt")
        self.tableViewProfit = QtWidgets.QTableView(self.groupBoxProfilt)
        self.tableViewProfit.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.tableViewProfit.setObjectName("tableViewProfit")
        self.groupBoxOperate = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxOperate.setGeometry(QtCore.QRect(700, 10, 231, 281))
        self.groupBoxOperate.setObjectName("groupBoxOperate")
        self.tableViewOperate = QtWidgets.QTableView(self.groupBoxOperate)
        self.tableViewOperate.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.tableViewOperate.setObjectName("tableViewOperate")
        self.groupBoxGrowth = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxGrowth.setGeometry(QtCore.QRect(10, 300, 231, 281))
        self.groupBoxGrowth.setObjectName("groupBoxGrowth")
        self.tableViewGrowth = QtWidgets.QTableView(self.groupBoxGrowth)
        self.tableViewGrowth.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.tableViewGrowth.setObjectName("tableViewGrowth")
        self.groupBoxDebtpay = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxDebtpay.setGeometry(QtCore.QRect(240, 300, 231, 281))
        self.groupBoxDebtpay.setObjectName("groupBoxDebtpay")
        self.tableViewDebtpay = QtWidgets.QTableView(self.groupBoxDebtpay)
        self.tableViewDebtpay.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.tableViewDebtpay.setObjectName("tableViewDebtpay")
        self.groupBoxCashflow = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxCashflow.setGeometry(QtCore.QRect(470, 300, 231, 281))
        self.groupBoxCashflow.setObjectName("groupBoxCashflow")
        self.tableViewCashflow = QtWidgets.QTableView(self.groupBoxCashflow)
        self.tableViewCashflow.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.tableViewCashflow.setObjectName("tableViewCashflow")
        self.OKButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKButton.setGeometry(QtCore.QRect(20, 610, 75, 23))
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QtCore.QRect(120, 610, 75, 23))
        self.CancelButton.setObjectName("CancelButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.OKButton.clicked.connect(MainWindow.OK)
        self.CancelButton.clicked.connect(MainWindow.Cancel)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "指标参数选择"))
        self.groupBoxBasics.setTitle(_translate("MainWindow", "基本指标"))
        self.groupBoxReport.setTitle(_translate("MainWindow", "业绩指标"))
        self.groupBoxProfilt.setTitle(_translate("MainWindow", "盈利指标"))
        self.groupBoxOperate.setTitle(_translate("MainWindow", "营运指标"))
        self.groupBoxGrowth.setTitle(_translate("MainWindow", "成长指标"))
        self.groupBoxDebtpay.setTitle(_translate("MainWindow", "偿债指标"))
        self.groupBoxCashflow.setTitle(_translate("MainWindow", "现金流量"))
        self.OKButton.setText(_translate("MainWindow", "OK"))
        self.CancelButton.setText(_translate("MainWindow", "Cancel"))

