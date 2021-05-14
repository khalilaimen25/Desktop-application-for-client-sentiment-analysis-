# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from main import *
import hotels_list
from QLabelClickable import *
from histogram import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 530)
        MainWindow.setMinimumSize(QtCore.QSize(875, 530))
        MainWindow.setMaximumSize(QtCore.QSize(875, 530))
        MainWindow.setStyleSheet("color:#fff")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(875, 540))
        self.centralwidget.setMaximumSize(QtCore.QSize(875, 540))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 875, 540))
        self.label.setMinimumSize(QtCore.QSize(575, 530))
        self.label.setMaximumSize(QtCore.QSize(1000, 600))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(140, 40, 601, 65))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.logo.setStyleSheet("background-color:transparent;")
        self.container = QtWidgets.QFrame(self.centralwidget)
        self.container.setGeometry(QtCore.QRect(0, 110, 881, 391))
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.result_frame = QtWidgets.QFrame(self.container)
        self.result_frame.setGeometry(QtCore.QRect(40, 110, 811, 271))
        self.result_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")

        self.search_frame = QtWidgets.QFrame(self.container)
        self.search_frame.setGeometry(QtCore.QRect(10, 3, 861, 104))
        self.search_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.location = QtWidgets.QRadioButton(self.search_frame)
        self.location.setGeometry(QtCore.QRect(290, 80, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.location.setFont(font)
        self.location.setStyleSheet("color:#62b6b6;\n"
"font-size:14px;\n"
"font-weight: bold;\n"
"\n"
"")
        self.location.setObjectName("location")
        self.all = QtWidgets.QRadioButton(self.search_frame)
        self.all.setGeometry(QtCore.QRect(140, 80, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.all.setFont(font)
        self.all.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.all.setAutoFillBackground(False)
        self.all.setStyleSheet("color:#6e9ddd;\n"
"font-size:14px;\n"
"font-weight: bold;")
        self.all.setChecked(True)
        self.all.setObjectName("all")
        self.lineEdit = QtWidgets.QLineEdit(self.search_frame)
        self.lineEdit.setGeometry(QtCore.QRect(440, 29, 271, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color:#0a3555;\n"
"padding-left:10px;\n"
"")
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.service = QtWidgets.QRadioButton(self.search_frame)
        self.service.setGeometry(QtCore.QRect(200, 80, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.service.setFont(font)
        self.service.setStyleSheet("color:#6e9ddd;\n"
"font-size:14px;\n"
"font-weight: bold;\n"
"")
        self.service.setObjectName("service")
        self.food = QtWidgets.QRadioButton(self.search_frame)
        self.food.setGeometry(QtCore.QRect(570, 80, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.food.setFont(font)
        self.food.setStyleSheet("color:#62b6b6;\n"
"font-size:14px;\n"
"font-weight: bold;\n"
"\n"
"")
        self.food.setObjectName("food")
        self.entertainment = QtWidgets.QRadioButton(self.search_frame)
        self.entertainment.setGeometry(QtCore.QRect(710, 80, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.entertainment.setFont(font)
        self.entertainment.setStyleSheet("color:#62b6b6;\n"
"font-size:14px;\n"
"font-weight: bold;\n"
"\n"
"")
        self.entertainment.setObjectName("entertainment")
        self.search = QtWidgets.QLabel(self.search_frame)
        self.search.setGeometry(QtCore.QRect(70, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.search.setFont(font)
        self.search.setAcceptDrops(False)
        self.search.setStyleSheet("color:#fff;\n"
"font-size:16px;\n"
"font-weight: bold;\n"
"")
        self.search.setFrameShadow(QtWidgets.QFrame.Plain)
        self.search.setTextFormat(QtCore.Qt.AutoText)
        self.search.setObjectName("search")
        self.label_5 = QtWidgets.QLabel(self.search_frame)
        self.label_5.setGeometry(QtCore.QRect(461, 4, 121, 18))
        self.label_5.setStyleSheet("color:#fff")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.search_frame)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font-size:16px;\n"
"font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.submit = QtWidgets.QPushButton(self.search_frame)
        self.submit.setGeometry(QtCore.QRect(730, 30, 90, 27))
        self.submit.setStyleSheet("color:#000")
        self.submit.setObjectName("submit")
        self.clean = QtWidgets.QRadioButton(self.search_frame)
        self.clean.setGeometry(QtCore.QRect(380, 80, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.clean.setFont(font)
        self.clean.setStyleSheet("color:#62b6b6;\n"
"font-size:14px;\n"
"font-weight: bold;\n"
"\n"
"")
        self.clean.setObjectName("clean")
        self.price = QtWidgets.QRadioButton(self.search_frame)
        self.price.setGeometry(QtCore.QRect(640, 80, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.price.setFont(font)
        self.price.setStyleSheet("color:#62b6b6;\n"
"font-size:14px;\n"
"font-weight: bold;\n"
"\n"
"")
        self.price.setObjectName("price")
        self.list_hotels = QtWidgets.QComboBox(self.search_frame)
        self.list_hotels.setGeometry(QtCore.QRect(190, 30, 231, 25))
        self.list_hotels.setObjectName("list_hotels")
        self.list_hotels.setStyleSheet("color:#0a3555;")

        self.rooms = QtWidgets.QRadioButton(self.search_frame)
        self.rooms.setGeometry(QtCore.QRect(490, 80, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.rooms.setFont(font)
        self.rooms.setStyleSheet("color:#62b6b6;\n"
"font-size:14px;\n"
"font-weight: bold;\n"
"\n"
"")
        self.rooms.setObjectName("rooms")
        self.enable_search = QtWidgets.QCheckBox(self.search_frame)
        self.enable_search.setGeometry(QtCore.QRect(438, 3, 21, 20))
        self.enable_search.setText("")
        self.enable_search.setObjectName("enable_search")

        self.result_frame = QtWidgets.QFrame(self.container)
        self.error_frame = QtWidgets.QFrame(self.container)

        self.frame_2 = QtWidgets.QFrame(self.result_frame)
        self.frame_3 = QtWidgets.QFrame(self.result_frame)
        self.frame_4 = QtWidgets.QFrame(self.result_frame)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("color:#fff;")
        self.label_5.setObjectName("label_4")


        self.posnum = QtWidgets.QLabel(self.frame_2)
        self.posper = QtWidgets.QLabel(self.frame_2)
        self.comment_result = QtWidgets.QLabel(self.result_frame)
        self.comment_error = QtWidgets.QLabel(self.error_frame)

        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.neunum = QtWidgets.QLabel(self.frame_3)
        self.neuper = QtWidgets.QLabel(self.frame_3)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setStyleSheet("color:#fff;")

        self.negnum = QtWidgets.QLabel(self.frame_4)
        self.negper = QtWidgets.QLabel(self.frame_4)

        self.result_frame.setGeometry(QtCore.QRect(30, 120, 811, 270))
        self.result_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")

        self.error_frame.setGeometry(QtCore.QRect(30, 120, 811, 261))
        self.error_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.error_frame.setObjectName("error_frame")

        self.error_frame.hide()

        self.frame_2.setGeometry(QtCore.QRect(20, 40, 241, 201))
        self.frame_2.setStyleSheet("background-color:rgb(255,255,255,70);\n"
                                   "border-radius: 10px ;\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4.setGeometry(QtCore.QRect(0, 0, 241, 41))
        self.label_4.setStyleSheet("font-size:20px;\n"
                                   "font-weight:bold;\n"
                                   "background-color:green;\n"
                                   "border: 2px solid white;\n"
                                   "border-radius:10px 10px 1px 1px;")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.posnum.setGeometry(QtCore.QRect(10, 50, 221, 20))
        self.posnum.setStyleSheet("color:#000;\n"
                                  "font-size:12px;\n"
                                  "font-weight:bold;\n"
                                  "background-color:rgb(255,0,0,0)\n"
                                  "")
        self.posnum.setText("")
        self.posnum.setAlignment(QtCore.Qt.AlignCenter)
        self.posnum.setObjectName("posnum")
        self.posper.setGeometry(QtCore.QRect(10, 70, 211, 101))
        self.posper.setStyleSheet("color:#1eb521;\n"
                                  "font-size:90px;\n"
                                  "background-color:rgb(255,0,0,0)")
        self.posper.setText("")
        self.posper.setAlignment(QtCore.Qt.AlignCenter)
        self.posper.setObjectName("posper")
        self.comment_result.setGeometry(QtCore.QRect(10, 0, 750, 37))
        self.comment_result.setMinimumSize(QtCore.QSize(791, 0))
        self.comment_result.setStyleSheet("font-size:20px;\n"
                                          "font-weight:bold;\n"
                                          "color:white;")
        self.comment_result.setText("")
        self.comment_result.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.comment_result.setObjectName("comment_result")
        self.comment_result.setStyleSheet("background-color:rgb(0,0,0,70);font-size:22px;font-weight:bold;border-radius: 10px")
        self.frame_3.setGeometry(QtCore.QRect(280, 40, 241, 201))
        self.frame_3.setStyleSheet("background-color:rgb(255,255,255,70);\n"
                                   "border-radius: 10px ;\n"
                                   "")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_7.setGeometry(QtCore.QRect(0, 0, 241, 41))
        self.label_7.setStyleSheet("font-size:20px;\n"
                                   "font-weight:bold;\n"
                                   "background-color:#f7f147;\n"
                                   "border: 2px solid white;\n"
                                   "border-radius:10px 10px 1px 1px;\n"
                                   "color:#8e8f91")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.neunum.setGeometry(QtCore.QRect(10, 50, 221, 20))
        self.neunum.setStyleSheet("color:#000;\n"
                                  "font-size:12px;\n"
                                  "font-weight:bold;\n"
                                  "background-color:rgb(255,0,0,0)\n"
                                  "")
        self.neunum.setText("")
        self.neunum.setAlignment(QtCore.Qt.AlignCenter)
        self.neunum.setObjectName("neunum")
        self.neuper.setGeometry(QtCore.QRect(20, 70, 211, 101))
        self.neuper.setStyleSheet("color:#fff832;\n"
                                  "font-size:90px;\n"
                                  " text-shadow: 3px 2px 5px red;\n"
                                  "background-color:rgb(255,0,0,0)\n"
                                  "")
        self.neuper.setText("")
        self.neuper.setAlignment(QtCore.Qt.AlignCenter)
        self.neuper.setObjectName("neuper")
        self.frame_4.setGeometry(QtCore.QRect(540, 40, 241, 201))
        self.frame_4.setStyleSheet("background-color:rgb(255,255,255,70);\n"
                                   "border-radius: 10px ;\n"
                                   "")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_10.setGeometry(QtCore.QRect(0, 0, 241, 41))
        self.label_10.setStyleSheet("font-size:20px;\n"
                                    "font-weight:bold;\n"
                                    "background-color:red;\n"
                                    "border: 2px solid white;\n"
                                    "border-radius: 10px;")
        self.label_10.setText("")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.negnum.setGeometry(QtCore.QRect(10, 50, 221, 20))
        self.negnum.setStyleSheet("color:#000;\n"
                                  "font-size:12px;\n"
                                  "font-weight:bold;\n"
                                  "background-color:rgb(255,0,0,0)\n"
                                  "\n"
                                  "")
        self.negnum.setText("")
        self.negnum.setAlignment(QtCore.Qt.AlignCenter)
        self.negnum.setObjectName("negnum")
        self.negper.setGeometry(QtCore.QRect(20, 70, 211, 101))
        self.negper.setStyleSheet("color:red;\n"
                                  "font-size:90px;\n"
                                  "background-color:rgb(255,0,0,0)\n"
                                  "")
        self.negper.setText("")
        self.negper.setAlignment(QtCore.Qt.AlignCenter)
        self.negper.setObjectName("negper")
        #
        self.label_4.setText('Positive')
        self.label_7.setText('Neutral')
        self.label_10.setText('Negative')

        self.click_comment = QLabelClickable(self.result_frame)
        self.click_comment.setGeometry(QtCore.QRect(320, 250, 160, 20))
        self.click_comment.setStyleSheet("color:rgb(0, 0, 0)")
        self.click_comment.setObjectName("click_comment")
        self.click_comment.setCursor(Qt.PointingHandCursor)
        self.click_comment.setStyleSheet("text-decoration:underline;font-weight:bold;font-style: italic;")

        # self.result_frame.hide()
        # self.result_frame.show()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 21))
        self.menubar.setObjectName("menubar")
        self.menuGergreg = QtWidgets.QMenu(self.menubar)
        self.menuGergreg.setTitle("")
        self.menuGergreg.setObjectName("menuGergreg")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuChoose_Data_Set = QtWidgets.QMenu(self.menuFile)
        self.menuChoose_Data_Set.setObjectName("menuChoose_Data_Set")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLondon = QtWidgets.QAction(MainWindow)
        self.actionLondon.setObjectName("actionLondon")
        self.actionChennai = QtWidgets.QAction(MainWindow)
        self.actionChennai.setObjectName("actionChennai")
        self.actionHotels_Comparision = QtWidgets.QAction(MainWindow)
        self.actionHotels_Comparision.setObjectName("actionHotels_Comparision")
        self.menuChoose_Data_Set.addAction(self.actionLondon)
        self.menuChoose_Data_Set.addAction(self.actionChennai)
        self.menuTools.addAction(self.actionHotels_Comparision)

        self.menuFile.addAction(self.menuChoose_Data_Set.menuAction())

        self.menubar.addAction(self.menuGergreg.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())


        #------------------- tab comment ---------------------
        self.tab_comment = QtWidgets.QTabWidget(self.container)
        self.tab_comment.setGeometry(QtCore.QRect(20, 20, 821, 291))
        self.tab_comment.setObjectName("tab_comment")
        self.tab_comment.setStyleSheet("color:black;")
        self.tabpos = QtWidgets.QWidget()
        self.tabpos.setObjectName("tabpos")
        self.gridLayout = QtWidgets.QGridLayout(self.tabpos)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.tabpos)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaPos = QtWidgets.QWidget()
        self.scrollAreaPos.setGeometry(QtCore.QRect(0, 0, 797, 240))
        self.scrollAreaPos.setObjectName("scrollAreaPos")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaPos)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.scrollArea.setWidget(self.scrollAreaPos)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tab_comment.addTab(self.tabpos, "")
        self.tabneg = QtWidgets.QWidget()
        self.tabneg.setObjectName("tabneg")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabneg)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollneg = QtWidgets.QScrollArea(self.tabneg)
        self.scrollneg.setWidgetResizable(True)
        self.scrollneg.setObjectName("scrollneg")
        self.scrollAreaNeg = QtWidgets.QWidget()
        self.scrollAreaNeg.setGeometry(QtCore.QRect(0, 0, 577, 240))
        self.scrollAreaNeg.setObjectName("scrollAreaNeg")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaNeg)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollneg.setWidget(self.scrollAreaNeg)
        self.gridLayout_3.addWidget(self.scrollneg, 0, 0, 1, 1)
        self.tab_comment.addTab(self.tabneg, "")
        self.tabneu = QtWidgets.QWidget()
        self.tabneu.setObjectName("tabneu")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabneu)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollneu = QtWidgets.QScrollArea(self.tabneu)
        self.scrollneu.setWidgetResizable(True)
        self.scrollneu.setObjectName("scrollneu")
        self.scrollAreaNeu = QtWidgets.QWidget()
        self.scrollAreaNeu.setGeometry(QtCore.QRect(0, 0, 577, 240))
        self.scrollAreaNeu.setObjectName("scrollAreaNeu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaNeu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.scrollneu.setWidget(self.scrollAreaNeu)
        self.gridLayout_5.addWidget(self.scrollneu, 0, 0, 1, 1)
        self.tab_comment.addTab(self.tabneu, "")
        self.back = QtWidgets.QPushButton(self.container)
        self.back.setText("Back")
        self.back.setStyleSheet("color:black")
        self.back.setGeometry(QtCore.QRect(760, 360, 90, 25))

        # ------------------ end tab comment ---------------

        # -------------------- histogram interface --------------
        self.hist = QtWidgets.QFrame(self.container)
        self.hist.setGeometry(QtCore.QRect(20, 20, 821, 591))
        self.hist.setObjectName("hist")
        self.hist.setStyleSheet("color:black;")

        self.list_hotels_label = QtWidgets.QLabel(self.hist)
        self.list_hotels_label.setGeometry(QtCore.QRect(25, 0, 120, 16))
        self.list_hotels_label.setObjectName("label_2")
        self.list_hotels_label.setText("Select Hotels:")
        self.list_hotels_label.setStyleSheet("color:white; font-size:17px;font-weight:bold;")


        self.hotels_scrolls_list = QtWidgets.QScrollArea(self.hist)
        self.hotels_scrolls_list.setGeometry(QtCore.QRect(30, 20, 271, 331))
        self.hotels_scrolls_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hotels_scrolls_list.setWidgetResizable(True)
        self.hotels_scrolls_list.setObjectName("hotels_scrolls_list")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 269, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_hotels = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_hotels.setObjectName("verticalLayout")

        self.hotels_scrolls_list.setWidget(self.scrollAreaWidgetContents)

        self.groupBox = QtWidgets.QFrame(self.hist)
        self.groupBox.setGeometry(QtCore.QRect(390, 80, 301, 250))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("color:#000;")

        self.filter_label = QtWidgets.QLabel(self.groupBox)
        self.filter_label.setText("Select filter:")
        self.filter_label.setGeometry(QtCore.QRect(20, 10, 120, 15))
        self.filter_label.setObjectName("label")
        self.filter_label.setStyleSheet("color:white; font-size:17px;font-weight:bold;")

        self.filter_hist = QtWidgets.QComboBox(self.groupBox)
        self.filter_hist.setGeometry(QtCore.QRect(20, 35, 111, 31))
        self.filter_hist.setObjectName("filter_hist")
        self.filter_hist.addItems(["all","service","location","cleanliness","food","price","rooms","entertainment"])

        self.pos_hist = QtWidgets.QCheckBox("Positive Reviews", self.groupBox)
        self.pos_hist.setGeometry(QtCore.QRect(20, 80, 200, 30))
        self.pos_hist.setStyleSheet("padding-left:20px;color:#000;border-radius:10px;font-weight:bold;background-color:rgb(255,255,255,200)")
        self.pos_hist.setObjectName("pos_hist")
        self.pos_hist.setChecked(True)

        self.neg_hist = QtWidgets.QCheckBox("Negative Reviews", self.groupBox)
        self.neg_hist.setGeometry(QtCore.QRect(20, 125, 200, 30))
        self.neg_hist.setStyleSheet("padding-left:20px;color:#000;border-radius:10px;font-weight:bold;background-color:rgb(255,255,255,200)")
        self.neg_hist.setObjectName("neg_hist")

        self.show_hist = QtWidgets.QPushButton("Show Histograme", self.groupBox)
        self.show_hist.setGeometry(QtCore.QRect(20, 170, 170, 35))
        self.show_hist.setObjectName("show_hist")

        # --------------- end histograme --------------------
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        pixmap = QtGui.QPixmap("logo.png")  # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.logo.width(), self.logo.height(), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.logo.setPixmap(pixmap)  # Set the pixmap onto the label
        self.logo.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center

        self.chennai_click()

        self.submit.clicked.connect(self.get_text)

        self.actionLondon.triggered.connect(self.london_click)
        self.actionChennai.triggered.connect(self.chennai_click)

        self.actionHotels_Comparision.triggered.connect(self.show_hist_gui)

        self.enable_search.stateChanged.connect(self.enabled_changed_action)

        self.click_comment.clicked.connect(self.show_tab)

        self.back.clicked.connect(self.draw_back)

        self.show_hist.clicked.connect(self.draw_hist)

    def draw_comments(self, list_cm):
        print(list_cm[0])
        if len(list_cm[0]) > 0:
            for i in range(0,len(list_cm[0])):
                self.username = QtWidgets.QLabel(self.scrollAreaNeu)
                self.username.setGeometry(QtCore.QRect(5, 5, 341, 15))
                self.username.setObjectName("username")
                self.username.setText(list_cm[0][i][1])
                self.username.setStyleSheet("font-style:italic;font-weight:bold;color:#0a3555")
                self.comment_text = QtWidgets.QLabel(self.scrollAreaNeu)
                self.comment_text.setGeometry(QtCore.QRect(5, 5, 500, 15))
                self.comment_text.setObjectName("comment_text")
                self.comment_text.setStyleSheet("color:#00000a")
                self.comment_text.setText("\t"+list_cm[0][i][0])
                # self.comment_text.setStyleSheet("background-color:red;")
                self.gridLayout_2.addWidget(self.username)
                self.gridLayout_2.addWidget(self.comment_text)

        if len(list_cm[1]) > 0:
            for i in range(0, len(list_cm[1])):
                self.username = QtWidgets.QLabel(self.scrollAreaNeu)
                self.username.setGeometry(QtCore.QRect(5, 5, 341, 15))
                self.username.setObjectName("username")
                self.username.setText(list_cm[1][i][1])
                self.username.setStyleSheet("font-style:italic;font-weight:bold;color:#0a3555")
                self.comment_text = QtWidgets.QLabel(self.scrollAreaNeu)
                self.comment_text.setGeometry(QtCore.QRect(5, 5, 500, 15))
                self.comment_text.setObjectName("comment_text")
                self.comment_text.setStyleSheet("color:#00000a")
                self.comment_text.setText("\t" + list_cm[1][i][0])
                # self.comment_text.setStyleSheet("background-color:red;")
                self.verticalLayout.addWidget(self.username)
                self.verticalLayout.addWidget(self.comment_text)

        if len(list_cm[2]) > 0:
            for i in range(0, len(list_cm[2])):
                self.username = QtWidgets.QLabel(self.scrollAreaNeu)
                self.username.setGeometry(QtCore.QRect(5, 5, 341, 15))
                self.username.setObjectName("username")
                self.username.setText(list_cm[2][i][1])
                self.username.setStyleSheet("font-style:italic;font-weight:bold;color:#0a3555")
                self.comment_text = QtWidgets.QLabel(self.scrollAreaNeu)
                self.comment_text.setGeometry(QtCore.QRect(5, 5, 500, 15))
                self.comment_text.setObjectName("comment_text")
                self.comment_text.setStyleSheet("color:#00000a")
                self.comment_text.setText("\t" + list_cm[2][i][0])
                # self.comment_text.setStyleSheet("background-color:red;")
                self.verticalLayout_3.addWidget(self.username)
                self.verticalLayout_3.addWidget(self.comment_text)
            # for i in range(3, self.verticalLayout_3.count()):
            #      self.verticalLayout_3.itemAt(i).widget().deleteLater()

    def delete_comments(self):
        for i in range(0, self.verticalLayout_3.count()):
             self.verticalLayout_3.itemAt(i).widget().deleteLater()
        for i in range(0, self.verticalLayout.count()):
            self.verticalLayout.itemAt(i).widget().deleteLater()
        for i in range(0, self.gridLayout_2.count()):
            self.gridLayout_2.itemAt(i).widget().deleteLater()

    def draw_error(self):
        # self.error_frame.deleteLater()
        # self.error_frame.setGeometry(QtCore.QRect(30, 220, 811, 261))
        # self.error_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.error_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.error_frame.setObjectName("result_frame")

        # self.result_frame.setGeometry(QtCore.QRect(30, 220, 811, 261))
        # self.result_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.result_frame.setObjectName("result_frame")

        # self.label_4.setText('')
        # self.label_7.setText('')
        # self.label_10.setText('')
        # self.posnum.setText('')
        # self.posper.setText('')
        # self.negnum.setText('')
        # self.negper.setText('')
        # self.neunum.setText('')
        # self.neuper.setText('')
        # self.frame.setStyleSheet("display:none;visibility: hidden;")
        # self.frame_2.setStyleSheet("display:none;visibility: hidden;")
        # self.frame_3.setStyleSheet("display:none;visibility: hidden;")
        # self.posper.setStyleSheet("display:none;visibility: hidden;")
        # self.posnum.setStyleSheet("display:none;visibility: hidden;")
        # self.negper.setStyleSheet("display:none;visibility: hidden;")
        # self.negnum.setStyleSheet("display:none;visibility: hidden;")
        # self.neuper.setStyleSheet("display:none;visibility: hidden;")
        # self.neunum.setStyleSheet("display:none;visibility: hidden;")
        # self.label_4.setStyleSheet("display:none;visibility: hidden;")
        # self.label_7.setStyleSheet("display:none;visibility: hidden;")
        # self.label_10.setStyleSheet("display:none;visibility: hidden;")

        self.result_frame.hide()
        self.error_frame.show()

        self.comment_error.setGeometry(QtCore.QRect(0, 0, 800, 200))
        self.comment_error.setStyleSheet("font-size:45px;\n"
                                          "font-weight:bold;\n"
                                          "color:#fff;")
        self.comment_error.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.comment_error.setObjectName("error_result")

        self.comment_error.setText("Invalid Hotel name...!\nPlease type a correct one ")

    def draw_result(self, list_pr):

        self.error_frame.hide()
        self.result_frame.show()

        if self.all.isChecked():
            self.comment_result.setText("Toatal number of comments is " + str(list_pr[0]))
        elif self.location.isChecked():
            self.comment_result.setText("Toatal number of comments concerning location is " + str(list_pr[0]))
        elif self.service.isChecked():
            self.comment_result.setText("Toatal number of comments concerning service is " + str(list_pr[0]))
        elif self.clean.isChecked():
            self.comment_result.setText("Toatal number of comments concerning cleanliness is " + str(list_pr[0]))
        elif self.rooms.isChecked():
            self.comment_result.setText("Toatal number of comments concerning rooms is " + str(list_pr[0]))
        elif self.food.isChecked():
            self.comment_result.setText("Toatal number of comments concerning food is " + str(list_pr[0]))
        elif self.price.isChecked():
            self.comment_result.setText("Toatal number of comments concerning price is " + str(list_pr[0]))
        elif self.entertainment.isChecked():
            self.comment_result.setText("Toatal number of comments concerning entertainment is " + str(list_pr[0]))

        self.posnum.setText("{} / {} of Comments".format(list_pr[1], list_pr[0]))
        self.posper.setText("{}%".format(list_pr[4]))
        self.neunum.setText("{} / {} of Comments".format(list_pr[3], list_pr[0]))
        self.neuper.setText("{}%".format(list_pr[5]))
        self.negnum.setText("{} / {} of Comments".format(list_pr[2], list_pr[0]))
        self.negper.setText("{}%".format(list_pr[6]))

        cm = list_pr[7:10]
        self.delete_comments()
        self.draw_comments(cm)

    def get_text(self):

        file = self.file
        print(file+".....")
        list_pr = []

        service = ["service", "waiter", "waitress", "employee", "lobby", "welcome", "reception", "staff", "porter",
                   "security", "room-service", "internet", "wifi", "wi-fi"]
        location = ["place","environment", "location", "area", "position", "region", "neighborhood"]
        rooms = ["rooms", "bathrooms", "toilet", "bed", "sleep", "decoration", "room service", "views", "quiet", "chic", "comfort", "noisy"]
        food = ["food", "restaurant", "tea", "drinks", "coffee", "dinner", "lunch", "breakfast", "cuisine", "tasty", "kitchen", "buffet", "delicious"]
        cleanliness = ["clean", "concierge", "laundry", "dirty", "cleanliness", "smelly", "cleaness", "smell", "grose","stinky"]
        price = ["price", "money", "pricing", "pricey", "expensive", "cheap", "cost", "discount"]
        entertainment = ["entertainment", "pool", "bar", "theater", "party", "spectacle", "sport"]
        #
        # hotel_name = self.list_hotels.currentText()
        #
        # if hotel_name == "Choose Hotel":
        #     hotel_name = self.lineEdit.text()
        if self.enable_search.isChecked():
            hotel_name = self.lineEdit.text()
        else:
            hotel_name = self.list_hotels.currentText()

        if self.all.isChecked():
            print("all")
            list_pr = get_general_review(file, hotel_name)
        if self.service.isChecked():
            print("service")
            list_pr = get_filter_review(file, hotel_name, service)
        if self.location.isChecked():
            print("location")
            list_pr = get_filter_review(file, hotel_name, location)
        if self.clean.isChecked():
            print("cleanliness")
            list_pr = get_filter_review(file, hotel_name, cleanliness)
        if self.food.isChecked():
            print("food")
            list_pr = get_filter_review(file, hotel_name, food)
        if self.rooms.isChecked():
            print("rooms")
            list_pr = get_filter_review(file, hotel_name, rooms)
        if self.price.isChecked():
            print("price")
            list_pr = get_filter_review(file, hotel_name, price)
        if self.entertainment.isChecked():
            print("entertainment")
            list_pr = get_filter_review(file, hotel_name, entertainment)

        # print(list_pr)

        if list_pr == "error":
            self.draw_error()
        else:
            self.draw_result(list_pr)

    def london_click(self):
        print("london")
        self.file = "london_reviews.xls"
        pixmap = QtGui.QPixmap("london4.png")  # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.label.setPixmap(pixmap)  # Set the pixmap onto the label
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to
        self.all.setStyleSheet("color:#6e9ddd;font-size:14px;font-size:14px;")
        self.service.setStyleSheet("color:#6e9ddd;font-size:14px;")
        self.location.setStyleSheet("color:#62b6c6;font-size:14px;")
        self.clean.setStyleSheet("color:#62b6c6;font-size:14px;")
        self.rooms.setStyleSheet("color:#62b6b6;font-size:14px;")
        self.food.setStyleSheet("color:#62b6c6;font-size:14px;")
        self.price.setStyleSheet("color:#62b9b6;font-size:14px;")
        self.entertainment.setStyleSheet("color:#62b6b6;font-size:14px;")

        for i in range(0, self.verticalLayout_hotels.count()):
             self.verticalLayout_hotels.itemAt(i).widget().deleteLater()

        hotels = hotels_list.london_hotels[1:21]
        self.hotel_check_all = QtWidgets.QCheckBox("all", self.scrollAreaWidgetContents)
        self.verticalLayout_hotels.addWidget(self.hotel_check_all)
        for hotel in hotels:
                self.hotel_check = QtWidgets.QCheckBox(hotel, self.scrollAreaWidgetContents)
                self.verticalLayout_hotels.addWidget(self.hotel_check)

        self.hotel_check_all.clicked.connect(self.all_cheched)

        # self.comment_result.setText('')
        # self.label_4.setText('')
        # self.label_7.setText('')
        # self.label_10.setText('')
        # self.posnum.setText('')
        # self.posper.setText('')
        # self.negnum.setText('')
        # self.negper.setText('')
        # self.neunum.setText('')
        # self.neuper.setText('')
        # self.comment_result.setStyleSheet("display:none;visibility: hidden;")
        # self.frame_2.setStyleSheet("display:none;visibility: hidden;")
        # self.frame_3.setStyleSheet("display:none;visibility: hidden;")
        # self.frame_4.setStyleSheet("display:none;visibility: hidden;")
        # self.posper.setStyleSheet("display:none;visibility: hidden;")
        # self.posnum.setStyleSheet("display:none;visibility: hidden;")
        # self.negper.setStyleSheet("display:none;visibility: hidden;")
        # self.negnum.setStyleSheet("display:none;visibility: hidden;")
        # self.neuper.setStyleSheet("display:none;visibility: hidden;")
        # self.neunum.setStyleSheet("display:none;visibility: hidden;")
        # self.label_4.setStyleSheet("display:none;visibility: hidden;")
        # self.label_7.setStyleSheet("display:none;visibility: hidden;")
        # self.label_10.setStyleSheet("display:none;visibility: hidden;")
        self.error_frame.hide()
        self.result_frame.hide()
        self.hist.hide()

        self.tab_comment.hide()
        self.back.hide()
        self.search_frame.show()

        hotels = hotels_list.london_hotels
        self.list_hotels.clear()
        self.list_hotels.addItems(hotels)

    def chennai_click(self):
        print("chennai")
        self.file = "chennai_reviews.xls"
        pixmap = QtGui.QPixmap("chennai.jpg")  # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.label.setPixmap(pixmap)  # Set the pixmap onto the label
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to
        self.all.setStyleSheet("color:#012866;font-size:14px;")
        self.service.setStyleSheet("color:#012860;font-size:14px;")
        self.location.setStyleSheet("color:#012858;font-size:14px;")
        self.clean.setStyleSheet("color:#012856;font-size:14px;")
        self.rooms.setStyleSheet("color:#012852;font-size:14px;")
        self.food.setStyleSheet("color:#012848;font-size:14px;")
        self.price.setStyleSheet("color:#012846;font-size:14px;")
        self.entertainment.setStyleSheet("color:#012842;font-size:14px;")

        for i in range(0, self.verticalLayout_hotels.count()):
             self.verticalLayout_hotels.itemAt(i).widget().deleteLater()

        hotels = hotels_list.chennai_hotels[1:257]
        self.hotel_check_all = QtWidgets.QCheckBox("all", self.scrollAreaWidgetContents)
        self.verticalLayout_hotels.addWidget(self.hotel_check_all)
        for hotel in hotels:
                self.hotel_check = QtWidgets.QCheckBox(hotel, self.scrollAreaWidgetContents)
                self.verticalLayout_hotels.addWidget(self.hotel_check)

        self.hotel_check_all.clicked.connect(self.all_cheched)

        # self.comment_result.setText('')
        # self.neuper.setText('')
        # self.label_4.setText('')
        # self.label_7.setText('')
        # self.label_10.setText('')
        # self.posnum.setText('')
        # self.posper.setText('')
        # self.negnum.setText('')
        # self.negper.setText('')
        # self.neunum.setText('')
        # self.neuper.setText('')
        # self.comment_result.setStyleSheet("display:none;visibility: hidden;")
        # self.frame_2.setStyleSheet("display:none;visibility: hidden;")
        # self.frame_3.setStyleSheet("display:none;visibility: hidden;")
        # self.frame_4.setStyleSheet("display:none;visibility: hidden;")
        # self.posper.setStyleSheet("display:none;visibility: hidden;")
        # self.posnum.setStyleSheet("display:none;visibility: hidden;")
        # self.negper.setStyleSheet("display:none;visibility: hidden;")
        # self.negnum.setStyleSheet("display:none;visibility: hidden;")
        # self.neuper.setStyleSheet("display:none;visibility: hidden;")
        # self.neunum.setStyleSheet("display:none;visibility: hidden;")
        # self.label_4.setStyleSheet("display:none;visibility: hidden;")
        # self.label_7.setStyleSheet("display:none;visibility: hidden;")
        # self.label_10.setStyleSheet("display:none;visibility: hidden;")

        self.error_frame.hide()
        self.result_frame.hide()
        self.hist.hide()

        self.tab_comment.hide()
        self.back.hide()
        self.search_frame.show()

        hotels = hotels_list.chennai_hotels
        self.list_hotels.clear()
        self.list_hotels.addItems(hotels)

    def enabled_changed_action(self, state):
        if QtCore.Qt.Checked == state:
            self.lineEdit.setEnabled(True)
            self.lineEdit.setFocus(True)
            self.list_hotels.setEnabled(False)
            self.list_hotels.setStyleSheet("color:#8c8c8c;")
        else:
            self.lineEdit.setEnabled(False)
            self.list_hotels.setEnabled(True)
            self.list_hotels.setStyleSheet("color:#0a3555;")

    def show_tab(self):

        self.result_frame.hide()
        self.search_frame.hide()

        self.tab_comment.show()
        self.back.show()


        # self.back.setGeometry(QtCore.QRect(780, 350, 90, 27))
        # self.back.setObjectName("back")

    def show_hist_gui(self):

        self.search_frame.hide()
        self.result_frame.hide()

        self.hist.show()

    def draw_back(self):
        self.tab_comment.hide()

        self.result_frame.show()
        self.search_frame.show()
        self.back.hide()

    def all_cheched(self):
        if self.hotel_check_all.isChecked() == True:
            for i in range(0, self.verticalLayout_hotels.count()):
                self.verticalLayout_hotels.itemAt(i).widget().setChecked(True)
        else:
            for i in range(0, self.verticalLayout_hotels.count()):
                self.verticalLayout_hotels.itemAt(i).widget().setChecked(False)

    def draw_hist(self):
        list_checked = []
        for i in range(1, self.verticalLayout_hotels.count()):
            if self.verticalLayout_hotels.itemAt(i).widget().isChecked() == True:
                list_checked.append(self.verticalLayout_hotels.itemAt(i).widget().text())
        print(list_checked)

        filter = self.filter_hist.currentText()

        filer_pos_neg = ""
        b=False
        if self.pos_hist.isChecked() and self.neg_hist.isChecked():
            filer_pos_neg = "posneg"
            b = True
        else:
            if self.pos_hist.isChecked():
                filer_pos_neg = "positive"
                b = True
            if self.neg_hist.isChecked():
                filer_pos_neg = "negative"
                b = True

        if b and len(list_checked)>0:
            histogram(self.file, filter, filer_pos_neg, list_checked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hotel Sentiment Analyser"))
        self.click_comment.setText(_translate("MainWindow", "Display comments"))
        self.location.setText(_translate("MainWindow", "Location"))
        self.all.setText(_translate("MainWindow", "All"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Hotel Name..."))
        self.service.setText(_translate("MainWindow", "Service"))
        self.food.setText(_translate("MainWindow", "Food"))
        self.entertainment.setText(_translate("MainWindow", "Entertainment"))
        self.search.setText(_translate("MainWindow", "Search Hotel : "))
        self.label_5.setText(_translate("MainWindow", "Enable search..."))
        self.label_2.setText(_translate("MainWindow", "Fliter by :"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.clean.setText(_translate("MainWindow", "Cleanliness"))
        self.price.setText(_translate("MainWindow", "Price"))
        self.rooms.setText(_translate("MainWindow", "Rooms"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

        self.menuChoose_Data_Set.setTitle(_translate("MainWindow", "Choose Data Set"))
        self.actionLondon.setText(_translate("MainWindow", "London (Multi-language)"))
        self.actionChennai.setText(_translate("MainWindow", "Chennai (English)"))

        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionHotels_Comparision.setText(_translate("MainWindow", "Hotels Comparision"))

        self.tab_comment.setTabText(self.tab_comment.indexOf(self.tabpos), _translate("MainWindow", "Positive"))
        self.tab_comment.setTabText(self.tab_comment.indexOf(self.tabneg), _translate("MainWindow", "Negative"))
        self.tab_comment.setTabText(self.tab_comment.indexOf(self.tabneu), _translate("MainWindow", "Neutral"))


