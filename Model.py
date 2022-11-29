import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Model:
    def __init__(self):
        self.view = None
        self.contr = None
        self.data = None

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

