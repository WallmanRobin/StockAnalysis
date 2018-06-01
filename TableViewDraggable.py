#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class MyModel(QtGui.QStandardItemModel):

    def dropMimeData(self, data, action, row, col, parent):
        """
        Always move the entire row, and don't allow column "shifting"
        """
        return super().dropMimeData(data, action, 0, col , parent)

class MyStyle(QtWidgets.QProxyStyle):

    def drawPrimitive(self, element, option, painter, widget=None):
        """
        Draw a line across the entire row rather than just the column
        we're hovering over.  This may not always work depending on global
        style - for instance I think it won't work on OSX.
        """
        if element == self.PE_IndicatorItemViewItemDrop and not option.rect.isNull():
            option_new = QtWidgets.QStyleOption(option)
            option_new.rect.setLeft(0)
            if widget:
                option_new.rect.setRight(widget.width())
            option = option_new
        super().drawPrimitive(element, option, painter, widget)

class MyTableView(QtWidgets.QTableView):

    def __init__(self, parent):
        super().__init__(parent)
        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setSelectionBehavior(self.SelectColumns)
        self.setSelectionMode(self.SingleSelection)
        self.setShowGrid(False)
        self.setDragDropMode(self.InternalMove)
        self.setDragDropOverwriteMode(False)

        # Set our custom style - this draws the drop indicator across the whole row
        self.setStyle(MyStyle())

        # Set our custom model - this prevents row "shifting"
        self.model = MyModel()
        self.setModel(self.model)

        for (idx, data) in enumerate(['foo', 'bar', 'baz']):
            item_1 = QtGui.QStandardItem('Item {}'.format(idx))
            #item_1.setEditable(False)
            #item_1.setDropEnabled(False)

            item_2 = QtGui.QStandardItem(data)
            #item_2.setEditable(False)
            #item_2.setDropEnabled(False)

            self.model.appendRow([item_1, item_2])

class Testing(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        # Main widget
        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        self.setCentralWidget(w)

        # spacer
        l.addWidget(QtWidgets.QLabel('top'), 1)

        # Combo Box
        l.addWidget(MyTableView(self))

        # spacer
        l.addWidget(QtWidgets.QLabel('bottom'), 1)

        # A bit of window housekeeping
        self.resize(400, 400)
        self.setWindowTitle('Testing')
        self.show()

if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    test = Testing()
    sys.exit(app.exec_())