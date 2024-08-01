# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compare_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QGroupBox, QHeaderView, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_CompareWindow(object):
    def setupUi(self, CompareWindow):
        if not CompareWindow.objectName():
            CompareWindow.setObjectName(u"CompareWindow")
        CompareWindow.resize(543, 814)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CompareWindow.sizePolicy().hasHeightForWidth())
        CompareWindow.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(CompareWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_modes = QGroupBox(CompareWindow)
        self.gb_modes.setObjectName(u"gb_modes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gb_modes.sizePolicy().hasHeightForWidth())
        self.gb_modes.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.gb_modes)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tw_modes = QTreeWidget(self.gb_modes)
        self.tw_modes.setObjectName(u"tw_modes")
        self.tw_modes.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.tw_modes.setAlternatingRowColors(True)
        self.tw_modes.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tw_modes.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tw_modes.setAnimated(True)

        self.verticalLayout_2.addWidget(self.tw_modes)


        self.gridLayout.addWidget(self.gb_modes, 0, 0, 2, 1)

        self.gb_Filters = QGroupBox(CompareWindow)
        self.gb_Filters.setObjectName(u"gb_Filters")
        sizePolicy1.setHeightForWidth(self.gb_Filters.sizePolicy().hasHeightForWidth())
        self.gb_Filters.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.gb_Filters)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tw_filters = QTreeWidget(self.gb_Filters)
        __qtreewidgetitem = QTreeWidgetItem(self.tw_filters)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        self.tw_filters.setObjectName(u"tw_filters")
        sizePolicy1.setHeightForWidth(self.tw_filters.sizePolicy().hasHeightForWidth())
        self.tw_filters.setSizePolicy(sizePolicy1)
        self.tw_filters.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.tw_filters.setAlternatingRowColors(True)
        self.tw_filters.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tw_filters.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tw_filters.setAnimated(True)

        self.verticalLayout_3.addWidget(self.tw_filters)

        self.pb_buildTree = QPushButton(self.gb_Filters)
        self.pb_buildTree.setObjectName(u"pb_buildTree")

        self.verticalLayout_3.addWidget(self.pb_buildTree)

        self.pb_clearTree = QPushButton(self.gb_Filters)
        self.pb_clearTree.setObjectName(u"pb_clearTree")

        self.verticalLayout_3.addWidget(self.pb_clearTree)


        self.gridLayout.addWidget(self.gb_Filters, 0, 1, 1, 1)

        self.gp_actions = QGroupBox(CompareWindow)
        self.gp_actions.setObjectName(u"gp_actions")
        sizePolicy1.setHeightForWidth(self.gp_actions.sizePolicy().hasHeightForWidth())
        self.gp_actions.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.gp_actions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tw_actions = QTreeWidget(self.gp_actions)
        __qtreewidgetitem1 = QTreeWidgetItem(self.tw_actions)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.tw_actions)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.tw_actions)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.tw_actions.setObjectName(u"tw_actions")
        self.tw_actions.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.tw_actions.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout.addWidget(self.tw_actions)


        self.gridLayout.addWidget(self.gp_actions, 1, 1, 1, 1)

        self.pb_compare = QPushButton(CompareWindow)
        self.pb_compare.setObjectName(u"pb_compare")

        self.gridLayout.addWidget(self.pb_compare, 3, 0, 1, 2)


        self.retranslateUi(CompareWindow)

        QMetaObject.connectSlotsByName(CompareWindow)
    # setupUi

    def retranslateUi(self, CompareWindow):
        CompareWindow.setWindowTitle(QCoreApplication.translate("CompareWindow", u"Dialog", None))
        self.gb_modes.setTitle(QCoreApplication.translate("CompareWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u0440\u0435\u0436\u0438\u043c\u044b", None))
        ___qtreewidgetitem = self.tw_modes.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("CompareWindow", u"\u0411\u043e\u0440\u0442", None));
        self.gb_Filters.setTitle(QCoreApplication.translate("CompareWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b", None))
        ___qtreewidgetitem1 = self.tw_filters.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("CompareWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None));

        __sortingEnabled = self.tw_filters.isSortingEnabled()
        self.tw_filters.setSortingEnabled(False)
        ___qtreewidgetitem2 = self.tw_filters.topLevelItem(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("CompareWindow", u"\u041f\u043e\u0434\u0441\u0438\u0441\u0442\u0435\u043c\u0430", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("CompareWindow", u"\u0412\u0438\u0431\u0440\u0430\u0446\u0438\u044f", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("CompareWindow", u"\u0414\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None));
        self.tw_filters.setSortingEnabled(__sortingEnabled)

        self.pb_buildTree.setText(QCoreApplication.translate("CompareWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0434\u0435\u0440\u0435\u0432\u043e", None))
        self.pb_clearTree.setText(QCoreApplication.translate("CompareWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0434\u0435\u0440\u0435\u0432\u043e", None))
        self.gp_actions.setTitle(QCoreApplication.translate("CompareWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        ___qtreewidgetitem5 = self.tw_actions.headerItem()
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("CompareWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None));

        __sortingEnabled1 = self.tw_actions.isSortingEnabled()
        self.tw_actions.setSortingEnabled(False)
        ___qtreewidgetitem6 = self.tw_actions.topLevelItem(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("CompareWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0441 \u0441\u0435\u0433\u043c\u0435\u043d\u0442\u0430\u043c\u0438", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem6.child(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("CompareWindow", u"\u041e\u0441\u0440\u0435\u0434\u043d\u044f\u0442\u044c", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem6.child(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("CompareWindow", u"\u0421\u0442\u0440\u043e\u0438\u0442\u044c \u043d\u0435\u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem6.child(2)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("CompareWindow", u"\u0421\u0443\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None));
        ___qtreewidgetitem10 = self.tw_actions.topLevelItem(1)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("CompareWindow", u"\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("CompareWindow", u"\u041f\u0440\u043e\u0441\u0441\u0443\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0433\u0440\u0443\u043f\u043f\u044b", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem10.child(1)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("CompareWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0441\u0440\u0435\u0434\u043d\u0438\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 ", None));
        ___qtreewidgetitem13 = self.tw_actions.topLevelItem(2)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("CompareWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0430", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("CompareWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0438\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None));
        self.tw_actions.setSortingEnabled(__sortingEnabled1)

        self.pb_compare.setText(QCoreApplication.translate("CompareWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c", None))
    # retranslateUi

