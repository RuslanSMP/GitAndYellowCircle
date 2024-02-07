from PyQt5 import uic
from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from random import choice, randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self, Form):
        self.setGeometry(300, 300, 150, 150)
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.Button.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_cirlce(qp)
            qp.end()
        self.do_paint = False

    def draw_cirlce(self, qp):
        x = randint(10, 550)
        y = randint(10, 250)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setBrush(QColor(*color))
        leigt = randint(25, 50)
        qp.drawEllipse(x - leigt // 2, y - leigt // 2, leigt,
                       leigt)

if __name__ == '__main__':
    app = QApplication(argv)
    ex = MyWidget()
    ex.show()
    exit(app.exec())