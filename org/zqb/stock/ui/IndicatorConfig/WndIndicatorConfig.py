from PyQt5 import QtWidgets, QtGui

#指标参数设置窗口
class WndIndicatorConfig(QtWidgets.QMainWindow):
    indUI = None
    analysisWnd = None

    def __init__(self, indUI, analysisWnd):
        QtWidgets.QMainWindow.__init__(self)
        self.indUI = indUI
        self.analysisWnd = analysisWnd
    def cancel(self):
        self.hide()
        pass
    def OK(self):
        print('a0')
        cfg = self.indUI.saveIndicatorConfig()
        print('a1')
        self.analysisWnd.refreshStockListData(self.indUI.indDataHnd)
        print('a2')
        self.hide()