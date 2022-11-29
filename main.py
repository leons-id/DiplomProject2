import sys, View, Model, Contr
from PyQt5.QtWidgets import *


def main():
    app = QApplication(sys.argv)
    # app.setStyleSheet(stylesheet)
    model = Model.Model()
    Contr.Contr(model)
    # app.setStyleSheet(Stylesheet_1)
    # print(QStyleFactory.keys())
    app.setStyle('Fusion')
    app.exec_()


if __name__ == '__main__':
    sys.exit(main())

