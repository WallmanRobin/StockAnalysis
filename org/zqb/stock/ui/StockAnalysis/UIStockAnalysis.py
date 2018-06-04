# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIStockAnalysis.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from org.zqb.stock.ui.StockAnalysis.StockAnalysisTableView import StockAnalysisTableView

class UIStockAnalysis(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        #要替换成支持拖拽换列顺序的类
        self.tableViewStock = StockAnalysisTableView(self.centralwidget)
        self.tableViewStock.setMouseTracking(True)
        self.tableViewStock.setAcceptDrops(True)
        self.tableViewStock.setDragEnabled(True)
        self.tableViewStock.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableViewStock.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableViewStock.setAlternatingRowColors(True)
        self.tableViewStock.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableViewStock.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableViewStock.setSortingEnabled(True)
        self.tableViewStock.setObjectName("tableViewStock")
        self.gridLayout.addWidget(self.tableViewStock, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuConfig = QtWidgets.QMenu(self.menubar)
        self.menuConfig.setObjectName("menuConfig")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionIndicatorConfig = QtWidgets.QAction(MainWindow)
        self.actionIndicatorConfig.setObjectName("actionIndicatorConfig")
        self.menuFile.addAction(self.actionExit)
        self.menuConfig.addAction(self.actionIndicatorConfig)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())

        self.retranslateUi(MainWindow)
        self.menubar.triggered['QAction*'].connect(MainWindow.showIndicatorConfigWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "股票分析"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menuConfig.setTitle(_translate("MainWindow", "设置"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionIndicatorConfig.setText(_translate("MainWindow", "指标参数设置"))

