from org.zqb.stock.ui.IndicatorConfig import UIIndicatorConfig
from org.zqb.stock.ui.UIIndicatorConfigTableView import IndicatorConfigTableView
from org.zqb.stock.data.IndicatorConfigData import IndicatorConfigData
from PyQt5.QtWidgets import QHeaderView,QTableWidgetItem,QComboBox,QCheckBox
from PyQt5 import QtCore
from PyQt5.Qt import Qt

class UIIndicatorConfigExt(UIIndicatorConfig.UIIndicatorConfig):
    indDataHnd = None
    indMainWnd = None
    listTableWidget = {}
    def initIndViewData(self):
        self.indDataHnd = IndicatorConfigData()
        self.indDataHnd.getIndicator()

    def initIndView(self,mainWnd):
        self.setupUi(mainWnd)
        self.indMainWnd = mainWnd
        #获得要显示的指标
        data = self.initIndViewData()
        n = self.indDataHnd.iClassName
        self.listTableWidget = {n[0]:self.tableWidgetBasics, n[1]:self.tableWidgetReport, n[2]:self.tableWidgetProfit,
                                n[3]:self.tableWidgetOper, n[4]:self.tableWidgetGrowth, n[5]:self.tableWidgetDebt,
                                n[6]:self.tableWidgetCash}
        #显示各列表中的指标参数
        for n,v in self.listTableWidget.items():
            _translate = QtCore.QCoreApplication.translate
            v.setRowCount(len(self.indDataHnd.iClassLabel[n]))
            for i in range(len(self.indDataHnd.iClassLabel[n])):
                #设置前两列code和名称
                code = self.indDataHnd.iClassLabel[n][i][0]
                newItem = QTableWidgetItem(code)
                v.setItem(i, 0, newItem)
                name = self.indDataHnd.iClassLabel[n][i][1]
                newItem = QTableWidgetItem(name)
                v.setItem(i, 1, newItem)
                #设置排序方式
                qcom = QComboBox(v)
                qcom.addItem('降序')
                qcom.addItem('升序')
                s = self.indDataHnd.iClassData[n][code][1]
                if s == 'D':
                    qcom.setCurrentIndex(0)
                else:
                    qcom.setCurrentIndex(1)
                v.setCellWidget(i, 3, qcom)
                #设置是否选中
                qchk = QTableWidgetItem()
                c = self.indDataHnd.iClassData[n][code][0]
                if c=='Checked':
                    qchk.setCheckState(Qt.Checked)
                    qcom.setDisabled(False)
                else:
                    qchk.setCheckState(Qt.Unchecked)
                    qcom.setDisabled(True)
                v.setItem(i, 2, qchk)

            v.resizeColumnToContents(0)
            v.resizeColumnToContents(1)
            v.resizeColumnToContents(2)
            v.resizeColumnToContents(3)

    def saveIndicatorConfig(self):
        '''
        for n, v in self.listTableWidget.items():
            m = v.model()
            i=0
            for c in self.indDataHnd.iClassData[n].keys():
                self.indDataHnd.iClassData[n][c][0] = m.checkList[0][i]
                self.indDataHnd.iClassData[n][c][1] = m.checkList[1][i]
                i+=1
        '''
        for n, v in self.listTableWidget.items():
            i = 0
            for c in self.indDataHnd.iClassData[n].keys():
                print('b0')
                qchk = v.item(i,2)
                print('b1')
                if qchk.checkState()==Qt.Checked:
                    self.indDataHnd.iClassData[n][c][0] = 'Checked'
                else:
                    self.indDataHnd.iClassData[n][c][0] = 'Unchecked'
                print('b2')
                qcom = v.cellWidget(i, 3)
                print('b3')
                if qcom.currentIndex()==0:
                    self.indDataHnd.iClassData[n][c][1] ='D'
                else:
                    self.indDataHnd.iClassData[n][c][1] = 'A'
                print('b4')
                i += 1
        self.indDataHnd.saveConfigData()