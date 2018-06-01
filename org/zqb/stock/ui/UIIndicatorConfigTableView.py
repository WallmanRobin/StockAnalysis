from org.zqb.stock.ui.UICheckboxTableView import CheckboxTableViewModel
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)

class IndicatorConfigTableView(CheckboxTableViewModel):
    def __init__(self, parent=None):
        super(IndicatorConfigTableView, self).__init__(parent)
    def rowCount(self, QModelIndex):
        return len(self.checkList[0])

    def columnCount(self, QModelIndex):
        return len(self.title)

    #tableData:DataFrame(code,name,pe......)
    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return self.tableData[row][col]
            #return 'Row %d, Column %d' % (row + 1, col + 1)
        elif role == Qt.CheckStateRole:
            if col == 0:
                return Qt.Unchecked if 'Unchecked' in self.checkList[0][row] else Qt.Checked
            if col == 2:
                return Qt.Unchecked if 'Unchecked' in self.checkList[1][row] else Qt.Checked
        return QVariant()

    def flags(self, index):
        if index.column() == 0 or index.column() == 2:
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        return Qt.ItemIsEnabled

    def setTableData(self, tableData):
        self.tableData = tableData
        #self.checkList.append(['Unchecked' for e in self.rowData])
        #self.checkList.append(['Unchecked' for e in self.rowData])

    def setTitle(self, title):
        self.title = title

    def rowCount(self, QModelIndex):
        return len(self.checkList[0])

    def setData(self, index, value, role):
        row = index.row()
        col = index.column()
        #self.tableData.iat[row, col] = value
        if role == Qt.CheckStateRole and col == 0:
            self.checkList[0][row] = 'Checked' if value == Qt.Checked else 'Unchecked'
        if role == Qt.CheckStateRole and col == 2:
            self.checkList[1][row] = 'Checked' if value == Qt.Checked else 'Unchecked'
        return True