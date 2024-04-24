

from delimitedData import DelimitedData

delimitedData = DelimitedData()
delimitedData.getData("./data/json/promedioAbasSipsaMesMadr.json")
delimitedData.oneMonth("fechaMesIni", pathEnd="./sample/json/oneMonth/oneMonthN2.json")
delimitedData.quarter("fechaMesIni", pathEnd="./sample/json/oneMonth/oneMonthN2.json")
delimitedData.semester("fechaMesIni", pathEnd="./sample/json/oneMonth/oneMonthN2.json")
