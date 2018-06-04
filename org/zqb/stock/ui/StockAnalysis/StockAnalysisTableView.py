from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QDrag
from PyQt5.Qt import Qt

class StockAnalysisTableView(QtWidgets.QTableView):
    sourceCol = None
    targetCol = None
    def dragEnterEvent(self, event):
        l = self.selectedIndexes()
        for e in l:
            print(e.row(),e.column())
            self.sourceCol = e.column()
            break
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        point = event.pos()
        index = self.indexAt(event.pos())
        self.targetCol = index.column()
        self.model().swapTableDataColumns(self.sourceCol, self.targetCol)
        event.accept()

    '''
    def mousePressEvent(self, event):
        print('mousePressEvent called')
        #index = self.indexAt(event.pos())
        #print(index.row(), index.column())
        self.startDrag(event)
    '''
    '''
    def startDrag(self, event):
        print('startDrag called')
        #drag = QDrag(self)
        #index = self.indexAt(event.pos())
        #print(index.row(), index.column())
    '''