from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from org.zqb.stock.ui.IndicatorConfig.UIIndicatorConfigExt import UIIndicatorConfigExt
from org.zqb.stock.ui.IndicatorConfig.WndIndicatorConfig import WndIndicatorConfig

#指标参数设置窗口
class WndStockAnalysis(QtWidgets.QMainWindow):
    analysisWnd = None
    indWnd = None
    def showIndicatorConfigWindow(self):
        self.indWnd = UIIndicatorConfigExt()
        self.indWnd.initIndView(WndIndicatorConfig(self.indWnd, self.analysisWnd))
        #Qt.Qt.WindowModal没有模态窗口效果
        self.indWnd.indMainWnd.setWindowModality(Qt.ApplicationModal)
        self.indWnd.indMainWnd.show()
    def Cancel(self):
        pass
    def OK(self):
        pass
