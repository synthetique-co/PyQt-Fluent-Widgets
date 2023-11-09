# coding:utf-8
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from qfluentwidgets import IndeterminateProgressBar, ProgressBar, FluentThemeColor


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.vBoxLayout = QVBoxLayout(self)
        self.progressBar = ProgressBar(self)
        self.inProgressBar = IndeterminateProgressBar(self)

        # change the color of bar
        # self.progressBar.setCustomBarColor(FluentThemeColor.DEFAULT_BLUE.color(), FluentThemeColor.GOLD.color())
        # self.inProgressBar.setCustomBarColor(FluentThemeColor.DEFAULT_BLUE.color(), FluentThemeColor.GOLD.color())

        self.progressBar.setValue(50)
        self.vBoxLayout.addWidget(self.progressBar)
        self.vBoxLayout.addWidget(self.inProgressBar)
        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.resize(400, 400)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()