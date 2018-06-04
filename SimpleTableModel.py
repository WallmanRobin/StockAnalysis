from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)
from TableViewTest import TableViewTest
import sys

class SimpleTableModel(QAbstractTableModel):
    def rowCount(self, QModelIndex):
        return 4

    def columnCount(self, QModelIndex):
        return 4

    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return 'Row %d, Column %d' % (row + 1, col + 1)
        return QVariant()

    def headerData(self, section, orientation, role):
        t = ['Col1', 'Col2', 'Col3', 'Col4']
        print('b1')
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return t[section]

    def flags(self, index):

        return Qt.ItemIsEnabled|Qt.ItemIsEditable

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow();
win = TableViewTest()
print('a1')
win.setupUI(window)
'''
m = QtGui.QStandardItemModel()
for (idx, data) in enumerate(['foo', 'bar', 'baz']):
    item_1 = QtGui.QStandardItem('Item {}'.format(idx))
    # item_1.setEditable(False)
    # item_1.setDropEnabled(False)

    item_2 = QtGui.QStandardItem(data)
    # item_2.setEditable(False)
    # item_2.setDropEnabled(False)
    m.appendRow([item_1, item_2])
'''
win.tableView.setModel(SimpleTableModel())
print('a2')
window.show()
sys.exit(app.exec_())