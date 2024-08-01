# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHeaderView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(786, 711)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks|QMainWindow.DockOption.ForceTabbedDocks|QMainWindow.DockOption.VerticalTabs)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_Borts = QGroupBox(self.centralwidget)
        self.gb_Borts.setObjectName(u"gb_Borts")
        self.verticalLayout = QVBoxLayout(self.gb_Borts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_addBort = QPushButton(self.gb_Borts)
        self.pb_addBort.setObjectName(u"pb_addBort")

        self.verticalLayout.addWidget(self.pb_addBort)

        self.pb_removeBort = QPushButton(self.gb_Borts)
        self.pb_removeBort.setObjectName(u"pb_removeBort")

        self.verticalLayout.addWidget(self.pb_removeBort)

        self.tw_borts = QTreeWidget(self.gb_Borts)
        self.tw_borts.setObjectName(u"tw_borts")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_borts.sizePolicy().hasHeightForWidth())
        self.tw_borts.setSizePolicy(sizePolicy)
        self.tw_borts.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.tw_borts.setAlternatingRowColors(True)
        self.tw_borts.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tw_borts.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        self.verticalLayout.addWidget(self.tw_borts)

        self.pb_createGroup = QPushButton(self.gb_Borts)
        self.pb_createGroup.setObjectName(u"pb_createGroup")

        self.verticalLayout.addWidget(self.pb_createGroup)


        self.gridLayout.addWidget(self.gb_Borts, 0, 0, 2, 1)

        self.gb_flights = QGroupBox(self.centralwidget)
        self.gb_flights.setObjectName(u"gb_flights")
        self.verticalLayout_2 = QVBoxLayout(self.gb_flights)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tw_groupsFlights = QTreeWidget(self.gb_flights)
        self.tw_groupsFlights.setObjectName(u"tw_groupsFlights")
        self.tw_groupsFlights.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tw_groupsFlights.setAlternatingRowColors(True)
        self.tw_groupsFlights.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.tw_groupsFlights.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tw_groupsFlights.setAnimated(True)

        self.verticalLayout_2.addWidget(self.tw_groupsFlights)

        self.pb_delGroupOrFlight = QPushButton(self.gb_flights)
        self.pb_delGroupOrFlight.setObjectName(u"pb_delGroupOrFlight")

        self.verticalLayout_2.addWidget(self.pb_delGroupOrFlight)


        self.gridLayout.addWidget(self.gb_flights, 0, 2, 1, 1)

        self.pb_compare = QPushButton(self.centralwidget)
        self.pb_compare.setObjectName(u"pb_compare")

        self.gridLayout.addWidget(self.pb_compare, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 786, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gb_Borts.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0431\u043e\u0440\u0442\u043e\u0432 \u0438 \u043f\u043e\u043b\u0435\u0442\u043e\u0432", None))
        self.pb_addBort.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0431\u043e\u0440\u0442", None))
        self.pb_removeBort.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0431\u043e\u0440\u0442", None))
        ___qtreewidgetitem = self.tw_borts.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043b\u0435\u0442\u0430", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0435\u0442\u044b", None));
        self.pb_createGroup.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        self.gb_flights.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b \u043f\u043e\u043b\u0435\u0442\u043e\u0432 \u0434\u043b\u044f \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        ___qtreewidgetitem1 = self.tw_groupsFlights.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0435\u0442\u044b", None));
        self.pb_delGroupOrFlight.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pb_compare.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c", None))
    # retranslateUi

