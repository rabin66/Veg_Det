from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):

    def open_cam(self):
        from cv2v2 import camera_operate
        from datetime import datetime
        todaydate = datetime.now()
        filename = todaydate.strftime("%Y%m%d" + ".csv")

        if os.path.exists(filename):
            print("The price list is updated")
        else:
            from get_price import scrap
            scrap()
            print("Scrapping and Running")
        print("opened camera")
        camera_operate()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1221, 772)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Veg_Det/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleName("")
        MainWindow.setAutoFillBackground(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameVRPVS = QtWidgets.QLabel(self.centralwidget)
        self.nameVRPVS.setGeometry(QtCore.QRect(130, 20, 981, 91))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nameVRPVS.setFont(font)
        self.nameVRPVS.setObjectName("nameVRPVS")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(0, 100, 1221, 641))
        self.img.setAcceptDrops(False)
        self.img.setAutoFillBackground(True)
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("../Veg_Det/photo.png"))
        self.img.setObjectName("img")

        print(" check 1 ")

        self.startRecognition = QtWidgets.QPushButton(self.centralwidget)
        self.startRecognition.setGeometry(QtCore.QRect(510, 550, 231, 61))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.startRecognition.setFont(font)
        self.startRecognition.setObjectName("startRecognition")
        self.startRecognition.clicked.connect(self.open_cam)

        self.img.raise_()
        self.nameVRPVS.raise_()
        self.startRecognition.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vegetable Recognition and Price Viewer System"))
        self.nameVRPVS.setText(_translate("MainWindow", "VEGETABLE RECOGNITION AND PRICE VIEWER SYSTEM"))
        self.startRecognition.setText(_translate("MainWindow", "Start Recognition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

