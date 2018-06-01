from org.zqb.db.util import MysqlUtil
from org.zqb.stock.data import IndicatorConfigData
from pandas import pandas
import json
import pandas
import time

class StockAnalysisData:
    def getStockDataFrame(self, classData=None):
        cn = [e for e in classData.keys()]
        conn = MysqlUtil.getDBConn()
        #取最近的年和季度
        year = time.localtime()[0] - (time.localtime()[1] == 1)
        quarter = quarter=(time.localtime()[1] if time.localtime()[1]>3 else 12)//3
        dateWhere = "  A.YEAR=%d AND A.QUARTER=%d"%(year, quarter)
        excludeWhere = " AND NOT EXISTS(SELECT 'x' FROM terminateda Z WHERE A.CODE=Z.CODE) AND NOT EXISTS(SELECT 'x' FROM suspended Z WHERE A.CODE=Z.CODE)"

        for e in cn:
            if e=='stock_basics':
                sql = 'SELECT DISTINCT A.* FROM %s A WHERE 1=1 %s'%(e, excludeWhere)
                self.stockDataFrame = pandas.read_sql(sql, conn, 'code')
                #print(stockDataFrame.ix['000001',])
            else:
                sql = 'SELECT DISTINCT  A.* FROM %s A WHERE %s'%  (e, dateWhere + excludeWhere)
                df = pandas.read_sql(sql, conn, 'code')
                df.drop(columns=['name','year','quarter','month','day'], inplace=True)
                dup = [d for d in df.columns if d in self.stockDataFrame.columns]
                di = {}
                for du in dup:
                    di[du] = du+'_'+e
                df.rename(columns=di, inplace=True)
                #print(df.ix['000001', ])
                self.stockDataFrame = self.stockDataFrame.join(df)
        self.stockDataFrame.fillna(0, inplace=True)
        sort = self.getSortCols(classData)
        self.stockDataFrame.sort_values(by=sort[0], ascending=sort[1], inplace=True)

    def getSortCols(self, classData):
        cn = [e for e in classData.keys()]
        sortCols = []
        sortMth = []
        dataCols = [e for e in self.stockDataFrame.keys()]

        for e in cn:
            indDict = classData[e]
            for k, c in indDict.items():
                if c[0]=='Checked':
                    if (k + '_' + e) in dataCols:
                        sortCols.append(k + '_' + e)
                        if(c[1]=='Checked'):
                            sortMth.append(True)
                        else:
                            sortMth.append(False)
                    else:
                        if (k) in dataCols:
                            sortCols.append(k)
                            sortMth.append(c[1])
        return [sortCols, sortMth]

    #刚打开时，从配置文件中读取配置信息
    def initStockListData(self):
        indDataHandler = IndicatorConfigData.IndicatorConfigData()
        indDataHandler.getIndicator()
        return self.getStockListData(indDataHandler)

    #配置窗口点击保存后从配置窗口获取配置信息
    def getStockListData(self, indDataHnd):
        self.getStockDataFrame(indDataHnd.iClassData)

        title = ['代码','名称']
        dfCheckedCols = ['code','name']
        dfCols = [e for e in self.stockDataFrame.columns]
        for c,g in indDataHnd.iClassData.items():
            pos = 0
            for ind, ck in g.items():
                if ck[0]=='Checked':
                    if (indDataHnd.iClassLabel[c][pos][0] + '_' + c) in dfCols:
                        dfCheckedCols.append(indDataHnd.iClassLabel[c][pos][0] + '_' + c)
                    else:
                        if (indDataHnd.iClassLabel[c][pos][0]) in dfCols:
                            dfCheckedCols.append(indDataHnd.iClassLabel[c][pos][0])
                    title.append(indDataHnd.iClassLabel[c][pos][1])
                pos += 1

        # 将code列暂时从索引中去掉，和各列一起输出到TableView中
        self.stockDataFrame.reset_index(inplace=True)
        #print(self.stockDataFrame[dfCheckedCols][(self.stockDataFrame['name']=='华夏幸福')])
        self.stockDataFrame = self.restrictStockListData(dfCheckedCols)

        df = self.stockDataFrame[dfCheckedCols]
        #print(self.stockDataFrame)
        # 将code列设回索引
        self.stockDataFrame.set_index('code', inplace=True)
        pack=[]
        pack.append(df)
        pack.append(title)
        return pack

    def restrictStockListData(self, restrictCols):
        i = 0
        index = [True]
        for e in restrictCols:
            if (e != 'code' and e != 'name'):
                if i == 0:
                    index = (self.stockDataFrame[e] != 0)
                else:
                    index = index & (self.stockDataFrame[e] != 0)
            i += 1
        return self.stockDataFrame[index]
if __name__=='__main__':
    with open('config.json', 'r') as f:
        iClassData = json.load(f)['indicator_config']
    s = StockAnalysisData()
    p = s.initStockListData()