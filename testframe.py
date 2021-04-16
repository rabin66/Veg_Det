from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from datetime import datetime
import os
from get_price import scrap
from cv2v2 import camera_operate


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowIcon(QtGui.QIcon('icon.png'))
    win.setGeometry(200, 200, 1280, 720)
    win.setStyleSheet("background:rgb(3, 252, 132)")
    win.setWindowTitle("Vegetable Recognition and Price Viewer System")

    labelA = QtWidgets.QLabel(win)
    labelA.setText('Vegetable Recognition and Price Viewer System')
    labelA.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
    labelA.setFixedWidth(1000)
    labelA.setAlignment(QtCore.Qt.AlignCenter)
    labelA.move(100, 150)


    b1 = QtWidgets.QPushButton(win)
    b1.setText("Open Camera")
    b1.setGeometry(525, 500, 200, 50)
    b1.setStyleSheet("background-color: grey")

    def clicked():
       camera_operate()

    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())


##########################################################
todaydate = datetime.now()
filename = todaydate.strftime("%Y%m%d"+".csv")

if os.path.exists(filename):
    print("The price list is updated")
    window()
else:
    scrap()
    print("Scrapping and Running")
    window()