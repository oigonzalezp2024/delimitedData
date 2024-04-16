from delimitedData import DelimitedData

delimitaConsulta = DelimitedData()
delimitaConsulta.oneMonth("fechaMesIni", "./data/json/promedioAbasSipsaMesMadr.json", "./sample/json/oneMonth/oneMonth.json")
delimitaConsulta.quarter("fechaMesIni", "./data/json/promedioAbasSipsaMesMadr.json", "./sample/json/quarter/quarter.json")
delimitaConsulta.semester("fechaMesIni", "./data/json/promedioAbasSipsaMesMadr.json", "./sample/json/semester/semester.json")
