# coding:utf-8
import sys
from time import time

from PyQt5.QtCore import Qt, QCalendar, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

from qfluentwidgets import CalendarPicker, setTheme, Theme


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        self.setStyleSheet('Demo{background: white}')

        self.picker = CalendarPicker(self)
        self.picker.dateChanged.connect(print)

        # set date
        # self.picker.setDate(QDate(2023, 5, 30))

        # customize date format
        # self.picker.setDateFormat(Qt.TextDate)
        # self.picker.setDateFormat('yyyy-M-d')

        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.picker, 0, Qt.AlignCenter)
        self.resize(500, 500)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    t0 = time()
    w = Demo()
    t1 = time()
    print('耗时：', t1-t0)
    w.show()
    app.exec_()