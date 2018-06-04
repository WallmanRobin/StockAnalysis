#import tushare as tushare
import tushare
import pymysql
#from datetime import datetime, timedelta
import time
import math
import importlib
import pandas as pd


class TushareUtility:
    def getDBConn(self, host='localhost', user='stock', passwd='1qaz', db='stock'):
        conn = pymysql.connect(host, user, passwd, db)
        return conn

    def getStockBasics(self,year=time.localtime()[0]-(time.localtime()[1]==1), quarter=((time.localtime()[1]-1) if time.localtime()[1]>3 else 12)//3):
        basics = tushare.get_stock_basics()

        it = basics.iterrows()
        l = []

        for row in it:
            ll = [row[0]];
            ll.extend(row[1])
            l.append(ll)

        conn = self.getDBConn()
        sql = 'insert into stock_basics values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor = conn.cursor()
        cursor.executemany(sql, l)
        conn.commit()
        conn.close()

    #基本面数据的动态调用函数
    def getBasicListData(self, func, year=time.localtime()[0]-(time.localtime()[1]<4), quarter=((time.localtime()[1]-1) if time.localtime()[1]>3 else 12)//3, month=time.localtime()[1], day=time.localtime()[2], bseq=False):
        ip_module_cls=importlib.import_module('.', 'tushare')
        ip_method = getattr(ip_module_cls, func)
        data = ip_method(year, quarter)
        it = data.iterrows()
        l = []

        for row in it:
            #如果数据是NaN或者是'--'则改为0
            ll=[e if (isinstance(e, str) or not math.isnan(e)) and e!='--' else 0 for e in row[1].values]
            ll.extend([year, quarter, month, day])
            l.append(ll)

        sql='insert into '+func.replace('get_','')+' values('
        sql+='null' if bseq else ''
        s = ''
        for e in data.columns.values:
            s += ',%s'
        s = s.lstrip(',')
        sql += s
        #增加年季月天的参数位置
        sql+=',%s,%s,%s,%s'
        sql+=')'
        conn = self.getDBConn()
        cursor = conn.cursor()
        #print(sql)
        cursor.executemany(sql, l)
        conn.commit()
        conn.close()
        print(func+':'+str(year)+' '+ str(quarter)+' inserted!')
    #历史数据
    def getHistData(self, code, start=None, end=None,ktype='D', bseq=True):
        data = tushare.get_hist_data(code, start, end, ktype, 60, 0.5)

        if data is not None and not data.empty:
            it = data.iterrows()
            l = []
            for row in it:
                ll = [code, row[0]];
                ll.extend(row[1])
                #有些股票取历史数据时少了一列，特殊处理
                if len(data.columns.values)<14:
                    ll.append('0')
                ll.append(ktype)
                #print(ll)
                l.append(ll)


            sql = 'insert into hist_data values('
            sql += 'null' if bseq else ''
            #code和date参数位置
            sql += ',%s,%s'
            # 其他参数位置
            for e in data.columns.values:
                sql += ',%s'
            # 有些股票取历史数据时少了一`列，特殊处理
            if len(data.columns.values)<14:
                sql += ',%s'
            #kdtype参数位置
            sql += ',%s)'
            #print(sql)

            conn = self.getDBConn()
            cursor = conn.cursor()
            cursor.executemany(sql, l)
            conn.commit()
            conn.close()
            print(code+" "+start+" "+end+" inserted")
        else:
            print(code + " " + start + " " + end + " no data")

    #复权数据
    def getHData(self, code, start=None, end=None, autype='qfq', bseq=True):
        data = tushare.get_h_data(code, start, end, autype, 60, 0.5)

        if data is not None and not data.empty:
            it = data.iterrows()
            l = []
            for row in it:
                ll = [code, row[0]];
                ll.extend(row[1])
                ll.append(autype)
                # print(ll)
                l.append(ll)

            sql = 'insert into h_data values('
            sql += 'null' if bseq else ''
            # code和date参数位置
            sql += ',%s,%s'
            # 其他参数位置
            for e in data.columns.values:
                sql += ',%s'
            # autype参数位置
            sql += ',%s)'
            # print(sql)

            conn = self.getDBConn()
            cursor = conn.cursor()
            cursor.executemany(sql, l)
            conn.commit()
            conn.close()
            print(code + " " + start + " " + end + " inserted")
        else:
            print(code + " " + start + " " + end + " no data")

    #一次性获取当前交易所有股票的行情数据
    def getTodayAll(self):
        return tushare.get_today_all()

    #历史分笔
    def getTickData(self,code,date,bseq=True):
        data =  tushare.get_tick_data(code,date,10000,0.5)
        it = data.iterrows()
        l = []

        for row in it:
            if row[1][0][0].isdigit():
                ll=[code, date]
                # 如果数据是NaN或者是'--'则改为0
                ll.extend([e if (isinstance(e, str) or not math.isnan(e)) and e!='--' else 0 for e in row[1].values])
                #print(ll)
                l.append(ll)

        sql = 'insert into tick_data values('
        sql += 'null' if bseq else ''
        # code和date参数位置
        sql += ',%s,%s'
        for e in data.columns.values:
            sql += ',%s'
        sql += ')'
        #print(sql)

        conn = self.getDBConn()
        cursor = conn.cursor()
        cursor.executemany(sql, l)
        conn.commit()
        conn.close()
        print(code+' '+date+' inserted')

    # 大单交易数据
    def getSinaDd(self, code, date, vol=400, bseq=True):
        data = tushare.get_sina_dd(code, date,vol,60,0.5)

        it = data.iterrows()
        l = []

        for row in it:
            ll = [date]
            # 如果数据是NaN或者是'--'则改为0
            ll.extend([e if (isinstance(e, str) or not math.isnan(e)) and e != '--' else 0 for e in row[1].values])
            l.append(ll)

        sql = 'insert into sina_dd values('
        sql += 'null' if bseq else ''
        # date参数位置
        sql += ',%s'
        for e in data.columns.values:
            sql += ',%s'
        sql += ')'
        conn = self.getDBConn()
        cursor = conn.cursor()
        cursor.executemany(sql, l)
        conn.commit()
        conn.close()
        print(code + ' ' + date + ' inserted')

    #股票分类数据的动态调用函数
    def getClassifiedData(self, func, bseq=True):
        tushare.get_tick_data()
        ip_module_cls = importlib.import_module('.', 'tushare')
        ip_method = getattr(ip_module_cls, func)
        data = ip_method()
        if data is not None and not data.empty:
            it = data.iterrows()
            l = []

            for row in it:
                ll=[e if not isinstance(e, pd.Timestamp) else (str(e.year)+'-'+str(e.month).zfill(2)+'-'+str(e.day).zfill(2)) for e in row[1]]
                #print(ll)
                l.append(ll)

            #terminated是敏感字符，后面加a
            sql = 'insert into ' + (func.replace('get_', '') if func!='get_terminated' else (func.replace('get_', '')+'a'))  + ' values('
            sql += 'null' if bseq else ''
            for e in data.columns.values:
                sql += ',%s'
            sql += ')'
            #print(sql)
            conn = self.getDBConn()
            cursor = conn.cursor()
            cursor.executemany(sql, l)
            conn.commit()
            conn.close()
            print(func + ' inserted')
        else:
            print(func + ' no data')