from org.zqb.db.util import MysqlUtil
import json

class IndicatorConfigData:
    def __init__(self):
        self.iClassName = []
        self.iClassLabel = {}
        self.iClassData = {}
    #iClassData:{"stock_basics": {"industry": "Checked", "area": "Checked"...
    #iClassLabel:{"stock_basics:[["industry", "行业"], ["area","地区"]...
    #iClassName:{"stock_basics","report_data"...
    def getIndicator(self):
        self.iClassName = [];
        self.iClassLabel = {};
        self.iClassData = {}

        self.loadConfigData()

        self.iClassName = [e for e in self.iClassData.keys()]
        sql = "SELECT COLUMN_NAME, column_comment,' ' FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'stock' and column_name not in ('seq','code','name','year','quarter','month','day') AND TABLE_NAME = %s"
        d = {}
        for e in self.iClassName:
            ll = MysqlUtil.queryData(sql, e)
            self.iClassLabel[e] = ll

    def loadConfigData(self):
        with open('config.json', 'r') as f:
            self.iClassData = json.load(f)['indicator_config']

    def saveConfigData(self):
        data = {}
        with open('config.json', 'r') as f:
            data  = json.load(f)
            data['indicator_config'] = self.iClassData
        with open('config.json', 'w') as f:
                json.dump(data, f)
if __name__ == "__main__":
    d = IndicatorConfigData()
    #data = d.getIndicator()
    #print(data)
    d.getIndicator()
    print(d.iClassLabel)
    print(d.iClassName)
    print(d.iClassData)