# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FeiQ.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setMaximumSize(QtCore.QSize(211, 16777215))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.widget_4)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.listChat = QtWidgets.QListView(self.tab)
        self.listChat.setObjectName("listChat")
        self.gridLayout_6.addWidget(self.listChat, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listFriend = QtWidgets.QListView(self.tab_2)
        self.listFriend.setObjectName("listFriend")
        self.gridLayout_5.addWidget(self.listFriend, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 8)
        self.gridLayout_4.addWidget(self.widget_4, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.chatTitle = QtWidgets.QLabel(self.widget_2)
        self.chatTitle.setGeometry(QtCore.QRect(10, 0, 491, 20))
        self.chatTitle.setObjectName("chatTitle")
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.emojiToolButton = QtWidgets.QToolButton(self.widget_3)
        self.emojiToolButton.setGeometry(QtCore.QRect(10, 0, 31, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolbutton/Static/resource/emoji.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emojiToolButton.setIcon(icon)
        self.emojiToolButton.setIconSize(QtCore.QSize(24, 24))
        self.emojiToolButton.setObjectName("emojiToolButton")
        self.ImageToolButton = QtWidgets.QToolButton(self.widget_3)
        self.ImageToolButton.setGeometry(QtCore.QRect(50, 0, 31, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/toolbutton/Static/resource/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ImageToolButton.setIcon(icon1)
        self.ImageToolButton.setIconSize(QtCore.QSize(24, 24))
        self.ImageToolButton.setObjectName("ImageToolButton")
        self.gridLayout_3.addWidget(self.widget_3, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 3, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 20)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setRowStretch(3, 5)
        self.gridLayout_3.setRowStretch(4, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.listFriend.doubleClicked['QModelIndex'].connect(MainWindow.onFriendDbClick)
        self.pushButton.clicked.connect(MainWindow.onSendMessage)
        self.listChat.clicked['QModelIndex'].connect(MainWindow.onClickChatItem)
        self.emojiToolButton.clicked.connect(MainWindow.onClickEmoji)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "聊天"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "通讯录"))
        self.chatTitle.setText(_translate("MainWindow", "TextLabel"))
        self.emojiToolButton.setText(_translate("MainWindow", "..."))
        self.ImageToolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "按住Ctrl+Enter以换行"))
        self.pushButton.setText(_translate("MainWindow", "发送"))

import res_rc
