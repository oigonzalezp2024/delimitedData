from datetime import date
import json

class DelimitedData:

    def oneMonth(self, keyDate, path, pathEnd):
        data = self.getData(path)
        fil = []
        for i in data:
            if(self.validDate(i, keyDate, 1)):
                fil.append(i)
        content = json.dumps(fil, sort_keys=True, indent=4)
        self.saveData(pathEnd, content)

    def quarter(self, keyDate, path, pathEnd):
        data = self.getData(path)
        fil = []
        for i in data:
            if(self.validDate(i, keyDate, 3)):
                fil.append(i)
        content = json.dumps(fil, sort_keys=True, indent=4)
        self.saveData(pathEnd, content)

    def semester(self, keyDate, path, pathEnd):
        data = self.getData(path)
        fil = []
        for i in data:
            if(self.validDate(i, keyDate, 6)):
                fil.append(i)
        content = json.dumps(fil, sort_keys=True, indent=4)
        self.saveData(pathEnd, content)

    def getData(self, path):
        f = open(path,"r")
        content = f.read()
        f.close()
        return json.loads(content)

    def saveData(self, path, content):
        f = open(path,"w")
        f.write(content)
        f.close()

    def validDate(self, registro, keyDate, monthInit):
        year = int(registro[keyDate][0:4])
        month = int(registro[keyDate][5:7])
        nowYear = int(date.today().year)
        nowMonth = int(date.today().month)

        if(year == nowYear):
            print(year, month, nowYear, nowMonth)
            if(month >= nowMonth-monthInit):
                print(year, month, nowYear, nowMonth)
                return True
            else:
                return False
        else:
            return False

