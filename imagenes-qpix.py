# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagenes-qpix.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 581, 501))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("pollito 1.0.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.izan = QtWidgets.QPushButton(self.centralwidget)
        self.izan.setGeometry(QtCore.QRect(10, 502, 271, 61))
        self.izan.setObjectName("izan")
        self.eluney = QtWidgets.QPushButton(self.centralwidget)
        self.eluney.setGeometry(QtCore.QRect(290, 500, 271, 61))
        self.eluney.setObjectName("eluney")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.izan.clicked.connect(self.show_izan)
        self.eluney.clicked.connect(self.show_eluney)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.izan.setText(_translate("MainWindow", "IZAN"))
        self.eluney.setText(_translate("MainWindow", "ELUNEY"))

    def show_izan(self):
        self.photo.setPixmap(QtGui.QPixmap("pollito 1.0.jpg"))

    def show_eluney(self):
        self.photo.setPixmap(QtGui.QPixmap("pollita.jpeg"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
