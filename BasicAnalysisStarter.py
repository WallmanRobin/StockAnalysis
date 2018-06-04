from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
import sys

from org.zqb.stock.ui.StockAnalysis.UIStockAnalysis import UIStockAnalysis
from org.zqb.stock.ui.StockAnalysis.WndStockAnalysis import WndStockAnalysis
from org.zqb.stock.ui.StockAnalysis.UIStockAnalysisExt import UIStockAnalysisExt

QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling);
app = QtWidgets.QApplication(sys.argv)
window = WndStockAnalysis();
win = UIStockAnalysisExt()
window.analysisWnd = win
win.initStockAnalysisView(window)
window.show()
sys.exit(app.exec_())
