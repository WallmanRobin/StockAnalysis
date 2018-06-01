import pymysql


def getDBConn(host='localhost', user='stock', passwd='1qaz', db='stock'):
    conn = pymysql.connect(host, user, passwd, db)
    return conn

def queryData(sql, *param):
    conn = getDBConn()
    cursor = conn.cursor()
    cursor.execute(sql, param)
    results = cursor.fetchall()
    l = []
    for row in results:
        ll = [e for e in row]
        l.append(ll)
    return l

