from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
import sys
from UITest import UITest

QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling);
app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow();
win = UITest()
win.setupUI(window)
window.show()
sys.exit(app.exec_())