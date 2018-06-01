from org.zqb.stock.Tushare.TushareUtility import TushareUtility
import pymysql
import time
from datetime import datetime, timedelta

def getEveryDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date,"%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += timedelta(days=1)
    return date_list

tu = TushareUtility()

conn = tu.getDBConn()
cursor = conn.cursor()

'''
#获得基本面数据
tu.getStockBasics()
for y in range(2018,2019):
    for m in range(1,2):
        tu.getBasicListData('get_report_data', y, m, 0, 0)
        tu.getBasicListData('get_profit_data',y,m,0,0)
        tu.getBasicListData('get_operation_data',y,m,0,0)
        tu.getBasicListData('get_growth_data',y,m,0,0)
        tu.getBasicListData('get_debtpaying_data',y,m,0,0)
        tu.getBasicListData('get_cashflow_data',y,m,0,0)
'''

'''
#获得历史交易数据
cursor.execute("SELECT CODE FROM stock_basics order by code" )
results = cursor.fetchall()
tl = [['2015-01-01','2017-12-31'],['2018-01-02','2018-05-17']]
ktype=['D','W','M','5','15','30','60']
for row in results:
    for t in tl:
        for k in ktype:
            tu.getHistData(row[0],t[0],t[1], k)
        #pass
conn.close()

for e in['sh','sz','hs300','sz50','zxb','cyb']:
    for t in tl:
        for k in ktype:
            tu.getHistData(e,t[0],t[1], k)

'''

#获得历史分笔
cursor.execute("SELECT a.code, MIN(a.date) FROM tick_data a WHERE a.code=(SELECT MAX(z.code) FROM tick_data z) order by code" )
results = cursor.fetchall()
for row in results:
    code = row[0]
    date = (datetime.strptime(row[1], "%Y-%m-%d")-timedelta(days=1)).strftime("%Y-%m-%d")

dt = getEveryDay('2017-01-01',date)
dt.reverse();
for d in dt:
    tu.getTickData(code, d)

dt = getEveryDay('2017-01-01', '2018-05-17')
dt.reverse();

cursor.execute("SELECT CODE FROM stock_basics where code >'%s' order by code"%(code))
results = cursor.fetchall()
for row in results:
    for d in dt:
        tu.getTickData(row[0],d)


'''
#获得分类数据
tu.getClassifiedData('get_industry_classified')
tu.getClassifiedData('get_concept_classified')
tu.getClassifiedData('get_area_classified')
tu.getClassifiedData('get_sme_classified')
tu.getClassifiedData('get_gem_classified')
tu.getClassifiedData('get_st_classified')
tu.getClassifiedData('get_hs300s')
tu.getClassifiedData('get_sz50s')
tu.getClassifiedData('get_zz500s')
tu.getClassifiedData('get_terminated')
tu.getClassifiedData('get_suspended')
'''



