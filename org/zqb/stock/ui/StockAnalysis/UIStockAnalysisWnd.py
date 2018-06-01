from org.zqb.stock.ui.StockAnalysis import UIStockAnalysis
from org.zqb.stock.data import StockAnalysisData
from org.zqb.stock.ui.UICheckboxTableView import CheckboxTableViewModel
from PyQt5 import QtCore
import numpy as np
import pandas as pd
from org.zqb.stock.data import IndicatorConfigData

class UIStockAnalysisWnd(UIStockAnalysis.UIStockAnalysis, QtCore.QObject):
    #StockAnalysisData的引用
    stockDataHnd = None
    #显示窗口的引用
    mainWnd = None
    def initStockListData(self):
        self.stockDataHnd = StockAnalysisData.StockAnalysisData()
        return self.stockDataHnd.initStockListData()

    def refreshStockListData(self, indDataHnd):
        m = CheckboxTableViewModel()
        pack = self.stockDataHnd.getStockListData(indDataHnd)
        self.tableViewStock.model().setTableData(pack[0])
        self.tableViewStock.model().setTitle(pack[1])

    def initStockAnalysisView(self, mainWnd):
        self.setupUi(mainWnd)
        self.mainWnd = mainWnd
        pack = self.initStockListData()
        m = CheckboxTableViewModel()
        m.setTableData(pack[0])
        m.setTitle(pack[1])
        m.checkList = ['Unchecked' for i in range(len(pack[0]))]
        self.tableViewStock.setModel(m)

'''
    def dropEvent(self, e):
        print(e)
        e.accept()

    def dragEnterEvent(self, e):
        print(e)
        e.accept()

    def dragMoveEvent(self, e):
        print(e)
        e.accept()
'''