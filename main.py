from PyQt5 import uic
import io
from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from random import choice, randint


class MyTemplate():
    def __init__(self):
        self.template = """<?xml version="1.0" encoding="UTF-8"?>
        <ui version="4.0">
         <class>MainWindow</class>
         <widget class="QMainWindow" name="MainWindow">
          <property name="geometry">
           <rect>
            <x>0</x>
            <y>0</y>
            <width>598</width>
            <height>353</height>
           </rect>
          </property>
          <property name="windowTitle">
           <string>MainWindow</string>
          </property>
          <widget class="QWidget" name="centralwidget">
           <widget class="QPushButton" name="Button">
            <property name="geometry">
             <rect>
              <x>230</x>
              <y>120</y>
              <width>91</width>
              <height>21</height>
             </rect>
            </property>
            <property name="text">
             <string>Нажми меня!</string>
            </property>
           </widget>
          </widget>
          <widget class="QMenuBar" name="menubar">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>598</width>
             <height>21</height>
            </rect>
           </property>
          </widget>
          <widget class="QStatusBar" name="statusbar"/>
         </widget>
         <resources/>
         <connections/>
        </ui>"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self, Form):
        self.setGeometry(300, 300, 150, 150)
        my_ui = MyTemplate()
        f = io.StringIO(my_ui.template)
        uic.loadUi(f, self)
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
