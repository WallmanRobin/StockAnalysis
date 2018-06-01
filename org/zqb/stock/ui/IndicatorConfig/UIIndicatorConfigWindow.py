from PyQt5 import QtWidgets, QtGui

#指标参数设置窗口
class UIIndicatorConfigWindow(QtWidgets.QMainWindow):
    indWnd = None
    analysisWnd = None
    def Hello(self):
        pass
    def Cancel(self):
        self.hide()
        pass
    def OK(self):
        cfg = self.indWnd.saveIndicatorConfig()
        self.analysisWnd.refreshStockListData(self.indWnd.indDataHnd)
        self.hide()