import sys
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)
from pandas import DataFrame
class CheckBoxHeader(QHeaderView):
    clicked = pyqtSignal(bool)

    _x_offset = 3
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height()-self._width)/2.)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                else:
                    self.isOn = True
                self.clicked.emit(self.isOn)
                self.update()
        super(CheckBoxHeader, self).mousePressEvent(event)

class CheckboxTableViewModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(CheckboxTableViewModel, self).__init__(parent)
        self.tableData = None
        self.checkList = []
        self.title = [[]]
    def setTableData(self, tableData):
        self.tableData = tableData
        #self.checkList = ['Unchecked' for e in self.tableData]
    def setTitle(self, title):
        self.title = title
    def rowCount(self, QModelIndex):
        return len(self.checkList)

    def columnCount(self, QModelIndex):
        return len(self.title)

    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return str(self.tableData.iat[row, col])
            #return 'Row %d, Column %d' % (row + 1, col + 1)
        elif role == Qt.CheckStateRole:
            if col == 0:
                return Qt.Unchecked if 'Unchecked' in self.checkList[row] else Qt.Checked
        return QVariant()

    def setData(self, index, value, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            self.tableData.iat[row, col] = value
        if role == Qt.CheckSthateRole and col == 0:
            self.checkList[row] = 'Checked' if value == Qt.Checked else 'Unchecked'
        return True

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled
        return Qt.ItemIsEnabled|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled

    def headerData(self, section, orientation, role):
        #self.title=['名称','说明']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.title[section]
                '''
                if section == 0:
                    return 'Title 1'
                elif section == 1:
                    return 'Title 2'
                '''
    '''
    def headerClick(self, isOn):
        self.beginResetModel()
        if isOn:
            self.checkList = ['Checked' for e in self.checkList]
            
        else:
            self.checkList = ['Unchecked' for e in self.checkList]
        self.endResetModel()
    '''

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.layoutAboutToBeChanged.emit()
        asc = True
        if(order==Qt.DescendingOrder):
            asc = False
        self.tableData = self.tableData.sort_values(by=self.tableData.columns[Ncol],ascending=asc)
        self.layoutChanged.emit()

    def supportedDropActions(self):
        return Qt.CopyAction | Qt.MoveAction;

    def supportedDragActions(self):
        return Qt.CopyAction | Qt.MoveAction;
