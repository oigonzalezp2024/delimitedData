from datetime import date
import json

class DelimitedData:

    def __init__(self, path:str="")->None:
        self.data = []
        self.path = ""
        if(path != ""):
            self.getData(path)

    def getData(self, path:str="")->None:
        if(path != ""):
            self.path = path
            f = open(self.path,"r")
            content = f.read()
            f.close()
            self.data = json.loads(content)

    def oneMonth(self, keyDate:str="", path:str="", pathEnd:str="")->None:
        if(path != ""):
            self.path = path
            self.getData(path)
        res = self.period(keyDate, 1)
        content = json.dumps(res, sort_keys=True, indent=4)
        self.saveData(pathEnd, content)

    def quarter(self, keyDate:str="", path:str="", pathEnd:str="")->None:
        if(path != ""):
            self.path = path
            self.getData(path)
        res = self.period(keyDate, 3)
        content = json.dumps(res, sort_keys=True, indent=4)
        self.saveData(pathEnd, content)

    def semester(self, keyDate:str="", path:str="", pathEnd:str="")->None:
        if(path != ""):
            self.path = path
            self.getData(path)
        res = self.period(keyDate, 6)
        content = json.dumps(res, sort_keys=True, indent=4)
        self.saveData(pathEnd, content)

    def period(self, keyDate:str="", meses:int=0)->object:
        data = self.data
        res = []
        for i in data:
            if self.validDate(i, keyDate, meses):
                res.append(i)
        return res
    
    def validDate(self, registro:object={}, keyDate:str="", monthInit:int=0)->bool:
        year = int(registro[keyDate][0:4])
        month = int(registro[keyDate][5:7])
        nowYear = int(date.today().year)
        nowMonth = int(date.today().month)

        checkMonth = nowMonth - monthInit
        if (checkMonth < 0):
            nowYear -= 1
            checkMonth += 12

        if (year == nowYear):
            if (month >= checkMonth):
                return True
            else:
                return False
        else:
            return False

    def saveData(self, path:str="", content:str="")->None:
        f = open(path,"w")
        f.write(content)
        f.close()
