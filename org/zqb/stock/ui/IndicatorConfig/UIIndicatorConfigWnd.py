from org.zqb.stock.ui.IndicatorConfig import UIIndicatorConfig
from org.zqb.stock.ui.UIIndicatorConfigTableView import IndicatorConfigTableView
from org.zqb.stock.data.IndicatorConfigData import IndicatorConfigData

class UiIndicatorConfigWnd(UIIndicatorConfig.UIIndicatorConfig):
    indDataHnd = None
    def initIndViewData(self):
        self.indDataHnd = IndicatorConfigData()
        self.indDataHnd.getIndicator()

    def initIndView(self,mainWnd):
        self.setupUi(mainWnd)
        self.indMainWnd = mainWnd
        self.indMainWnd.wnd = self

        #获得要显示的指标
        data = self.initIndViewData()
        n = self.indDataHnd.iClassName
        self.listTableView = {n[0]:self.tableViewBasics, n[1]:self.tableViewReport, n[2]:self.tableViewProfit,
                              n[3]:self.tableViewOperate, n[4]:self.tableViewGrowth, n[5]:self.tableViewDebtpay,
                              n[6]:self.tableViewCashflow}

        #显示各列表中的指标参数
        i = 0
        title = ['名称','说明','升序']
        for n,v in self.listTableView.items():
            m = IndicatorConfigTableView()
            m.setTableData(self.indDataHnd.iClassLabel[n])
            m.setTitle(title)
            l0 = []
            l1 = []
            for e in self.indDataHnd.iClassData[n].values():
                l0.append(e[0])
                l1.append(e[1])
            m.checkList.append(l0)
            m.checkList.append(l1)
            v.setModel(m)

    def saveIndicatorConfig(self):
        for n, v in self.listTableView.items():
            m = v.model()
            i=0
            for c in self.indDataHnd.iClassData[n].keys():
                self.indDataHnd.iClassData[n][c][0] = m.checkList[0][i]
                self.indDataHnd.iClassData[n][c][1] = m.checkList[1][i]
                i+=1
        self.indDataHnd.saveConfigData()