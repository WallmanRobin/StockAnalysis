from PyQt5 import QtWidgets, Qt
import sys

from org.zqb.stock.ui.StockAnalysis.UIStockAnalysis import UIStockAnalysis
from org.zqb.stock.ui.StockAnalysis.UIStockAnalysisWindow import UIStockAnalysisWindow
from org.zqb.stock.ui.StockAnalysis.UIStockAnalysisWnd import UIStockAnalysisWnd

QtWidgets.QApplication.setAttribute(Qt.Qt.AA_EnableHighDpiScaling);
app = QtWidgets.QApplication(sys.argv)
QtWidgets.QMainWindow
window = UIStockAnalysisWindow();
win = UIStockAnalysisWnd()
window.analysisWnd = win
win.initStockAnalysisView(window)
window.show()
sys.exit(app.exec_())
