# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(858, 658)
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 171, 641))
        self.verticalFrame.setStyleSheet("background-color:rgb(181, 176, 172)")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_add = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_add.setStyleSheet("color:white;\n"
"\n"
"font: 16pt \"田氏颜体大字库\";")
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_delete = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_delete.setStyleSheet("color:white;\n"
"\n"
"font: 16pt \"田氏颜体大字库\";")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout_2.addWidget(self.pushButton_delete)
        self.pushButton_change = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_change.setStyleSheet("color:white;\n"
"\n"
"font: 16pt \"田氏颜体大字库\";")
        self.pushButton_change.setObjectName("pushButton_change")
        self.verticalLayout_2.addWidget(self.pushButton_change)
        self.pushButton_search = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_search.setStyleSheet("color:white;\n"
"\n"
"font: 16pt \"田氏颜体大字库\";\n"
"")
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout_2.addWidget(self.pushButton_search)
        self.pushButton_show = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_show.setStyleSheet("color:white;\n"
"\n"
"font: 16pt \"田氏颜体大字库\";")
        self.pushButton_show.setObjectName("pushButton_show")
        self.verticalLayout_2.addWidget(self.pushButton_show)
        self.pushButton_count = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_count.setStyleSheet("color:white;\n"
"\n"
"font: 16pt \"田氏颜体大字库\";")
        self.pushButton_count.setObjectName("pushButton_count")
        self.verticalLayout_2.addWidget(self.pushButton_count)
        self.pushButton_exit = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_exit.setStyleSheet("color:white;\n"
"\n"
"font: 16pt \"田氏颜体大字库\";")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout_2.addWidget(self.pushButton_exit)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(170, 0, 691, 631))
        self.stackedWidget.setStyleSheet("font: 14pt \"田氏颜体大字库\";")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_add = QtWidgets.QWidget()
        self.page_add.setObjectName("page_add")
        self.label_11 = QtWidgets.QLabel(self.page_add)
        self.label_11.setGeometry(QtCore.QRect(40, 40, 221, 51))
        font = QtGui.QFont()
        font.setFamily("田氏颜体大字库")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 16pt \"田氏颜体大字库\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_add)
        self.label_12.setGeometry(QtCore.QRect(200, 120, 81, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_add)
        self.label_13.setGeometry(QtCore.QRect(180, 170, 101, 41))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_add)
        self.label_14.setGeometry(QtCore.QRect(160, 210, 121, 51))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_add)
        self.label_15.setGeometry(QtCore.QRect(160, 320, 111, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page_add)
        self.label_16.setGeometry(QtCore.QRect(420, 360, 81, 51))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page_add)
        self.label_17.setGeometry(QtCore.QRect(210, 420, 71, 41))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page_add)
        self.label_18.setGeometry(QtCore.QRect(210, 370, 81, 31))
        self.label_18.setObjectName("label_18")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 120, 121, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_12.setGeometry(QtCore.QRect(290, 480, 111, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_13.setGeometry(QtCore.QRect(490, 370, 81, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_14.setGeometry(QtCore.QRect(290, 430, 111, 31))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_19 = QtWidgets.QLabel(self.page_add)
        self.label_19.setGeometry(QtCore.QRect(160, 480, 111, 31))
        self.label_19.setObjectName("label_19")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_24.setGeometry(QtCore.QRect(290, 170, 211, 31))
        self.lineEdit_24.setStyleSheet("font: 10pt \"田氏颜体大字库\";\n"
"color:rgb(203, 203, 203)")
        self.lineEdit_24.setText("")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_8.setGeometry(QtCore.QRect(290, 220, 211, 31))
        self.lineEdit_8.setStyleSheet("font: 10pt \"田氏颜体大字库\";\n"
"color:rgb(203, 203, 203)")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_9.setGeometry(QtCore.QRect(290, 320, 211, 31))
        self.lineEdit_9.setStyleSheet("font: 10pt \"田氏颜体大字库\";\n"
"color:rgb(203, 203, 203)")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_44 = QtWidgets.QLabel(self.page_add)
        self.label_44.setGeometry(QtCore.QRect(580, 370, 71, 21))
        font = QtGui.QFont()
        font.setFamily("田氏颜体大字库")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_add)
        self.pushButton_10.setGeometry(QtCore.QRect(292, 540, 91, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_47 = QtWidgets.QLabel(self.page_add)
        self.label_47.setGeometry(QtCore.QRect(430, 420, 111, 41))
        self.label_47.setObjectName("label_47")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_18.setGeometry(QtCore.QRect(550, 430, 131, 31))
        self.lineEdit_18.setStyleSheet("font: 10pt \"田氏颜体大字库\";\n"
"color:rgb(203, 203, 203)")
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_20 = QtWidgets.QLabel(self.page_add)
        self.label_20.setGeometry(QtCore.QRect(430, 480, 111, 31))
        self.label_20.setObjectName("label_20")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_19.setGeometry(QtCore.QRect(550, 480, 131, 31))
        self.lineEdit_19.setStyleSheet("font: 10pt \"田氏颜体大字库\";\n"
"color:rgb(203, 203, 203)")
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_38 = QtWidgets.QLabel(self.page_add)
        self.label_38.setGeometry(QtCore.QRect(0, 0, 688, 641))
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("familytreeapp/background.png"))
        self.label_38.setObjectName("label_38")
        self.lineEdit = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit.setGeometry(QtCore.QRect(290, 370, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.page_add)
        self.label.setGeometry(QtCore.QRect(210, 270, 91, 31))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 270, 111, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_38.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_13.raise_()
        self.lineEdit_14.raise_()
        self.label_19.raise_()
        self.lineEdit_24.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_9.raise_()
        self.label_44.raise_()
        self.pushButton_10.raise_()
        self.label_47.raise_()
        self.lineEdit_18.raise_()
        self.label_20.raise_()
        self.lineEdit_19.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.lineEdit_2.raise_()
        self.stackedWidget.addWidget(self.page_add)
        self.page_delete = QtWidgets.QWidget()
        self.page_delete.setObjectName("page_delete")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.page_delete)
        self.lineEdit_16.setGeometry(QtCore.QRect(430, 120, 111, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_21 = QtWidgets.QLabel(self.page_delete)
        self.label_21.setGeometry(QtCore.QRect(50, 40, 181, 51))
        self.label_21.setStyleSheet("font: 16pt \"田氏颜体大字库\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page_delete)
        self.label_22.setGeometry(QtCore.QRect(80, 120, 361, 31))
        self.label_22.setObjectName("label_22")
        self.label_39 = QtWidgets.QLabel(self.page_delete)
        self.label_39.setGeometry(QtCore.QRect(0, 0, 688, 641))
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap("familytreeapp/background.png"))
        self.label_39.setObjectName("label_39")
        self.label_23 = QtWidgets.QLabel(self.page_delete)
        self.label_23.setGeometry(QtCore.QRect(80, 230, 221, 31))
        self.label_23.setObjectName("label_23")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_delete)
        self.textBrowser.setGeometry(QtCore.QRect(80, 270, 471, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_delete)
        self.pushButton_9.setGeometry(QtCore.QRect(460, 500, 91, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton = QtWidgets.QPushButton(self.page_delete)
        self.pushButton.setGeometry(QtCore.QRect(430, 170, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_39.raise_()
        self.lineEdit_16.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.textBrowser.raise_()
        self.pushButton_9.raise_()
        self.pushButton.raise_()
        self.stackedWidget.addWidget(self.page_delete)
        self.page_change = QtWidgets.QWidget()
        self.page_change.setObjectName("page_change")
        self.label_25 = QtWidgets.QLabel(self.page_change)
        self.label_25.setGeometry(QtCore.QRect(50, 40, 241, 51))
        self.label_25.setStyleSheet("font: 16pt \"田氏颜体大字库\";")
        self.label_25.setObjectName("label_25")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_change)
        self.pushButton_8.setGeometry(QtCore.QRect(470, 520, 91, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_40 = QtWidgets.QLabel(self.page_change)
        self.label_40.setGeometry(QtCore.QRect(0, 0, 688, 641))
        self.label_40.setText("")
        self.label_40.setPixmap(QtGui.QPixmap("familytreeapp/background.png"))
        self.label_40.setObjectName("label_40")
        self.label_24 = QtWidgets.QLabel(self.page_change)
        self.label_24.setGeometry(QtCore.QRect(80, 120, 351, 31))
        self.label_24.setObjectName("label_24")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.page_change)
        self.lineEdit_17.setGeometry(QtCore.QRect(430, 120, 111, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_26 = QtWidgets.QLabel(self.page_change)
        self.label_26.setGeometry(QtCore.QRect(80, 180, 221, 31))
        self.label_26.setObjectName("label_26")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_change)
        self.textBrowser_2.setGeometry(QtCore.QRect(90, 230, 471, 171))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_27 = QtWidgets.QLabel(self.page_change)
        self.label_27.setGeometry(QtCore.QRect(90, 420, 231, 31))
        self.label_27.setObjectName("label_27")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_change)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 420, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_28 = QtWidgets.QLabel(self.page_change)
        self.label_28.setGeometry(QtCore.QRect(230, 470, 231, 31))
        self.label_28.setObjectName("label_28")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_change)
        self.lineEdit_10.setGeometry(QtCore.QRect(330, 470, 121, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_change)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 120, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_40.raise_()
        self.label_25.raise_()
        self.pushButton_8.raise_()
        self.label_24.raise_()
        self.lineEdit_17.raise_()
        self.label_26.raise_()
        self.textBrowser_2.raise_()
        self.label_27.raise_()
        self.comboBox_2.raise_()
        self.label_28.raise_()
        self.lineEdit_10.raise_()
        self.pushButton_2.raise_()
        self.stackedWidget.addWidget(self.page_change)
        self.page_search = QtWidgets.QWidget()
        self.page_search.setObjectName("page_search")
        self.label_45 = QtWidgets.QLabel(self.page_search)
        self.label_45.setGeometry(QtCore.QRect(0, 0, 688, 641))
        self.label_45.setText("")
        self.label_45.setPixmap(QtGui.QPixmap("familytreeapp/background.png"))
        self.label_45.setObjectName("label_45")
        self.label_29 = QtWidgets.QLabel(self.page_search)
        self.label_29.setGeometry(QtCore.QRect(50, 40, 181, 51))
        self.label_29.setStyleSheet("font: 16pt \"田氏颜体大字库\";")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.page_search)
        self.label_30.setGeometry(QtCore.QRect(80, 120, 351, 31))
        self.label_30.setObjectName("label_30")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_search)
        self.lineEdit_11.setGeometry(QtCore.QRect(432, 120, 111, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_31 = QtWidgets.QLabel(self.page_search)
        self.label_31.setGeometry(QtCore.QRect(80, 170, 181, 51))
        self.label_31.setObjectName("label_31")
        self.comboBox_3 = QtWidgets.QComboBox(self.page_search)
        self.comboBox_3.setGeometry(QtCore.QRect(250, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("田氏颜体大字库")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("font: 12pt \"田氏颜体大字库\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_search)
        self.textBrowser_3.setGeometry(QtCore.QRect(90, 290, 461, 231))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_32 = QtWidgets.QLabel(self.page_search)
        self.label_32.setGeometry(QtCore.QRect(80, 240, 381, 31))
        self.label_32.setObjectName("label_32")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_search)
        self.pushButton_13.setGeometry(QtCore.QRect(430, 180, 121, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.stackedWidget.addWidget(self.page_search)
        self.page_show = QtWidgets.QWidget()
        self.page_show.setObjectName("page_show")
        self.label_41 = QtWidgets.QLabel(self.page_show)
        self.label_41.setGeometry(QtCore.QRect(0, 0, 688, 641))
        self.label_41.setText("")
        self.label_41.setPixmap(QtGui.QPixmap("familytreeapp/background.png"))
        self.label_41.setObjectName("label_41")
        self.treeWidget = QtWidgets.QTreeWidget(self.page_show)
        self.treeWidget.setGeometry(QtCore.QRect(80, 150, 541, 411))
        self.treeWidget.setObjectName("treeWidget")
        self.label_2 = QtWidgets.QLabel(self.page_show)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 51, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_show)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 80, 111, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.page_show)
        self.label_3.setGeometry(QtCore.QRect(250, 80, 191, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_show)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 80, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_show)
        self.page_count = QtWidgets.QWidget()
        self.page_count.setObjectName("page_count")
        self.label_9 = QtWidgets.QLabel(self.page_count)
        self.label_9.setGeometry(QtCore.QRect(180, 170, 231, 61))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_count)
        self.label_10.setGeometry(QtCore.QRect(180, 250, 231, 31))
        self.label_10.setObjectName("label_10")
        self.label_35 = QtWidgets.QLabel(self.page_count)
        self.label_35.setGeometry(QtCore.QRect(160, 310, 221, 51))
        self.label_35.setObjectName("label_35")
        self.label_42 = QtWidgets.QLabel(self.page_count)
        self.label_42.setGeometry(QtCore.QRect(0, 0, 688, 641))
        self.label_42.setText("")
        self.label_42.setPixmap(QtGui.QPixmap("familytreeapp/background.png"))
        self.label_42.setObjectName("label_42")
        self.label_46 = QtWidgets.QLabel(self.page_count)
        self.label_46.setGeometry(QtCore.QRect(50, 40, 181, 51))
        self.label_46.setStyleSheet("font: 16pt \"田氏颜体大字库\";")
        self.label_46.setObjectName("label_46")
        self.label_42.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_35.raise_()
        self.label_46.raise_()
        self.stackedWidget.addWidget(self.page_count)
        self.stackedWidget.raise_()
        self.verticalFrame.raise_()
        home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 25))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.edit = QtWidgets.QMenu(self.menubar)
        self.edit.setObjectName("edit")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        home.setMenuBar(self.menubar)
        self.act_save = QtWidgets.QAction(home)
        self.act_save.setObjectName("act_save")
        self.act_save_as = QtWidgets.QAction(home)
        self.act_save_as.setObjectName("act_save_as")
        self.act_exit = QtWidgets.QAction(home)
        self.act_exit.setObjectName("act_exit")
        self.act_change = QtWidgets.QAction(home)
        self.act_change.setObjectName("act_change")
        self.act_delete = QtWidgets.QAction(home)
        self.act_delete.setObjectName("act_delete")
        self.act_add = QtWidgets.QAction(home)
        self.act_add.setObjectName("act_add")
        self.act_new = QtWidgets.QAction(home)
        self.act_new.setObjectName("act_new")
        self.actionpingjunnian = QtWidgets.QAction(home)
        self.actionpingjunnian.setObjectName("actionpingjunnian")
        self.actionr = QtWidgets.QAction(home)
        self.actionr.setObjectName("actionr")
        self.act_count = QtWidgets.QAction(home)
        self.act_count.setObjectName("act_count")
        self.file.addAction(self.act_new)
        self.file.addAction(self.act_save)
        self.file.addAction(self.act_save_as)
        self.file.addAction(self.act_exit)
        self.edit.addAction(self.act_change)
        self.edit.addAction(self.act_delete)
        self.edit.addAction(self.act_add)
        self.edit.addAction(self.act_count)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.edit.menuAction())
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(home)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "家谱管理系统"))
        self.pushButton_add.setText(_translate("home", "添加信息"))
        self.pushButton_delete.setText(_translate("home", "删除信息"))
        self.pushButton_change.setText(_translate("home", "查找/修改"))
        self.pushButton_search.setText(_translate("home", "查找关系"))
        self.pushButton_show.setText(_translate("home", "查看家谱"))
        self.pushButton_count.setText(_translate("home", "统计信息"))
        self.pushButton_exit.setText(_translate("home", "退出系统"))
        self.label_11.setText(_translate("home", "添加人员基本信息"))
        self.label_12.setText(_translate("home", "姓名："))
        self.label_13.setText(_translate("home", "出生地："))
        self.label_14.setText(_translate("home", "出生日期："))
        self.label_15.setText(_translate("home", "死亡日期："))
        self.label_16.setText(_translate("home", "身高："))
        self.label_17.setText(_translate("home", "职业："))
        self.label_18.setText(_translate("home", "性别："))
        self.label_19.setText(_translate("home", "父亲姓名："))
        self.label_44.setText(_translate("home", "cm"))
        self.pushButton_10.setText(_translate("home", "保存"))
        self.label_47.setText(_translate("home", "配偶姓名："))
        self.label_20.setText(_translate("home", "母亲姓名："))
        self.label.setText(_translate("home", "年龄："))
        self.label_21.setText(_translate("home", "删除人员信息"))
        self.label_22.setText(_translate("home", "请输入你想要删除的人员的姓名："))
        self.label_23.setText(_translate("home", "TA的信息如下所示："))
        self.pushButton_9.setText(_translate("home", "删除"))
        self.pushButton.setText(_translate("home", "查找信息"))
        self.label_25.setText(_translate("home", "查找/修改人员信息"))
        self.pushButton_8.setText(_translate("home", "保存"))
        self.label_24.setText(_translate("home", "请输入你想要修改的人员的名字："))
        self.label_26.setText(_translate("home", "TA的信息如下所示："))
        self.label_27.setText(_translate("home", "你想要修改的信息是："))
        self.comboBox_2.setItemText(0, _translate("home", "年龄"))
        self.comboBox_2.setItemText(1, _translate("home", "出生地"))
        self.comboBox_2.setItemText(2, _translate("home", "死亡日期"))
        self.comboBox_2.setItemText(3, _translate("home", "出生日期"))
        self.comboBox_2.setItemText(4, _translate("home", "身高"))
        self.comboBox_2.setItemText(5, _translate("home", "职业"))
        self.label_28.setText(_translate("home", "修改为："))
        self.pushButton_2.setText(_translate("home", "查找信息"))
        self.label_29.setText(_translate("home", "查找人员关系"))
        self.label_30.setText(_translate("home", "请输入你想要查找的人员的名字："))
        self.label_31.setText(_translate("home", "你想要查找TA的"))
        self.comboBox_3.setItemText(0, _translate("home", "父亲"))
        self.comboBox_3.setItemText(1, _translate("home", "配偶"))
        self.comboBox_3.setItemText(2, _translate("home", "兄弟姐妹"))
        self.comboBox_3.setItemText(3, _translate("home", "母亲"))
        self.comboBox_3.setItemText(4, _translate("home", "孩子"))
        self.label_32.setText(_translate("home", "查找的人员的对象的信息如下所示："))
        self.pushButton_13.setText(_translate("home", "开始查找"))
        self.treeWidget.headerItem().setText(0, _translate("home", "查看家谱"))
        self.label_2.setText(_translate("home", "以"))
        self.label_3.setText(_translate("home", "为祖先查看家谱"))
        self.pushButton_3.setText(_translate("home", "查看"))
        self.label_9.setText(_translate("home", "平均年龄：  岁"))
        self.label_10.setText(_translate("home", "平均身高：  cm"))
        self.label_35.setText(_translate("home", "家庭总人口：  人"))
        self.label_46.setText(_translate("home", "统计人员信息"))
        self.file.setTitle(_translate("home", "文件"))
        self.edit.setTitle(_translate("home", "编辑"))
        self.help.setTitle(_translate("home", "帮助"))
        self.act_save.setText(_translate("home", "保存"))
        self.act_save_as.setText(_translate("home", "另存为"))
        self.act_exit.setText(_translate("home", "退出"))
        self.act_change.setText(_translate("home", "修改"))
        self.act_delete.setText(_translate("home", "删除"))
        self.act_add.setText(_translate("home", "添加"))
        self.act_new.setText(_translate("home", "新建"))
        self.actionpingjunnian.setText(_translate("home", "平均年龄"))
        self.actionr.setText(_translate("home", "平均寿命"))
        self.act_count.setText(_translate("home", "统计"))
