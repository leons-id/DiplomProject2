import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Model:
    def __init__(self):
        self.view = None
        self.contr = None
        self.data = None
        self.cur_filter = ""
        self.fdata = self.data

    def addContr(self, contr):
        self.contr = contr

    def addView(self, view):
        self.view = view

    def notifyView(self):
        self.view.updateAll()

    def getDataFromFile(self, filename):
        try:
            data = pd.read_csv(filename, delimiter=';')
            print(filename.split(r'/')[-1].split('_')[1].split('.')[0], filename)
        except Exception as e:
            print(e)
            return
        dts = []
        for i in range(len(data.values)):
            for j in range(1, len(data.values[0])):
                # temp_time_minute.append(int(data.columns.values[j].split(':')[1]))
                dts.append([round(float(data.values[i][j].replace(",", ".")), 3),
                            int(data.values[i][0].split('.')[2]),
                            int(data.values[i][0].split('.')[1]),
                            int(data.values[i][0].split('.')[0]),
                            int(data.columns.values[j].split(':')[0]),
                            str(filename.split(r'/')[-1].split('_')[1].split('.')[0]), 'NULL'])
        self.data = pd.DataFrame(dts, columns=["Значение", "Год", "Месяц", "День", "Час", "Адрес", "ТУ"])
        print(self.data)

    def createSingleFilter(self, arg, cond, value, data):
        result = None
        if arg in data.columns:
            if cond == "равно":
                result = data[data[arg] == value]
            elif cond == "больше":
                result = data[data[arg] > value]
            elif cond == "меньше":
                result = data[data[arg] < value]
            elif cond == "больше или равно":
                result = data[data[arg] >= value]
            elif cond == "меньше или равно":
                result = data[data[arg] <= value]
            elif cond == "не равно":
                result = data[data[arg] != value]
        return result

    def createFilterRequest(self, inFilter):
        infFilter1 = inFilter[0]
        infFilter2 = inFilter[1]
        arg1 = infFilter1.get("arg")
        cond1 = infFilter1.get("cond")
        value1 = infFilter1.get("value")
        arg2 = infFilter1.get("arg")
        cond2 = infFilter1.get("cond")
        value2 = infFilter1.get("value")
        correct1 = False
        correct2 = False
        if arg1 != "" and cond1 != "" and value1 != "":
            self.fdata = self.createSingleFilter(arg1, cond1, value1, self.data)
            if arg2 != "" and cond2 != "" and value2 != "":
                self.fdata = self.createSingleFilter(arg2, cond2, value1, self.fdata)
        self.view.updateAll()

