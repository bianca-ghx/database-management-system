# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewAllBooksWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewAllBooksWindow(object):
    def setupUi(self, ViewAllBooksWindow):
        ViewAllBooksWindow.setObjectName("ViewAllBooksWindow")
        ViewAllBooksWindow.resize(1000, 900)
        ViewAllBooksWindow.setMinimumSize(QtCore.QSize(1000, 900))
        ViewAllBooksWindow.setMaximumSize(QtCore.QSize(1000, 900))
        self.centralwidget = QtWidgets.QWidget(ViewAllBooksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 30, 521, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 800, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 140, 941, 651))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        ViewAllBooksWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewAllBooksWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        ViewAllBooksWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewAllBooksWindow)
        self.statusbar.setObjectName("statusbar")
        ViewAllBooksWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewAllBooksWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewAllBooksWindow)

    def retranslateUi(self, ViewAllBooksWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewAllBooksWindow.setWindowTitle(_translate("ViewAllBooksWindow", "MainWindow"))
        self.label.setText(_translate("ViewAllBooksWindow", "View All Books"))
        self.pushButton.setText(_translate("ViewAllBooksWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewAllBooksWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewAllBooksWindow()
    ui.setupUi(ViewAllBooksWindow)
    ViewAllBooksWindow.show()
    sys.exit(app.exec_())
