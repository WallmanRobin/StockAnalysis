from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QComboBox
from PyQt5.Qt import Qt

class IndCfgTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.cellChanged.connect(self.checkBoxToggle)

    def checkBoxToggle(self, row, col):
        if col==2:
            #print(row, col)

            qcom = self.cellWidget(row, 3)

            if self.item(row, col).checkState()==Qt.Checked:
                qcom.setDisabled(False)
            else:
                qcom.setDisabled(True)
