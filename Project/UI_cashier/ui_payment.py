# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'payment.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(745, 475)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_left = QFrame(Dialog)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setStyleSheet(u"QWidget {\n"
"background-color: #FFFFFF;\n"
"}")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_left)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_order = QTableWidget(self.frame_left)
        if (self.table_order.columnCount() < 3):
            self.table_order.setColumnCount(3)
        font = QFont()
        font.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.table_order.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.table_order.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.table_order.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_order.setObjectName(u"table_order")

        self.verticalLayout.addWidget(self.table_order)

        self.table_summary = QTableWidget(self.frame_left)
        if (self.table_summary.rowCount() < 3):
            self.table_summary.setRowCount(3)
        font1 = QFont()
        font1.setPointSize(11)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.table_summary.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.table_summary.setVerticalHeaderItem(1, __qtablewidgetitem4)
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.table_summary.setVerticalHeaderItem(2, __qtablewidgetitem5)
        self.table_summary.setObjectName(u"table_summary")

        self.verticalLayout.addWidget(self.table_summary)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.frame_left)

        self.frame_right = QFrame(Dialog)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setMinimumSize(QSize(400, 400))
        self.frame_right.setStyleSheet(u"QFrame {\n"
"background-color: #FFFFFF;\n"
"}")
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_right)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(50, 50))
        self.frame.setStyleSheet(u"QFrame {\n"
"        background-color: #079757;\n"
"        border-radius: 10px;\n"
"        padding: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_total = QLabel(self.frame)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setMinimumSize(QSize(20, 0))
        self.label_total.setStyleSheet(u"QLabel {        \n"
"color: white;\n"
"font-size: 65px;\n"
"font-weight: bold;\n"
"qproperty-alignment: 'AlignVCenter | AlignRight';\n"
"padding-right: 0px;\n"
"}")

        self.verticalLayout_3.addWidget(self.label_total)


        self.verticalLayout_2.addWidget(self.frame)

        self.lbl_qr = QLabel(self.frame_right)
        self.lbl_qr.setObjectName(u"lbl_qr")

        self.verticalLayout_2.addWidget(self.lbl_qr)

        self.pbtn_back = QPushButton(self.frame_right)
        self.pbtn_back.setObjectName(u"pbtn_back")
        self.pbtn_back.setMinimumSize(QSize(40, 40))
        font3 = QFont()
        font3.setPointSize(14)
        self.pbtn_back.setFont(font3)
        self.pbtn_back.setStyleSheet(u"QPushButton {\n"
"background-color: #E1E2E4;\n"
"border: 1px solid #E1E2E4;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pbtn_back)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 6)
        self.verticalLayout_2.setStretch(2, 3)

        self.horizontalLayout.addWidget(self.frame_right)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.table_order.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23", None));
        ___qtablewidgetitem1 = self.table_order.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u0e08\u0e33\u0e19\u0e27\u0e19", None));
        ___qtablewidgetitem2 = self.table_order.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u0e22\u0e2d\u0e14\u0e23\u0e27\u0e21 (\u0e1a\u0e32\u0e17)", None));
        ___qtablewidgetitem3 = self.table_summary.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u0e2a\u0e48\u0e27\u0e19\u0e25\u0e14\u0e17\u0e49\u0e32\u0e22\u0e1a\u0e34\u0e25", None));
        ___qtablewidgetitem4 = self.table_summary.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"VAT (7%)", None));
        ___qtablewidgetitem5 = self.table_summary.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u0e23\u0e32\u0e04\u0e32\u0e23\u0e27\u0e21", None));
        self.label_total.setText(QCoreApplication.translate("Dialog", u"384.00", None))
        self.lbl_qr.setText("")
        self.pbtn_back.setText(QCoreApplication.translate("Dialog", u"\u0e22\u0e49\u0e2d\u0e19\u0e01\u0e25\u0e31\u0e1a", None))
    # retranslateUi

