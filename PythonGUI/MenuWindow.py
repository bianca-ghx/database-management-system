# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(1000, 900)
        MenuWindow.setMinimumSize(QtCore.QSize(1000, 900))
        MenuWindow.setMaximumSize(QtCore.QSize(1000, 900))
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 150, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 310, 291, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.verticalLayout.addWidget(self.pushButton1)
        self.pushButton2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.verticalLayout.addWidget(self.pushButton2)
        self.pushButton3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton3.setObjectName("pushButton3")
        self.verticalLayout.addWidget(self.pushButton3)
        self.pushButton4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton4.setObjectName("pushButton4")
        self.verticalLayout.addWidget(self.pushButton4)
        self.pushButton5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton5.setObjectName("pushButton5")
        self.verticalLayout.addWidget(self.pushButton5)
        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MenuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuWindow)
        self.statusbar.setObjectName("statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "MainWindow"))
        self.label.setText(_translate("MenuWindow", "X Library"))
        self.pushButton1.setText(_translate("MenuWindow", "Add Book"))
        self.pushButton2.setText(_translate("MenuWindow", "Delete Book"))
        self.pushButton3.setText(_translate("MenuWindow", "View Book List"))
        self.pushButton4.setText(_translate("MenuWindow", "Lend Books"))
        self.pushButton5.setText(_translate("MenuWindow", "Receive Returned Books"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(MenuWindow)
    MenuWindow.show()
    sys.exit(app.exec_())
