import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Model:
    def __init__(self):
        self.view = None
        self.contr = None

    def addContr(self, contr):
        self.contr = contr

    def addView(self, view):
        self.view = view

    def notifyView(self):
        self.view.updateAll()