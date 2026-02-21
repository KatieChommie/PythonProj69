# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(977, 542)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Table = QFrame(Form)
        self.Table.setObjectName(u"Table")
        self.Table.setStyleSheet(u"QFrame {\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #FFFFFF;\n"
"}")
        self.Table.setFrameShape(QFrame.StyledPanel)
        self.Table.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.Table)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.Table)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 613, 502))
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #FFFFFF;\n"
"}")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tbtn_table7 = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_table7.setObjectName(u"tbtn_table7")
        self.tbtn_table7.setMinimumSize(QSize(120, 120))
        font = QFont()
        font.setPointSize(16)
        self.tbtn_table7.setFont(font)
        self.tbtn_table7.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"img/t7.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tbtn_table7.setIcon(icon)
        self.tbtn_table7.setIconSize(QSize(150, 150))
        self.tbtn_table7.setCheckable(True)

        self.gridLayout.addWidget(self.tbtn_table7, 1, 2, 1, 1)

        self.tbtn_table2 = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_table2.setObjectName(u"tbtn_table2")
        self.tbtn_table2.setMinimumSize(QSize(120, 120))
        self.tbtn_table2.setFont(font)
        self.tbtn_table2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"img/t2.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tbtn_table2.setIcon(icon1)
        self.tbtn_table2.setIconSize(QSize(150, 150))
        self.tbtn_table2.setCheckable(True)

        self.gridLayout.addWidget(self.tbtn_table2, 0, 1, 1, 1)

        self.tbtn_table1 = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_table1.setObjectName(u"tbtn_table1")
        self.tbtn_table1.setMinimumSize(QSize(120, 120))
        self.tbtn_table1.setFont(font)
        self.tbtn_table1.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"img/t1.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tbtn_table1.setIcon(icon2)
        self.tbtn_table1.setIconSize(QSize(150, 150))
        self.tbtn_table1.setCheckable(True)
        self.tbtn_table1.setChecked(True)

        self.gridLayout.addWidget(self.tbtn_table1, 0, 0, 1, 1)

        self.tbtn_table3 = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_table3.setObjectName(u"tbtn_table3")
        self.tbtn_table3.setMinimumSize(QSize(120, 120))
        self.tbtn_table3.setFont(font)
        self.tbtn_table3.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"img/t3.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tbtn_table3.setIcon(icon3)
        self.tbtn_table3.setIconSize(QSize(150, 150))
        self.tbtn_table3.setCheckable(True)

        self.gridLayout.addWidget(self.tbtn_table3, 0, 2, 1, 1)

        self.tbtn_table5 = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_table5.setObjectName(u"tbtn_table5")
        self.tbtn_table5.setMinimumSize(QSize(120, 120))
        self.tbtn_table5.setFont(font)
        self.tbtn_table5.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"img/t5.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tbtn_table5.setIcon(icon4)
        self.tbtn_table5.setIconSize(QSize(150, 150))
        self.tbtn_table5.setCheckable(True)

        self.gridLayout.addWidget(self.tbtn_table5, 1, 0, 1, 1)

        self.tbtn_table6 = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_table6.setObjectName(u"tbtn_table6")
        self.tbtn_table6.setMinimumSize(QSize(120, 120))
        self.tbtn_table6.setFont(font)
        self.tbtn_table6.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"img/t6.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tbtn_table6.setIcon(icon5)
        self.tbtn_table6.setIconSize(QSize(150, 150))
        self.tbtn_table6.setCheckable(True)

        self.gridLayout.addWidget(self.tbtn_table6, 1, 1, 1, 1)

        self.tbtn_table4 = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_table4.setObjectName(u"tbtn_table4")
        self.tbtn_table4.setMinimumSize(QSize(120, 120))
        self.tbtn_table4.setFont(font)
        self.tbtn_table4.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"img/t4.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tbtn_table4.setIcon(icon6)
        self.tbtn_table4.setIconSize(QSize(150, 150))
        self.tbtn_table4.setCheckable(True)

        self.gridLayout.addWidget(self.tbtn_table4, 0, 3, 1, 1)

        self.tbtn_table8 = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_table8.setObjectName(u"tbtn_table8")
        self.tbtn_table8.setMinimumSize(QSize(120, 120))
        self.tbtn_table8.setFont(font)
        self.tbtn_table8.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"img/t8.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tbtn_table8.setIcon(icon7)
        self.tbtn_table8.setIconSize(QSize(150, 150))
        self.tbtn_table8.setCheckable(True)

        self.gridLayout.addWidget(self.tbtn_table8, 1, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.Table)

        self.control = QFrame(Form)
        self.control.setObjectName(u"control")
        self.control.setStyleSheet(u"QFrame {\n"
"background-color: #FFFFFF;\n"
"}")
        self.control.setFrameShape(QFrame.StyledPanel)
        self.control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.control)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.control)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_table_header = QLabel(self.frame)
        self.lbl_table_header.setObjectName(u"lbl_table_header")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.lbl_table_header.setFont(font1)

        self.verticalLayout.addWidget(self.lbl_table_header)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        self.label.setFont(font2)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(20, 20))
        self.lineEdit.setMaximumSize(QSize(400, 40))
        self.lineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.num6 = QPushButton(self.control)
        self.num6.setObjectName(u"num6")
        self.num6.setMinimumSize(QSize(50, 40))
        self.num6.setMaximumSize(QSize(60, 40))
        self.num6.setFont(font2)
        self.num6.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num6, 1, 2, 1, 1)

        self.num5 = QPushButton(self.control)
        self.num5.setObjectName(u"num5")
        self.num5.setMinimumSize(QSize(50, 40))
        self.num5.setMaximumSize(QSize(60, 40))
        self.num5.setFont(font2)
        self.num5.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num5, 1, 1, 1, 1)

        self.delete1 = QPushButton(self.control)
        self.delete1.setObjectName(u"delete1")
        self.delete1.setMinimumSize(QSize(50, 40))
        self.delete1.setMaximumSize(QSize(60, 40))
        self.delete1.setFont(font2)
        self.delete1.setStyleSheet(u"QPushButton {\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #FFFFFF;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"img/backspace.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete1.setIcon(icon8)
        self.delete1.setIconSize(QSize(35, 35))

        self.gridLayout_4.addWidget(self.delete1, 3, 2, 1, 1)

        self.num0 = QPushButton(self.control)
        self.num0.setObjectName(u"num0")
        self.num0.setMinimumSize(QSize(50, 40))
        self.num0.setMaximumSize(QSize(60, 40))
        self.num0.setFont(font2)
        self.num0.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num0, 3, 1, 1, 1)

        self.num4 = QPushButton(self.control)
        self.num4.setObjectName(u"num4")
        self.num4.setMinimumSize(QSize(50, 40))
        self.num4.setMaximumSize(QSize(60, 40))
        self.num4.setFont(font2)
        self.num4.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num4, 1, 0, 1, 1)

        self.num3 = QPushButton(self.control)
        self.num3.setObjectName(u"num3")
        self.num3.setMinimumSize(QSize(50, 40))
        self.num3.setMaximumSize(QSize(60, 40))
        self.num3.setFont(font2)
        self.num3.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num3, 0, 2, 1, 1)

        self.num1 = QPushButton(self.control)
        self.num1.setObjectName(u"num1")
        self.num1.setMinimumSize(QSize(50, 40))
        self.num1.setMaximumSize(QSize(60, 40))
        self.num1.setFont(font2)
        self.num1.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num1, 0, 0, 1, 1)

        self.num2 = QPushButton(self.control)
        self.num2.setObjectName(u"num2")
        self.num2.setMinimumSize(QSize(50, 40))
        self.num2.setMaximumSize(QSize(60, 40))
        self.num2.setFont(font2)
        self.num2.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num2, 0, 1, 1, 1)

        self.num8 = QPushButton(self.control)
        self.num8.setObjectName(u"num8")
        self.num8.setMinimumSize(QSize(50, 40))
        self.num8.setMaximumSize(QSize(60, 40))
        self.num8.setFont(font2)
        self.num8.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num8, 2, 1, 1, 1)

        self.num9 = QPushButton(self.control)
        self.num9.setObjectName(u"num9")
        self.num9.setMinimumSize(QSize(50, 40))
        self.num9.setMaximumSize(QSize(60, 40))
        self.num9.setFont(font2)
        self.num9.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num9, 2, 2, 1, 1)

        self.num7 = QPushButton(self.control)
        self.num7.setObjectName(u"num7")
        self.num7.setMinimumSize(QSize(50, 40))
        self.num7.setMaximumSize(QSize(60, 40))
        self.num7.setFont(font2)
        self.num7.setStyleSheet(u"QPushButton {\n"
"background-color: #FAF9F6;\n"
"border: 1px solid #000000;\n"
"}")

        self.gridLayout_4.addWidget(self.num7, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.frame_3 = QFrame(self.control)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(10, 10))
        self.frame_3.setMaximumSize(QSize(10, 10))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.pbtn_confirm = QPushButton(self.control)
        self.pbtn_confirm.setObjectName(u"pbtn_confirm")
        self.pbtn_confirm.setMinimumSize(QSize(50, 50))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.pbtn_confirm.setFont(font3)
        self.pbtn_confirm.setStyleSheet(u"QPushButton {\n"
"background-color: #FFF59D;\n"
"border: 1px solid #FFF59D;\n"
"}")

        self.verticalLayout_2.addWidget(self.pbtn_confirm)


        self.horizontalLayout.addWidget(self.control)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tbtn_table7.setText(QCoreApplication.translate("Form", u"7", None))
        self.tbtn_table2.setText(QCoreApplication.translate("Form", u"2", None))
        self.tbtn_table1.setText(QCoreApplication.translate("Form", u"1", None))
#if QT_CONFIG(shortcut)
        self.tbtn_table1.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.tbtn_table3.setText(QCoreApplication.translate("Form", u"3", None))
        self.tbtn_table5.setText(QCoreApplication.translate("Form", u"5", None))
        self.tbtn_table6.setText(QCoreApplication.translate("Form", u"6", None))
        self.tbtn_table4.setText(QCoreApplication.translate("Form", u"4", None))
        self.tbtn_table8.setText(QCoreApplication.translate("Form", u"8", None))
        self.lbl_table_header.setText(QCoreApplication.translate("Form", u"\u0e20\u0e32\u0e22\u0e43\u0e19 \u0e42\u0e15\u0e4a\u0e30\u0e17\u0e35\u0e48 1", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"2", None))
        self.num6.setText(QCoreApplication.translate("Form", u"6", None))
        self.num5.setText(QCoreApplication.translate("Form", u"5", None))
        self.num0.setText(QCoreApplication.translate("Form", u"0", None))
        self.num4.setText(QCoreApplication.translate("Form", u"4", None))
        self.num3.setText(QCoreApplication.translate("Form", u"3", None))
        self.num1.setText(QCoreApplication.translate("Form", u"1", None))
        self.num2.setText(QCoreApplication.translate("Form", u"2", None))
        self.num8.setText(QCoreApplication.translate("Form", u"8", None))
        self.num9.setText(QCoreApplication.translate("Form", u"9", None))
        self.num7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pbtn_confirm.setText(QCoreApplication.translate("Form", u"\u0e2a\u0e31\u0e48\u0e07\u0e2d\u0e32\u0e2b\u0e32\u0e23", None))
    # retranslateUi

