from PyQt5 import QtWidgets, Qt
from org.zqb.stock.ui.IndicatorConfig.UIIndicatorConfigWnd import UiIndicatorConfigWnd
from org.zqb.stock.ui.IndicatorConfig.UIIndicatorConfigWindow import UIIndicatorConfigWindow

#指标参数设置窗口
class UIStockAnalysisWindow(QtWidgets.QMainWindow):
    analysisWnd = None
    indWnd = None
    def showIndicatorConfigWindow(self):
        self.indWnd = UiIndicatorConfigWnd()
        self.indWnd.initIndView(UIIndicatorConfigWindow())
        #Qt.Qt.WindowModal没有模态窗口效果
        self.indWnd.indMainWnd.analysisWnd = self.analysisWnd
        self.indWnd.indMainWnd.setWindowModality(Qt.Qt.ApplicationModal)
        self.indWnd.indMainWnd.indWnd = self.indWnd
        self.indWnd.indMainWnd.show()
    def Cancel(self):
        pass
    def OK(self):
        pass
