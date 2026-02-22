# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 640)
        MainWindow.setMaximumSize(QSize(360, 640))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget_2 = QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"")
        self.Profile_shop = QWidget(self.page_home)
        self.Profile_shop.setObjectName(u"Profile_shop")
        self.Profile_shop.setGeometry(QRect(0, 0, 341, 161))
        self.Profile_shop.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_background_shop = QLabel(self.Profile_shop)
        self.label_background_shop.setObjectName(u"label_background_shop")
        self.label_background_shop.setGeometry(QRect(0, -80, 341, 181))
        self.label_background_shop.setPixmap(QPixmap(u"food_steak/image/background.jpg"))
        self.label_background_shop.setScaledContents(True)
        self.label_name_shop = QLabel(self.Profile_shop)
        self.label_name_shop.setObjectName(u"label_name_shop")
        self.label_name_shop.setGeometry(QRect(0, 130, 341, 20))
        self.label_name_shop.setStyleSheet(u"font: 12pt \"Arial\";")
        self.label_name_shop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_logo_shop = QLabel(self.Profile_shop)
        self.label_logo_shop.setObjectName(u"label_logo_shop")
        self.label_logo_shop.setGeometry(QRect(120, 30, 100, 100))
        self.label_logo_shop.setMinimumSize(QSize(100, 100))
        self.label_logo_shop.setMaximumSize(QSize(120, 120))
        self.label_logo_shop.setStyleSheet(u"background: transparent;\n"
"border: none;")
        self.label_logo_shop.setFrameShape(QFrame.Shape.NoFrame)
        self.label_logo_shop.setFrameShadow(QFrame.Shadow.Plain)
        self.label_logo_shop.setPixmap(QPixmap(u"food_steak/image/logo.PNG"))
        self.label_logo_shop.setScaledContents(True)
        self.label_logo_shop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_number_table = QLabel(self.Profile_shop)
        self.label_number_table.setObjectName(u"label_number_table")
        self.label_number_table.setGeometry(QRect(10, 10, 71, 21))
        self.label_number_table.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.category = QWidget(self.page_home)
        self.category.setObjectName(u"category")
        self.category.setGeometry(QRect(0, 160, 341, 61))
        self.category.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #e53935;   /* \u0e0a\u0e35\u0e49\u0e40\u0e21\u0e32\u0e2a\u0e4c\u0e41\u0e25\u0e49\u0e27\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e2a\u0e35 */\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.category)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea_category = QScrollArea(self.category)
        self.scrollArea_category.setObjectName(u"scrollArea_category")
        self.scrollArea_category.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u0e41\u0e16\u0e1a\u0e1e\u0e37\u0e49\u0e19\u0e2b\u0e25\u0e31\u0e07 */\n"
"QScrollBar:horizontal {\n"
"    height: 2px;                /* \u0e1a\u0e32\u0e07 \u0e46 */\n"
"    background: transparent;    /* \u0e44\u0e21\u0e48\u0e21\u0e35\u0e1e\u0e37\u0e49\u0e19\u0e2b\u0e25\u0e31\u0e07 */\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* \u0e15\u0e31\u0e27\u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19 */\n"
"QScrollBar::handle:horizontal {\n"
"    background: #cfcfcf;        /* \u0e2a\u0e35\u0e40\u0e17\u0e32\u0e2d\u0e48\u0e2d\u0e19 */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* \u0e15\u0e2d\u0e19 hover */\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #a8a8a8;\n"
"}\n"
"\n"
"/* \u0e0b\u0e48\u0e2d\u0e19\u0e1b\u0e38\u0e48\u0e21\u0e25\u0e39\u0e01\u0e28\u0e23 */\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"    background: none;\n"
"}\n"
"\n"
"/* \u0e1e\u0e37\u0e49\u0e19\u0e17\u0e35\u0e48\u0e27\u0e48"
                        "\u0e32\u0e07 */\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"")
        self.scrollArea_category.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_category.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea_category.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_category.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_category.setWidgetResizable(True)
        self.scrollAreaWidgetContents_category = QWidget()
        self.scrollAreaWidgetContents_category.setObjectName(u"scrollAreaWidgetContents_category")
        self.scrollAreaWidgetContents_category.setGeometry(QRect(0, 0, 505, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_category)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_all = QPushButton(self.scrollAreaWidgetContents_category)
        self.btn_all.setObjectName(u"btn_all")

        self.horizontalLayout_4.addWidget(self.btn_all)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.btn_steak = QPushButton(self.scrollAreaWidgetContents_category)
        self.btn_steak.setObjectName(u"btn_steak")

        self.horizontalLayout_4.addWidget(self.btn_steak)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.btn_burger = QPushButton(self.scrollAreaWidgetContents_category)
        self.btn_burger.setObjectName(u"btn_burger")

        self.horizontalLayout_4.addWidget(self.btn_burger)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)

        self.btn_pasta = QPushButton(self.scrollAreaWidgetContents_category)
        self.btn_pasta.setObjectName(u"btn_pasta")

        self.horizontalLayout_4.addWidget(self.btn_pasta)

        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_13)

        self.btn_salad = QPushButton(self.scrollAreaWidgetContents_category)
        self.btn_salad.setObjectName(u"btn_salad")

        self.horizontalLayout_4.addWidget(self.btn_salad)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.btn_snack = QPushButton(self.scrollAreaWidgetContents_category)
        self.btn_snack.setObjectName(u"btn_snack")

        self.horizontalLayout_4.addWidget(self.btn_snack)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.btn_drink = QPushButton(self.scrollAreaWidgetContents_category)
        self.btn_drink.setObjectName(u"btn_drink")

        self.horizontalLayout_4.addWidget(self.btn_drink)

        self.horizontalSpacer_16 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)

        self.scrollArea_category.setWidget(self.scrollAreaWidgetContents_category)

        self.horizontalLayout_2.addWidget(self.scrollArea_category)

        self.widget_home_to_cart = QWidget(self.page_home)
        self.widget_home_to_cart.setObjectName(u"widget_home_to_cart")
        self.widget_home_to_cart.setGeometry(QRect(0, 560, 341, 61))
        self.btn_home_to_cart = QPushButton(self.widget_home_to_cart)
        self.btn_home_to_cart.setObjectName(u"btn_home_to_cart")
        self.btn_home_to_cart.setGeometry(QRect(10, 10, 321, 34))
        self.btn_home_to_cart.setMinimumSize(QSize(0, 34))
        self.btn_home_to_cart.setMaximumSize(QSize(16777215, 34))
        self.btn_home_to_cart.setStyleSheet(u"QPushButton {\n"
"    background-color: #ef5350;    \n"
"    color: white;               \n"
"    border: none;                 \n"
"    border-radius: 6px;      \n"
"    padding: 6px 15px;          \n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d32f2f;   \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#f3ff70;    \n"
"    color: black;\n"
"}")
        self.scrollArea_all = QScrollArea(self.page_home)
        self.scrollArea_all.setObjectName(u"scrollArea_all")
        self.scrollArea_all.setGeometry(QRect(10, 230, 320, 321))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_all.sizePolicy().hasHeightForWidth())
        self.scrollArea_all.setSizePolicy(sizePolicy)
        self.scrollArea_all.setMinimumSize(QSize(320, 0))
        self.scrollArea_all.setMaximumSize(QSize(320, 16777215))
        self.scrollArea_all.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 5px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cfcfcf;\n"
"    border-radius: 3px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #a8a8a8;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea_all.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_all.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea_all.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_all.setWidgetResizable(True)
        self.scrollAreaWidgetContents_all = QWidget()
        self.scrollAreaWidgetContents_all.setObjectName(u"scrollAreaWidgetContents_all")
        self.scrollAreaWidgetContents_all.setGeometry(QRect(0, 0, 320, 321))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_all)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_all_title = QLabel(self.scrollAreaWidgetContents_all)
        self.label_all_title.setObjectName(u"label_all_title")
        self.label_all_title.setStyleSheet(u"font: 11pt \"Arial\";")

        self.verticalLayout_15.addWidget(self.label_all_title)

        self.gridLayout_all_item = QGridLayout()
        self.gridLayout_all_item.setObjectName(u"gridLayout_all_item")

        self.verticalLayout_15.addLayout(self.gridLayout_all_item)

        self.scrollArea_all.setWidget(self.scrollAreaWidgetContents_all)
        self.stackedWidget_2.addWidget(self.page_home)
        self.page_detail = QWidget()
        self.page_detail.setObjectName(u"page_detail")
        self.verticalLayout = QVBoxLayout(self.page_detail)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_detail_2 = QWidget(self.page_detail)
        self.widget_detail_2.setObjectName(u"widget_detail_2")
        self.widget_header_detail = QWidget(self.widget_detail_2)
        self.widget_header_detail.setObjectName(u"widget_header_detail")
        self.widget_header_detail.setGeometry(QRect(0, 0, 321, 261))
        self.label_food_image = QLabel(self.widget_header_detail)
        self.label_food_image.setObjectName(u"label_food_image")
        self.label_food_image.setGeometry(QRect(0, 0, 321, 301))
        self.label_food_image.setScaledContents(True)
        self.btn_detail_to_home = QPushButton(self.widget_header_detail)
        self.btn_detail_to_home.setObjectName(u"btn_detail_to_home")
        self.btn_detail_to_home.setGeometry(QRect(10, 10, 31, 31))
        self.btn_detail_to_home.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.btn_detail_to_home.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #848484;\n"
"}")
        self.widget_message = QWidget(self.widget_detail_2)
        self.widget_message.setObjectName(u"widget_message")
        self.widget_message.setGeometry(QRect(0, 250, 321, 281))
        self.widget_message.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.label_food_name = QLabel(self.widget_message)
        self.label_food_name.setObjectName(u"label_food_name")
        self.label_food_name.setGeometry(QRect(20, 20, 281, 16))
        self.label_food_name.setStyleSheet(u"font: 700 11pt \"Arial\";")
        self.label_food_price = QLabel(self.widget_message)
        self.label_food_price.setObjectName(u"label_food_price")
        self.label_food_price.setGeometry(QRect(30, 50, 261, 16))
        self.label_food_price.setStyleSheet(u"font: 10pt \"Segoe UI\";\n"
"font: 600 9pt \"Segoe UI\";")
        self.frame_line_detail = QFrame(self.widget_message)
        self.frame_line_detail.setObjectName(u"frame_line_detail")
        self.frame_line_detail.setGeometry(QRect(10, 90, 301, 1))
        self.frame_line_detail.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"    background-color: #dddddd; \n"
"    max-height: 1px;\n"
"}")
        self.frame_line_detail.setFrameShape(QFrame.Shape.HLine)
        self.frame_line_detail.setFrameShadow(QFrame.Shadow.Plain)
        self.label_note_description_2 = QLabel(self.widget_message)
        self.label_note_description_2.setObjectName(u"label_note_description_2")
        self.label_note_description_2.setGeometry(QRect(20, 110, 101, 16))
        self.label_note_description_2.setStyleSheet(u"font: 600 10pt \"Segoe UI\";")
        self.label_note_description = QLabel(self.widget_message)
        self.label_note_description.setObjectName(u"label_note_description")
        self.label_note_description.setGeometry(QRect(20, 140, 261, 16))
        self.textEdit_message = QTextEdit(self.widget_message)
        self.textEdit_message.setObjectName(u"textEdit_message")
        self.textEdit_message.setGeometry(QRect(10, 180, 301, 61))
        self.textEdit_message.setStyleSheet(u"QTextEdit {\n"
"    border: 1px solid #dddddd;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    background-color: white;\n"
"}")
        self.widget_add_to_cart = QWidget(self.widget_detail_2)
        self.widget_add_to_cart.setObjectName(u"widget_add_to_cart")
        self.widget_add_to_cart.setGeometry(QRect(0, 530, 321, 71))
        self.horizontalLayout = QHBoxLayout(self.widget_add_to_cart)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_delete = QPushButton(self.widget_add_to_cart)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMaximumSize(QSize(70, 35))
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE5E3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E74C3C;\n"
"    color: white;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_delete)

        self.label_qty_list = QLabel(self.widget_add_to_cart)
        self.label_qty_list.setObjectName(u"label_qty_list")
        self.label_qty_list.setMaximumSize(QSize(8, 20))
        self.label_qty_list.setStyleSheet(u"font: 600 10pt \"Segoe UI\";")
        self.label_qty_list.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_qty_list)

        self.btn_add = QPushButton(self.widget_add_to_cart)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMaximumSize(QSize(70, 35))
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFE5E3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E74C3C;\n"
"    color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_add)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_add_to_cart = QPushButton(self.widget_add_to_cart)
        self.btn_add_to_cart.setObjectName(u"btn_add_to_cart")
        self.btn_add_to_cart.setMinimumSize(QSize(160, 34))
        self.btn_add_to_cart.setMaximumSize(QSize(160, 34))
        self.btn_add_to_cart.setStyleSheet(u"QPushButton {\n"
"    background-color: #ef5350;  \n"
"    color: white;             \n"
"    border: none;            \n"
"    border-radius: 5px;    \n"
"    padding: 6px 15px;       \n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d32f2f; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#f3ff70; \n"
"    color: black;\n"
"}\n"
"")
        self.btn_add_to_cart.setIconSize(QSize(16, 16))
        self.btn_add_to_cart.setAutoRepeatDelay(300)

        self.horizontalLayout.addWidget(self.btn_add_to_cart)


        self.verticalLayout.addWidget(self.widget_detail_2)

        self.stackedWidget_2.addWidget(self.page_detail)
        self.page_cart = QWidget()
        self.page_cart.setObjectName(u"page_cart")
        self.widget_header_list = QWidget(self.page_cart)
        self.widget_header_list.setObjectName(u"widget_header_list")
        self.widget_header_list.setGeometry(QRect(0, -1, 341, 61))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_header_list.sizePolicy().hasHeightForWidth())
        self.widget_header_list.setSizePolicy(sizePolicy1)
        self.widget_header_list.setStyleSheet(u"background-color: rgb(39, 139, 64);\n"
"border-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.widget_header_list)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_17 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_17)

        self.btn_cart_to_home = QPushButton(self.widget_header_list)
        self.btn_cart_to_home.setObjectName(u"btn_cart_to_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_cart_to_home.sizePolicy().hasHeightForWidth())
        self.btn_cart_to_home.setSizePolicy(sizePolicy2)
        self.btn_cart_to_home.setMinimumSize(QSize(30, 30))
        self.btn_cart_to_home.setMaximumSize(QSize(30, 30))
        self.btn_cart_to_home.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 14px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #848484;\n"
"}")
        self.btn_cart_to_home.setIconSize(QSize(16, 18))

        self.horizontalLayout_3.addWidget(self.btn_cart_to_home)

        self.horizontalSpacer_8 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.lable_menulist = QLabel(self.widget_header_list)
        self.lable_menulist.setObjectName(u"lable_menulist")
        self.lable_menulist.setStyleSheet(u"font: 700 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.lable_menulist.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lable_menulist)

        self.horizontalSpacer_9 = QSpacerItem(85, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.scrollArea = QScrollArea(self.page_cart)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QRect(-3, 60, 341, 441))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 5px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cfcfcf;\n"
"    border-radius: 3px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #a8a8a8;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 341, 441))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_cart = QVBoxLayout()
        self.verticalLayout_cart.setObjectName(u"verticalLayout_cart")

        self.verticalLayout_3.addLayout(self.verticalLayout_cart)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget_6 = QWidget(self.page_cart)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 510, 343, 101))
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(18, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_total_item = QLabel(self.widget_6)
        self.label_total_item.setObjectName(u"label_total_item")
        self.label_total_item.setStyleSheet(u"font: 600 9pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_total_item)

        self.horizontalSpacer_2 = QSpacerItem(168, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.label_total_price = QLabel(self.widget_6)
        self.label_total_price.setObjectName(u"label_total_price")
        self.label_total_price.setStyleSheet(u"font: 600 9pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_total_price)

        self.horizontalSpacer_4 = QSpacerItem(18, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.btn_checkout = QPushButton(self.widget_6)
        self.btn_checkout.setObjectName(u"btn_checkout")
        self.btn_checkout.setMinimumSize(QSize(0, 34))
        self.btn_checkout.setMaximumSize(QSize(16777215, 34))
        self.btn_checkout.setStyleSheet(u"QPushButton {\n"
"    background-color: #ef5350;    \n"
"    color: white;               \n"
"    border: none;                 \n"
"    border-radius: 6px;      \n"
"    padding: 6px 15px;          \n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d32f2f;   \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#f3ff70;    \n"
"    color: black;\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_checkout)

        self.horizontalSpacer_7 = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.frame_line_botton = QFrame(self.page_cart)
        self.frame_line_botton.setObjectName(u"frame_line_botton")
        self.frame_line_botton.setGeometry(QRect(0, 500, 341, 1))
        self.frame_line_botton.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"    background-color: #dddddd; \n"
"    max-height: 1px;\n"
"}")
        self.frame_line_botton.setFrameShape(QFrame.Shape.HLine)
        self.frame_line_botton.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_line_top = QFrame(self.page_cart)
        self.frame_line_top.setObjectName(u"frame_line_top")
        self.frame_line_top.setGeometry(QRect(0, 60, 341, 1))
        self.frame_line_top.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"    background-color: #dddddd; \n"
"    max-height: 1px;\n"
"}")
        self.frame_line_top.setFrameShape(QFrame.Shape.HLine)
        self.frame_line_top.setFrameShadow(QFrame.Shadow.Plain)
        self.stackedWidget_2.addWidget(self.page_cart)

        self.verticalLayout_2.addWidget(self.stackedWidget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_background_shop.setText("")
        self.label_name_shop.setText(QCoreApplication.translate("MainWindow", u"Steak With Me", None))
        self.label_logo_shop.setText("")
        self.label_number_table.setText(QCoreApplication.translate("MainWindow", u"\u0e42\u0e15\u0e4a\u0e30 : #2", None))
        self.btn_all.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", None))
        self.btn_steak.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e40\u0e15\u0e47\u0e01", None))
        self.btn_burger.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1a\u0e2d\u0e23\u0e4c\u0e40\u0e01\u0e2d\u0e23\u0e4c", None))
        self.btn_pasta.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e1b\u0e32\u0e40\u0e01\u0e15\u0e15\u0e35", None))
        self.btn_salad.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e25\u0e31\u0e14", None))
        self.btn_snack.setText(QCoreApplication.translate("MainWindow", u"\u0e02\u0e2d\u0e07\u0e17\u0e32\u0e19\u0e40\u0e25\u0e48\u0e19", None))
        self.btn_drink.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e14\u0e37\u0e48\u0e21", None))
        self.btn_home_to_cart.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", None))
        self.label_all_title.setText("")
        self.label_food_image.setText("")
        self.btn_detail_to_home.setText("")
        self.label_food_name.setText("")
        self.label_food_price.setText(QCoreApplication.translate("MainWindow", u"\u0e3f0", None))
        self.label_note_description_2.setText(QCoreApplication.translate("MainWindow", u"\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e15\u0e34\u0e21", None))
        self.label_note_description.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e38\u0e13\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e43\u0e2a\u0e48\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e15\u0e34\u0e21\u0e44\u0e14\u0e49\u0e17\u0e35\u0e48\u0e19\u0e35\u0e48 \u0e40\u0e0a\u0e48\u0e19 \u0e2d\u0e32\u0e2b\u0e32\u0e23\u0e17\u0e35\u0e48\u0e41\u0e1e\u0e49", None))
        self.textEdit_message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\"\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e15\u0e34\u0e21...\"", None))
        self.btn_delete.setText("")
#if QT_CONFIG(tooltip)
        self.label_qty_list.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/>1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_qty_list.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_add.setText("")
        self.btn_add_to_cart.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23", None))
        self.btn_cart_to_home.setText("")
        self.lable_menulist.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e2d\u0e32\u0e2b\u0e32\u0e23\u0e17\u0e35\u0e48\u0e2a\u0e31\u0e48\u0e07", None))
        self.label_total_item.setText(QCoreApplication.translate("MainWindow", u"3 \u0e23\u0e32\u0e22\u0e01\u0e32\u0e23", None))
        self.label_total_price.setText(QCoreApplication.translate("MainWindow", u"\u0e3f00.00", None))
        self.btn_checkout.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e31\u0e48\u0e07\u0e2d\u0e32\u0e2b\u0e32\u0e23", None))
    # retranslateUi

