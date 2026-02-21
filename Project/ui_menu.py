# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 542)
        MainWindow.setStyleSheet(u"QToolButton {\n"
"        background-color: white;\n"
"        border: 1px solid #e0e0e0;\n"
"        border-radius: 12px;\n"
"        padding-top: 1px;\n"
"        font-size: 13px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"        border: 2px solid #FFD100;\n"
"}\n"
"\n"
"/*\u0e1b\u0e23\u0e31\u0e1a\u0e23\u0e30\u0e22\u0e30\u0e2b\u0e48\u0e32\u0e07\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07 Icon \u0e01\u0e31\u0e1a Text */\n"
"QToolButton::menu-indicator { image: none; }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widge_left = QWidget(self.centralwidget)
        self.widge_left.setObjectName(u"widge_left")
        self.widge_left.setStyleSheet(u"QWidget {\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #212121;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widge_left)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.widge_left)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"background-color: #079757;\n"
"border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pbtn_3 = QPushButton(self.frame)
        self.pbtn_3.setObjectName(u"pbtn_3")
        self.pbtn_3.setMinimumSize(QSize(30, 30))
        self.pbtn_3.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"img/3.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbtn_3.setIcon(icon)
        self.pbtn_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pbtn_3)

        self.pbtn_search = QPushButton(self.frame)
        self.pbtn_search.setObjectName(u"pbtn_search")
        self.pbtn_search.setMinimumSize(QSize(30, 30))
        self.pbtn_search.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"img/search.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbtn_search.setIcon(icon1)
        self.pbtn_search.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pbtn_search)

        self.lbl_order_id = QLabel(self.frame)
        self.lbl_order_id.setObjectName(u"lbl_order_id")

        self.horizontalLayout_2.addWidget(self.lbl_order_id)


        self.verticalLayout.addWidget(self.frame)

        self.category = QFrame(self.widge_left)
        self.category.setObjectName(u"category")
        self.category.setStyleSheet(u"QFrame {\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #212121;\n"
"}")
        self.category.setFrameShape(QFrame.StyledPanel)
        self.category.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.category)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tbtn_all = QToolButton(self.category)
        self.tbtn_all.setObjectName(u"tbtn_all")
        self.tbtn_all.setMinimumSize(QSize(80, 70))
        self.tbtn_all.setMaximumSize(QSize(90, 70))
        font = QFont()
        font.setBold(True)
        self.tbtn_all.setFont(font)

        self.horizontalLayout_3.addWidget(self.tbtn_all)

        self.tbtn_cat_steak = QToolButton(self.category)
        self.tbtn_cat_steak.setObjectName(u"tbtn_cat_steak")
        self.tbtn_cat_steak.setMinimumSize(QSize(80, 70))
        self.tbtn_cat_steak.setMaximumSize(QSize(90, 70))
        self.tbtn_cat_steak.setFont(font)

        self.horizontalLayout_3.addWidget(self.tbtn_cat_steak)

        self.tbtn_cat_burger = QToolButton(self.category)
        self.tbtn_cat_burger.setObjectName(u"tbtn_cat_burger")
        self.tbtn_cat_burger.setMinimumSize(QSize(80, 70))
        self.tbtn_cat_burger.setMaximumSize(QSize(90, 70))
        self.tbtn_cat_burger.setFont(font)

        self.horizontalLayout_3.addWidget(self.tbtn_cat_burger)

        self.tbtn_cat_spaghetti = QToolButton(self.category)
        self.tbtn_cat_spaghetti.setObjectName(u"tbtn_cat_spaghetti")
        self.tbtn_cat_spaghetti.setMinimumSize(QSize(80, 70))
        self.tbtn_cat_spaghetti.setMaximumSize(QSize(90, 70))
        self.tbtn_cat_spaghetti.setFont(font)

        self.horizontalLayout_3.addWidget(self.tbtn_cat_spaghetti)

        self.tbtn_cat_salad = QToolButton(self.category)
        self.tbtn_cat_salad.setObjectName(u"tbtn_cat_salad")
        self.tbtn_cat_salad.setMinimumSize(QSize(80, 70))
        self.tbtn_cat_salad.setMaximumSize(QSize(90, 70))
        self.tbtn_cat_salad.setFont(font)

        self.horizontalLayout_3.addWidget(self.tbtn_cat_salad)

        self.tbtn_cat_snack = QToolButton(self.category)
        self.tbtn_cat_snack.setObjectName(u"tbtn_cat_snack")
        self.tbtn_cat_snack.setMinimumSize(QSize(80, 70))
        self.tbtn_cat_snack.setMaximumSize(QSize(90, 70))
        self.tbtn_cat_snack.setFont(font)
        self.tbtn_cat_snack.setStyleSheet(u"QPushButton {\n"
"background-color: #FFFFFF;\n"
"border: 1px solid #212121;\n"
"}")

        self.horizontalLayout_3.addWidget(self.tbtn_cat_snack)

        self.tbtn_cat_drink = QToolButton(self.category)
        self.tbtn_cat_drink.setObjectName(u"tbtn_cat_drink")
        self.tbtn_cat_drink.setMinimumSize(QSize(80, 70))
        self.tbtn_cat_drink.setMaximumSize(QSize(90, 70))
        self.tbtn_cat_drink.setFont(font)

        self.horizontalLayout_3.addWidget(self.tbtn_cat_drink)


        self.verticalLayout.addWidget(self.category)

        self.food_menu = QScrollArea(self.widge_left)
        self.food_menu.setObjectName(u"food_menu")
        self.food_menu.setWidgetResizable(True)
        self.menuGrid = QWidget()
        self.menuGrid.setObjectName(u"menuGrid")
        self.menuGrid.setGeometry(QRect(0, 0, 597, 1020))
        self.gridLayout = QGridLayout(self.menuGrid)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_salad_tuna = QToolButton(self.menuGrid)
        self.btn_salad_tuna.setObjectName(u"btn_salad_tuna")
        self.btn_salad_tuna.setMinimumSize(QSize(140, 120))
        self.btn_salad_tuna.setMaximumSize(QSize(140, 120))
        self.btn_salad_tuna.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_salad_tuna, 3, 3, 1, 1)

        self.btn_redsoda = QToolButton(self.menuGrid)
        self.btn_redsoda.setObjectName(u"btn_redsoda")
        self.btn_redsoda.setMinimumSize(QSize(140, 120))
        self.btn_redsoda.setMaximumSize(QSize(140, 120))
        self.btn_redsoda.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_redsoda, 6, 3, 1, 1)

        self.btn_steak_porkchop = QToolButton(self.menuGrid)
        self.btn_steak_porkchop.setObjectName(u"btn_steak_porkchop")
        self.btn_steak_porkchop.setMinimumSize(QSize(140, 120))
        self.btn_steak_porkchop.setMaximumSize(QSize(140, 120))
        self.btn_steak_porkchop.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_steak_porkchop, 0, 2, 1, 1)

        self.btn_steak_teriyaki = QToolButton(self.menuGrid)
        self.btn_steak_teriyaki.setObjectName(u"btn_steak_teriyaki")
        self.btn_steak_teriyaki.setMinimumSize(QSize(140, 120))
        self.btn_steak_teriyaki.setMaximumSize(QSize(140, 120))
        self.btn_steak_teriyaki.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_steak_teriyaki, 1, 0, 1, 1)

        self.btn_steak_garlic = QToolButton(self.menuGrid)
        self.btn_steak_garlic.setObjectName(u"btn_steak_garlic")
        self.btn_steak_garlic.setMinimumSize(QSize(140, 120))
        self.btn_steak_garlic.setMaximumSize(QSize(140, 120))
        self.btn_steak_garlic.setStyleSheet(u"")
        self.btn_steak_garlic.setIconSize(QSize(20, 20))
        self.btn_steak_garlic.setCheckable(False)
        self.btn_steak_garlic.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.btn_steak_garlic.setAutoRaise(False)
        self.btn_steak_garlic.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.btn_steak_garlic, 0, 0, 1, 1)

        self.btn_frenchfries = QToolButton(self.menuGrid)
        self.btn_frenchfries.setObjectName(u"btn_frenchfries")
        self.btn_frenchfries.setMinimumSize(QSize(140, 120))
        self.btn_frenchfries.setMaximumSize(QSize(140, 120))
        self.btn_frenchfries.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_frenchfries, 4, 2, 1, 1)

        self.btn_bluehawaiian = QToolButton(self.menuGrid)
        self.btn_bluehawaiian.setObjectName(u"btn_bluehawaiian")
        self.btn_bluehawaiian.setMinimumSize(QSize(140, 120))
        self.btn_bluehawaiian.setMaximumSize(QSize(140, 120))
        self.btn_bluehawaiian.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_bluehawaiian, 6, 2, 1, 1)

        self.btn_burger_teriyaki = QToolButton(self.menuGrid)
        self.btn_burger_teriyaki.setObjectName(u"btn_burger_teriyaki")
        self.btn_burger_teriyaki.setMinimumSize(QSize(140, 120))
        self.btn_burger_teriyaki.setMaximumSize(QSize(140, 120))
        self.btn_burger_teriyaki.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_burger_teriyaki, 2, 3, 1, 1)

        self.btn_burger_bacon = QToolButton(self.menuGrid)
        self.btn_burger_bacon.setObjectName(u"btn_burger_bacon")
        self.btn_burger_bacon.setMinimumSize(QSize(140, 120))
        self.btn_burger_bacon.setMaximumSize(QSize(140, 120))
        self.btn_burger_bacon.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_burger_bacon, 2, 0, 1, 1)

        self.btn_steak_grillfish = QToolButton(self.menuGrid)
        self.btn_steak_grillfish.setObjectName(u"btn_steak_grillfish")
        self.btn_steak_grillfish.setMinimumSize(QSize(140, 120))
        self.btn_steak_grillfish.setMaximumSize(QSize(140, 120))
        self.btn_steak_grillfish.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_steak_grillfish, 1, 2, 1, 1)

        self.btn_water = QToolButton(self.menuGrid)
        self.btn_water.setObjectName(u"btn_water")
        self.btn_water.setMinimumSize(QSize(140, 120))
        self.btn_water.setMaximumSize(QSize(140, 120))
        self.btn_water.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_water, 7, 1, 1, 1)

        self.btn_steak_pepper = QToolButton(self.menuGrid)
        self.btn_steak_pepper.setObjectName(u"btn_steak_pepper")
        self.btn_steak_pepper.setMinimumSize(QSize(140, 120))
        self.btn_steak_pepper.setMaximumSize(QSize(140, 120))
        self.btn_steak_pepper.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_steak_pepper, 0, 1, 1, 1)

        self.btn_steak_hamcheese = QToolButton(self.menuGrid)
        self.btn_steak_hamcheese.setObjectName(u"btn_steak_hamcheese")
        self.btn_steak_hamcheese.setMinimumSize(QSize(140, 120))
        self.btn_steak_hamcheese.setMaximumSize(QSize(140, 120))
        self.btn_steak_hamcheese.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_steak_hamcheese, 1, 1, 1, 1)

        self.btn_ice = QToolButton(self.menuGrid)
        self.btn_ice.setObjectName(u"btn_ice")
        self.btn_ice.setMinimumSize(QSize(140, 120))
        self.btn_ice.setMaximumSize(QSize(140, 120))
        self.btn_ice.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_ice, 7, 2, 1, 1)

        self.btn_passionfruit = QToolButton(self.menuGrid)
        self.btn_passionfruit.setObjectName(u"btn_passionfruit")
        self.btn_passionfruit.setMinimumSize(QSize(140, 120))
        self.btn_passionfruit.setMaximumSize(QSize(140, 120))
        self.btn_passionfruit.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_passionfruit, 7, 0, 1, 1)

        self.btn_coke_jug = QToolButton(self.menuGrid)
        self.btn_coke_jug.setObjectName(u"btn_coke_jug")
        self.btn_coke_jug.setMinimumSize(QSize(140, 120))
        self.btn_coke_jug.setMaximumSize(QSize(140, 120))
        self.btn_coke_jug.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_coke_jug, 6, 0, 1, 1)

        self.btn_spaghetti_tomyum = QToolButton(self.menuGrid)
        self.btn_spaghetti_tomyum.setObjectName(u"btn_spaghetti_tomyum")
        self.btn_spaghetti_tomyum.setMinimumSize(QSize(140, 120))
        self.btn_spaghetti_tomyum.setMaximumSize(QSize(140, 120))
        self.btn_spaghetti_tomyum.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_spaghetti_tomyum, 3, 2, 1, 1)

        self.btn_spinach = QToolButton(self.menuGrid)
        self.btn_spinach.setObjectName(u"btn_spinach")
        self.btn_spinach.setMinimumSize(QSize(140, 120))
        self.btn_spinach.setMaximumSize(QSize(140, 120))
        self.btn_spinach.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_spinach, 5, 2, 1, 1)

        self.btn_potatoes = QToolButton(self.menuGrid)
        self.btn_potatoes.setObjectName(u"btn_potatoes")
        self.btn_potatoes.setMinimumSize(QSize(140, 120))
        self.btn_potatoes.setMaximumSize(QSize(140, 120))
        self.btn_potatoes.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_potatoes, 5, 0, 1, 1)

        self.btn_spaghetti_carbonara = QToolButton(self.menuGrid)
        self.btn_spaghetti_carbonara.setObjectName(u"btn_spaghetti_carbonara")
        self.btn_spaghetti_carbonara.setMinimumSize(QSize(140, 120))
        self.btn_spaghetti_carbonara.setMaximumSize(QSize(140, 120))
        self.btn_spaghetti_carbonara.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_spaghetti_carbonara, 3, 1, 1, 1)

        self.btn_burger_spicy = QToolButton(self.menuGrid)
        self.btn_burger_spicy.setObjectName(u"btn_burger_spicy")
        self.btn_burger_spicy.setMinimumSize(QSize(140, 120))
        self.btn_burger_spicy.setMaximumSize(QSize(140, 120))
        self.btn_burger_spicy.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_burger_spicy, 2, 1, 1, 1)

        self.btn_salad_vegetable = QToolButton(self.menuGrid)
        self.btn_salad_vegetable.setObjectName(u"btn_salad_vegetable")
        self.btn_salad_vegetable.setMinimumSize(QSize(140, 120))
        self.btn_salad_vegetable.setMaximumSize(QSize(140, 120))
        self.btn_salad_vegetable.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_salad_vegetable, 4, 1, 1, 1)

        self.btn_spaghetti_drunk = QToolButton(self.menuGrid)
        self.btn_spaghetti_drunk.setObjectName(u"btn_spaghetti_drunk")
        self.btn_spaghetti_drunk.setMinimumSize(QSize(140, 120))
        self.btn_spaghetti_drunk.setMaximumSize(QSize(140, 120))
        self.btn_spaghetti_drunk.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_spaghetti_drunk, 3, 0, 1, 1)

        self.btn_bread = QToolButton(self.menuGrid)
        self.btn_bread.setObjectName(u"btn_bread")
        self.btn_bread.setMinimumSize(QSize(140, 120))
        self.btn_bread.setMaximumSize(QSize(140, 120))
        self.btn_bread.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_bread, 4, 3, 1, 1)

        self.btn_steak_friedfish = QToolButton(self.menuGrid)
        self.btn_steak_friedfish.setObjectName(u"btn_steak_friedfish")
        self.btn_steak_friedfish.setMinimumSize(QSize(140, 120))
        self.btn_steak_friedfish.setMaximumSize(QSize(140, 120))
        self.btn_steak_friedfish.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_steak_friedfish, 1, 3, 1, 1)

        self.btn_lemontea = QToolButton(self.menuGrid)
        self.btn_lemontea.setObjectName(u"btn_lemontea")
        self.btn_lemontea.setMinimumSize(QSize(140, 120))
        self.btn_lemontea.setMaximumSize(QSize(140, 120))
        self.btn_lemontea.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_lemontea, 6, 1, 1, 1)

        self.btn_salad_apple = QToolButton(self.menuGrid)
        self.btn_salad_apple.setObjectName(u"btn_salad_apple")
        self.btn_salad_apple.setMinimumSize(QSize(140, 120))
        self.btn_salad_apple.setMaximumSize(QSize(140, 120))
        self.btn_salad_apple.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_salad_apple, 4, 0, 1, 1)

        self.btn_coke_glass = QToolButton(self.menuGrid)
        self.btn_coke_glass.setObjectName(u"btn_coke_glass")
        self.btn_coke_glass.setMinimumSize(QSize(140, 120))
        self.btn_coke_glass.setMaximumSize(QSize(140, 120))
        self.btn_coke_glass.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_coke_glass, 5, 3, 1, 1)

        self.btn_steak_spicy = QToolButton(self.menuGrid)
        self.btn_steak_spicy.setObjectName(u"btn_steak_spicy")
        self.btn_steak_spicy.setMinimumSize(QSize(140, 120))
        self.btn_steak_spicy.setMaximumSize(QSize(140, 120))
        self.btn_steak_spicy.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_steak_spicy, 0, 3, 1, 1)

        self.btn_onion = QToolButton(self.menuGrid)
        self.btn_onion.setObjectName(u"btn_onion")
        self.btn_onion.setMinimumSize(QSize(140, 120))
        self.btn_onion.setMaximumSize(QSize(140, 120))
        self.btn_onion.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_onion, 5, 1, 1, 1)

        self.btn_burger_fish = QToolButton(self.menuGrid)
        self.btn_burger_fish.setObjectName(u"btn_burger_fish")
        self.btn_burger_fish.setMinimumSize(QSize(140, 120))
        self.btn_burger_fish.setMaximumSize(QSize(140, 120))
        self.btn_burger_fish.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.gridLayout.addWidget(self.btn_burger_fish, 2, 2, 1, 1)

        self.food_menu.setWidget(self.menuGrid)

        self.verticalLayout.addWidget(self.food_menu)


        self.horizontalLayout.addWidget(self.widge_left)

        self.widget_right = QWidget(self.centralwidget)
        self.widget_right.setObjectName(u"widget_right")
        self.widget_right.setMinimumSize(QSize(320, 320))
        self.widget_right.setStyleSheet(u"QWidget {\n"
"background-color: #FFFFFF;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.header = QFrame(self.widget_right)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pbtn_table = QPushButton(self.header)
        self.pbtn_table.setObjectName(u"pbtn_table")
        self.pbtn_table.setMinimumSize(QSize(50, 50))
        self.pbtn_table.setMaximumSize(QSize(120, 120))
        font1 = QFont()
        font1.setPointSize(14)
        self.pbtn_table.setFont(font1)
        self.pbtn_table.setContextMenuPolicy(Qt.NoContextMenu)
        self.pbtn_table.setLayoutDirection(Qt.LeftToRight)
        self.pbtn_table.setStyleSheet(u"QPushButton {\n"
"background-color: #F8F9FA;\n"
"border: 1px solid #F8F9FA\n"
"}")

        self.horizontalLayout_4.addWidget(self.pbtn_table)

        self.lbl_current_table = QLabel(self.header)
        self.lbl_current_table.setObjectName(u"lbl_current_table")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.lbl_current_table.setFont(font2)
        self.lbl_current_table.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbl_current_table.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_4.addWidget(self.lbl_current_table)


        self.verticalLayout_2.addWidget(self.header)

        self.order = QTableWidget(self.widget_right)
        if (self.order.columnCount() < 3):
            self.order.setColumnCount(3)
        font2 = QFont()
        font2.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.order.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.order.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.order.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.order.setObjectName(u"order")
        self.order.setFont(font2)
        self.order.setStyleSheet(u"QTableWidget {\n"
"border: 1px solid #212121;\n"
"}")
        self.order.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.order.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.order.horizontalHeader().setVisible(True)
        self.order.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.order)

        self.lbl_total = QLabel(self.widget_right)
        self.lbl_total.setObjectName(u"lbl_total")
        self.lbl_total.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.lbl_total.setFont(font3)
        self.lbl_total.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.lbl_total, 0, Qt.AlignRight)

        self.summary = QFrame(self.widget_right)
        self.summary.setObjectName(u"summary")
        self.summary.setFrameShape(QFrame.StyledPanel)
        self.summary.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.summary)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pbtn_save = QPushButton(self.summary)
        self.pbtn_save.setObjectName(u"pbtn_save")
        self.pbtn_save.setMinimumSize(QSize(50, 50))
        self.pbtn_save.setMaximumSize(QSize(120, 120))
        font4 = QFont()
        font4.setPointSize(16)
        self.pbtn_save.setFont(font4)
        self.pbtn_save.setStyleSheet(u"QPushButton {\n"
"background-color: #E1E2E4;\n"
"border: 1px solid #E1E2E4;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.pbtn_save)

        self.pbtn_pay = QPushButton(self.summary)
        self.pbtn_pay.setObjectName(u"pbtn_pay")
        self.pbtn_pay.setMinimumSize(QSize(50, 50))
        self.pbtn_pay.setMaximumSize(QSize(120, 120))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.pbtn_pay.setFont(font5)
        self.pbtn_pay.setStyleSheet(u"QPushButton {\n"
"background-color: #FFF59D;\n"
"border: 1px solid #FFF59D;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pbtn_pay)


        self.verticalLayout_2.addWidget(self.summary)


        self.horizontalLayout.addWidget(self.widget_right)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 978, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pbtn_3.setText("")
        self.pbtn_search.setText("")
        self.lbl_order_id.setText("")
        self.tbtn_all.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", None))
        self.tbtn_cat_steak.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e40\u0e15\u0e47\u0e01", None))
        self.tbtn_cat_burger.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1a\u0e2d\u0e23\u0e4c\u0e40\u0e01\u0e2d\u0e23\u0e4c", None))
        self.tbtn_cat_spaghetti.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e1b\u0e32\u0e23\u0e4c\u0e40\u0e01\u0e15\u0e15\u0e35", None))
        self.tbtn_cat_salad.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e25\u0e31\u0e14", None))
        self.tbtn_cat_snack.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e32\u0e19\u0e40\u0e25\u0e48\u0e19", None))
        self.tbtn_cat_drink.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e14\u0e37\u0e48\u0e21", None))
        self.btn_salad_tuna.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_redsoda.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_steak_porkchop.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_steak_teriyaki.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_steak_garlic.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_frenchfries.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_bluehawaiian.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_burger_teriyaki.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_burger_bacon.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_steak_grillfish.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_water.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_steak_pepper.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_steak_hamcheese.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_ice.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_passionfruit.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_coke_jug.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_spaghetti_tomyum.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_spinach.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_potatoes.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_spaghetti_carbonara.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_burger_spicy.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_salad_vegetable.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_spaghetti_drunk.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_bread.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_steak_friedfish.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_lemontea.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_salad_apple.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_coke_glass.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_steak_spicy.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_onion.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_burger_fish.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pbtn_table.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e42\u0e15\u0e4a\u0e30", None))
        ___qtablewidgetitem = self.order.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23", None));
        ___qtablewidgetitem1 = self.order.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19", None));
        ___qtablewidgetitem2 = self.order.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0e22\u0e2d\u0e14\u0e23\u0e27\u0e21 (\u0e1a\u0e32\u0e17)", None));
        self.lbl_total.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.pbtn_save.setText(QCoreApplication.translate("MainWindow", u"\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
        self.pbtn_pay.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e33\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23", None))
    # retranslateUi

