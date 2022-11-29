from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavToolbar
from matplotlib.figure import Figure


class View(QMainWindow):
    def __init__(self, inController, parent=None):
        super().__init__(parent)
        self.controller = inController
        self.ui = Ui(self.controller, self)
        self.setCentralWidget(self.ui)
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.resize(600, 600)


class Ui(QWidget):
    def __init__(self, inContr, parent=None):
        super().__init__(parent)
        self.contr = inContr
        self.parent = parent
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)
        self.main_tab = QTabWidget()
        self.grid.addWidget(self.main_tab, 0, 0)
        self.main_data_tab = QTabWidget()
        self.main_tab.addTab(self.main_data_tab, "Данные")
        self.data_tab_table_cont = SimpleContainer()
        self.main_data_tab.addTab(self.data_tab_table_cont, "Таблица данных")
        self.data_tab_table = SimpleTable()
        self.data_tab_table_cont.grid.addWidget(self.data_tab_table, 0, 0)

        self.data_tab_filter_cont = SimpleContainer()
        self.main_data_tab.addTab(self.data_tab_filter_cont, "Управление данными")

        self.main_graph_tab = QTabWidget()
        self.main_tab.addTab(self.main_graph_tab, "Графики")
        self.graph_tab1 = SimpleGraphContainer()
        self.main_graph_tab.addTab(self.graph_tab1, "По часам")
        self.graph_tab1_param1 = YearMonthDayParamTable()
        self.graph_tab1.grid.addWidget(self.graph_tab1_param1, 1, 0)

        self.graph_tab2 = SimpleGraphContainer()
        self.main_graph_tab.addTab(self.graph_tab2, "Гистограмма среднего потребления")
        self.graph_tab2_mtab = QTabWidget()
        self.graph_tab2.grid.addWidget(self.graph_tab2_mtab, 0, 0)
        self.graph_tab2_param1 = YearMonthParamTable()
        self.graph_tab2_mtab.addTab(self.graph_tab2_param1, "Фильтр")
        self.graph_tab2_param2 = SpinParamTable()
        self.graph_tab2_mtab.addTab(self.graph_tab2_param2, "Диапазоны")




    def updateAll(self):
        pass


class SimpleContainer(QFrame):
    def __init__(self):
        super(SimpleContainer, self).__init__()
        self.grid = QGridLayout()
        self.setLayout(self.grid)


class SimpleGraphContainer(SimpleContainer):
    def __init__(self):
        super(SimpleGraphContainer, self).__init__()
        self.btn = QPushButton("Построить")
        self.grid.addWidget(self.btn, 0, 0)


class SimpleTable(QTableWidget):
    def __init__(self):
        super(SimpleTable, self).__init__()


class LabeledContainer(SimpleContainer):
    def __init__(self, label=""):
        super(LabeledContainer, self).__init__()
        self.label = QLabel(label)
        self.grid.addWidget(self.label, 0, 0)


class LabeledCombo(LabeledContainer):
    def __init__(self, label=""):
        super(LabeledCombo, self).__init__(label)
        self.combo = QComboBox()
        self.grid.addWidget(self.combo, 0, 1)


class LabeledCheck(LabeledContainer):
    def __init__(self, label=""):
        super(LabeledCheck, self).__init__(label)
        self.check = QCheckBox()
        self.grid.addWidget(self.check, 0, 1)


class LabeledSpin(LabeledContainer):
    def __init__(self, label=""):
        super(LabeledSpin, self).__init__(label)
        self.spin = QSpinBox()
        self.grid.addWidget(self.spin, 0, 1)


class LabeledEntry(LabeledContainer):
    def __init__(self, label=""):
        super(LabeledEntry, self).__init__(label)
        self.entry = QLineEdit()
        self.grid.addWidget(self.entry, 0, 1)


class SimpleParamTable(QFrame):
    def __init__(self):
        super(SimpleParamTable, self).__init__()
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.addBtn = QPushButton(text="Добавить")
        self.grid.addWidget(self.addBtn, 1, 1)
        self.table = QTableWidget()
        self.grid.addWidget(self.table, 2, 0, 1, 2)


class SpinParamTable(SimpleParamTable):
    def __init__(self):
        super(SpinParamTable, self).__init__()
        self.entry = LabeledCombo()
        self.grid.addWidget(self.entry, 0, 0, 1, 2)


class YearMonthParamTable(SimpleParamTable):
    def __init__(self):
        super(YearMonthParamTable, self).__init__()
        self.year_combo = LabeledCombo("Год")
        self.month_combo = LabeledCombo("Месяц")
        self.tu_combo = LabeledCombo("Номер ТУ")
        self.addr_combo = LabeledCombo("Адрес")
        self.cbox = SimpleContainer()
        self.cbox.grid.addWidget(self.tu_combo, 0, 0)
        self.cbox.grid.addWidget(self.addr_combo, 1, 0)
        self.cbox.grid.addWidget(self.year_combo, 2, 0)
        self.cbox.grid.addWidget(self.month_combo, 3, 0)
        self.grid.addWidget(self.cbox, 0, 0, 1, 2)


class YearMonthDayParamTable(YearMonthParamTable):
    def __init__(self):
        super(YearMonthDayParamTable, self).__init__()
        self.day_combo = LabeledCombo("День")
        self.cbox.grid.addWidget(self.day_combo, 4, 0)
