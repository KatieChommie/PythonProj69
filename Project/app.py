import sys
import qrcode
import os
import random
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QWidget,
                               QDialog, QMessageBox, QInputDialog, QPushButton,
                               QVBoxLayout, QTableWidget, QHeaderView)
from PySide6.QtGui import QIcon, Qt, QPixmap
from ui_menu import Ui_MainWindow
from ui_table import Ui_TableWindow
from ui_payment import Ui_PaymentWindow
from db_manager import DBManager
from cart import Cart
from datetime import datetime

class POS_system(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = DBManager("D:/code/python/forproj2026/menu.db")
        self.cart = Cart()

        self.ui.pbtn_3.clicked.connect(self.show_order_history)
        self.ui.pbtn_search.clicked.connect(self.search_menu)
        self.generate_order_id()

        # category actions
        self.steak_btns = [self.ui.btn_steak_garlic, self.ui.btn_steak_porkchop, self.ui.btn_steak_teriyaki,
                           self.ui.btn_steak_spicy, self.ui.btn_steak_pepper, self.ui.btn_steak_hamcheese,
                           self.ui.btn_steak_grillfish, self.ui.btn_steak_friedfish
                           ]
        self.burger_btns = [
            self.ui.btn_burger_bacon, self.ui.btn_burger_spicy,
            self.ui.btn_burger_teriyaki, self.ui.btn_burger_fish
        ]
        self.spaghetti_btns = [
            self.ui.btn_spaghetti_tomyum, self.ui.btn_spaghetti_carbonara, self.ui.btn_spaghetti_drunk
        ]
        self.salad_btns = [
            self.ui.btn_salad_tuna, self.ui.btn_salad_vegetable, self.ui.btn_salad_apple
        ]
        self.snack_btns = [
            self.ui.btn_frenchfries, self.ui.btn_spinach, self.ui.btn_potatoes,
            self.ui.btn_onion, self.ui.btn_bread
        ]
        self.drink_btns = [
            self.ui.btn_redsoda, self.ui.btn_bluehawaiian, self.ui.btn_water,
            self.ui.btn_ice, self.ui.btn_passionfruit, self.ui.btn_coke_jug,
            self.ui.btn_lemontea, self.ui.btn_coke_glass
        ]
        self.all_food_btns = (self.steak_btns + self.burger_btns + self.spaghetti_btns +
                              self.salad_btns + self.snack_btns + self.drink_btns)

        self.ui.tbtn_all.clicked.connect(lambda: self.filter_category("all"))
        self.ui.tbtn_cat_steak.clicked.connect(lambda: self.filter_category("steak"))
        self.ui.tbtn_cat_burger.clicked.connect(lambda: self.filter_category("burger"))
        self.ui.tbtn_cat_spaghetti.clicked.connect(lambda: self.filter_category("spaghetti"))
        self.ui.tbtn_cat_salad.clicked.connect(lambda: self.filter_category("salad"))
        self.ui.tbtn_cat_snack.clicked.connect(lambda: self.filter_category("snack"))
        self.ui.tbtn_cat_drink.clicked.connect(lambda: self.filter_category("drink"))

        #image-steak
        self.ui.btn_steak_garlic.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_garlic.jpg"))
        self.ui.btn_steak_garlic.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_steak_garlic, "menus", 101)
        self.ui.btn_steak_pepper.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_pepper.jpg"))
        self.ui.btn_steak_pepper.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_steak_pepper, "menus", 102)
        self.ui.btn_steak_porkchop.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_porkchop.jpeg"))
        self.ui.btn_steak_porkchop.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_steak_porkchop, "menus", 103)
        self.ui.btn_steak_spicy.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_spicy.jpg"))
        self.ui.btn_steak_spicy.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_steak_spicy, "menus", 104)
        self.ui.btn_steak_teriyaki.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_teriyaki.jpg"))
        self.ui.btn_steak_teriyaki.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_steak_teriyaki, "menus", 108)
        self.ui.btn_steak_hamcheese.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_hamcheese.jpg"))
        self.ui.btn_steak_hamcheese.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_steak_hamcheese, "menus", 105)
        self.ui.btn_steak_grillfish.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_grillfish.jpeg"))
        self.ui.btn_steak_grillfish.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_steak_grillfish, "menus", 106)
        self.ui.btn_steak_friedfish.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_friedfish.jpg"))
        self.ui.btn_steak_friedfish.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_steak_friedfish, "menus", 107)
        #image-burger
        self.ui.btn_burger_bacon.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/burger_bacon.jpg"))
        self.ui.btn_burger_bacon.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_burger_bacon, "burger", 201)
        self.ui.btn_burger_spicy.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/burger_spicy.jpeg"))
        self.ui.btn_burger_spicy.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_burger_spicy, "burger", 202)
        self.ui.btn_burger_fish.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/burger_fish.jpg"))
        self.ui.btn_burger_fish.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_burger_fish, "burger", 203)
        self.ui.btn_burger_teriyaki.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/burger_teriyaki.jpg"))
        self.ui.btn_burger_teriyaki.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_burger_teriyaki, "burger", 204)
        #image-spaghetti
        self.ui.btn_spaghetti_drunk.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/spaghetti_drunk.jpg"))
        self.ui.btn_spaghetti_drunk.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_spaghetti_drunk, "pasta", 301)
        self.ui.btn_spaghetti_carbonara.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/spaghetti_carbonara.jpg"))
        self.ui.btn_spaghetti_carbonara.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_spaghetti_carbonara, "pasta", 302)
        self.ui.btn_spaghetti_tomyum.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/spaghetti_tomyum.jpg"))
        self.ui.btn_spaghetti_tomyum.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_spaghetti_tomyum, "pasta", 303)
        #image-salad
        self.ui.btn_salad_tuna.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/salad_tuna.png"))
        self.ui.btn_salad_tuna.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_salad_tuna, "salad", 401)
        self.ui.btn_salad_apple.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/salad_apple.jpg"))
        self.ui.btn_salad_apple.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_salad_apple, "salad", 402)
        self.ui.btn_salad_vegetable.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/salad_vegetable.jpg"))
        self.ui.btn_salad_vegetable.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_salad_vegetable, "salad", 403)
        #image-snacks
        self.ui.btn_frenchfries.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/frenchfries.jpg"))
        self.ui.btn_frenchfries.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_frenchfries, "snacks", 501)
        self.ui.btn_bread.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/bread.jpg"))
        self.ui.btn_bread.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_bread, "snacks", 502)
        self.ui.btn_potatoes.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/potatoes.jpg"))
        self.ui.btn_potatoes.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_potatoes, "snacks", 503)
        self.ui.btn_onion.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/onion.jpg"))
        self.ui.btn_onion.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_onion, "snacks", 504)
        self.ui.btn_spinach.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/spinach.jpg"))
        self.ui.btn_spinach.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_spinach, "snacks", 505)
        #image-drinks
        self.ui.btn_coke_glass.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/coke_glass.jpeg"))
        self.ui.btn_coke_glass.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_coke_glass, "drinks", 601)
        self.ui.btn_coke_jug.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/coke_jug.jpeg"))
        self.ui.btn_coke_jug.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_coke_jug, "drinks", 602)
        self.ui.btn_lemontea.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/lemontea.jpg"))
        self.ui.btn_lemontea.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_lemontea, "drinks", 603)
        self.ui.btn_bluehawaiian.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/bluehawaiian.png"))
        self.ui.btn_bluehawaiian.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_bluehawaiian, "drinks", 604)
        self.ui.btn_redsoda.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/redsoda.jpg"))
        self.ui.btn_redsoda.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_redsoda, "drinks", 605)
        self.ui.btn_passionfruit.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/passionfruit.jpg"))
        self.ui.btn_passionfruit.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_passionfruit, "drinks", 606)
        self.ui.btn_water.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/water.jpeg"))
        self.ui.btn_water.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_water, "drinks", 607)
        self.ui.btn_ice.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/ice.jpg"))
        self.ui.btn_ice.setIconSize(QSize(110, 100))
        self.setup_button_ui(self.ui.btn_ice, "drinks", 608)

        #button actions
        #steak
        self.ui.btn_steak_garlic.clicked.connect(lambda: self.add_to_cart_db("menus", 101))
        self.ui.btn_steak_pepper.clicked.connect(lambda: self.add_to_cart_db("menus", 102))
        self.ui.btn_steak_porkchop.clicked.connect(lambda: self.add_to_cart_db("menus", 103))
        self.ui.btn_steak_spicy.clicked.connect(lambda: self.add_to_cart_db("menus", 104))
        self.ui.btn_steak_hamcheese.clicked.connect(lambda: self.add_to_cart_db("menus", 105))
        self.ui.btn_steak_grillfish.clicked.connect(lambda: self.add_to_cart_db("menus", 106))
        self.ui.btn_steak_friedfish.clicked.connect(lambda: self.add_to_cart_db("menus", 107))
        self.ui.btn_steak_teriyaki.clicked.connect(lambda: self.add_to_cart_db("menus", 108))
        #burger
        self.ui.btn_burger_bacon.clicked.connect(lambda: self.add_to_cart_db("burger", 201))
        self.ui.btn_burger_spicy.clicked.connect(lambda: self.add_to_cart_db("burger", 202))
        self.ui.btn_burger_fish.clicked.connect(lambda: self.add_to_cart_db("burger", 203))
        self.ui.btn_burger_teriyaki.clicked.connect(lambda: self.add_to_cart_db("burger", 204))
        #spaghetti
        self.ui.btn_spaghetti_drunk.clicked.connect(lambda: self.add_to_cart_db("pasta", 301))
        self.ui.btn_spaghetti_carbonara.clicked.connect(lambda: self.add_to_cart_db("pasta", 302))
        self.ui.btn_spaghetti_tomyum.clicked.connect(lambda: self.add_to_cart_db("pasta", 303))
        #salad
        self.ui.btn_salad_tuna.clicked.connect(lambda: self.add_to_cart_db("salad", 401))
        self.ui.btn_salad_apple.clicked.connect(lambda: self.add_to_cart_db("salad", 402))
        self.ui.btn_salad_vegetable.clicked.connect(lambda: self.add_to_cart_db("salad", 403))
        #snacks
        self.ui.btn_frenchfries.clicked.connect(lambda: self.add_to_cart_db("snacks", 501))
        self.ui.btn_bread.clicked.connect(lambda: self.add_to_cart_db("snacks", 502))
        self.ui.btn_potatoes.clicked.connect(lambda: self.add_to_cart_db("snacks", 503))
        self.ui.btn_onion.clicked.connect(lambda: self.add_to_cart_db("snacks", 504))
        self.ui.btn_spinach.clicked.connect(lambda: self.add_to_cart_db("snacks", 505))
        #drinks
        self.ui.btn_coke_glass.clicked.connect(lambda: self.add_to_cart_db("drinks", 601))
        self.ui.btn_coke_jug.clicked.connect(lambda: self.add_to_cart_db("drinks", 602))
        self.ui.btn_lemontea.clicked.connect(lambda: self.add_to_cart_db("drinks", 603))
        self.ui.btn_bluehawaiian.clicked.connect(lambda: self.add_to_cart_db("drinks", 604))
        self.ui.btn_redsoda.clicked.connect(lambda: self.add_to_cart_db("drinks", 605))
        self.ui.btn_passionfruit.clicked.connect(lambda: self.add_to_cart_db("drinks", 606))
        self.ui.btn_water.clicked.connect(lambda: self.add_to_cart_db("drinks", 607))
        self.ui.btn_ice.clicked.connect(lambda: self.add_to_cart_db("drinks", 608))

        #order
        self.ui.order.cellClicked.connect(self.manage_cart_item)
        self.ui.pbtn_clear.clicked.connect(self.clear_all_order)
        self.ui.pbtn_save.clicked.connect(self.save_current_order)

        #connection to others pages
        self.ui.pbtn_table.clicked.connect(self.open_table_window)
        self.ui.pbtn_pay.clicked.connect(self.open_payment_window)

    def filter_category(self, category_name):
        for btn in self.all_food_btns:
            btn.hide()

        buttons_to_show = []
        if category_name == "all":
            buttons_to_show = self.all_food_btns
        elif category_name == "steak":
            buttons_to_show = self.steak_btns
        elif category_name == "burger":
            buttons_to_show = self.burger_btns
        elif category_name == "spaghetti":
            buttons_to_show = self.spaghetti_btns
        elif category_name == "salad":
            buttons_to_show = self.salad_btns
        elif category_name == "snack":
            buttons_to_show = self.snack_btns
        elif category_name == "drink":
            buttons_to_show = self.drink_btns

        max_columns = 4
        row = 0
        col = 0
        for btn in buttons_to_show:
            btn.show()
            self.ui.gridLayout.addWidget(btn, row, col)
            col += 1
            if col >= max_columns:
                col = 0
                row += 1

    def show_order_history(self):
        orders = self.db.get_all_orders()
        dialog = QDialog(self)
        dialog.setWindowTitle("ประวัติการสั่งซื้อ")
        dialog.resize(700, 450)
        layout = QVBoxLayout(dialog)
        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["เลขบิล", "โต๊ะ", "ลูกค้า", "ยอดรวม", "สถานะ"])
        table.setRowCount(len(orders))
        for i, o in enumerate(orders):
            table.setItem(i, 0, QTableWidgetItem(str(o['order_no'])))
            table.setItem(i, 1, QTableWidgetItem(str(o['table_no'])))
            table.setItem(i, 2, QTableWidgetItem(str(o['cust_no'])))
            table.setItem(i, 3, QTableWidgetItem(f"{o['total']:,.2f}"))
            table.setItem(i, 4, QTableWidgetItem("จ่ายแล้ว" if o['status'] == 'paid' else "ค้างชำระ"))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(table)
        dialog.exec()

    def search_menu(self):

        search_text, ok_pressed = QInputDialog.getText(self, "ค้นหาเมนู", "พิมพ์ชื่ออาหารที่ต้องการค้นหา:")

        if ok_pressed and search_text:

            for btn in self.all_food_btns:
                btn.hide()

            buttons_to_show = []
            search_word = search_text.lower()
            for btn in self.all_food_btns:
                if search_word in btn.text().lower():
                    buttons_to_show.append(btn)

            max_columns = 4
            row = 0
            col = 0
            for btn in buttons_to_show:
                btn.show()
                self.ui.gridLayout.addWidget(btn, row, col)
                col += 1
                if col >= max_columns:
                    col = 0
                    row += 1

            if len(buttons_to_show) == 0:
                QMessageBox.warning(self, "ผลการค้นหา", f"ไม่พบเมนูที่มีคำว่า '{search_text}'")

    def generate_order_id(self):
        now = datetime.now()
        order_no = f"INV-{now.strftime('%Y%m%d-%H%M%S')}"
        self.current_order_id = order_no
        self.ui.lbl_order_id.setText(f"{order_no}")
        self.ui.lbl_order_id.setStyleSheet("color: white; font-size: 14px; font-weight: bold;")
    def add_to_cart(self, item_id, name, price):
        self.cart.add_item(item_id, name, price, qty=1)
        self.update_ui()
    def add_to_cart_db(self,table_name, item_id):
        item_data = self.db.get_menu_item(table_name, item_id)
        if item_data:
            self.cart.add_item(item_data["id"], item_data["name"], item_data["price"], qty=1)
            self.update_ui()
        else:
            QMessageBox.warning(self, "Error!", "Error!")

    def setup_button_ui(self, button, table_name, item_id):
        item_data = self.db.get_menu_item(table_name, item_id)

        if item_data:
            button.setText(item_data["name"])
        else:
            button.setText("ไม่พบข้อมูล")

        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

    def update_ui(self):
        items = self.cart.get_all_items()
        self.ui.order.setRowCount(len(items))

        for row_index, item in enumerate(items):
            self.ui.order.setItem(row_index, 0, QTableWidgetItem(item["name"]))
            self.ui.order.setItem(row_index, 1, QTableWidgetItem(str(item["qty"])))

            total_price = item["price"] * item["qty"]
            self.ui.order.setItem(row_index, 2, QTableWidgetItem(str(total_price)))

        total = self.cart.get_total_price()
        self.ui.lbl_total.setText(f"{total:,.2f} บาท")

    def manage_cart_item(self, row, column):
        items = self.cart.get_all_items()

        if row >= len(items):
            return

        selected_item = items[row]
        item_id = selected_item["id"]
        item_name = selected_item["name"]
        item_qty = selected_item["qty"]

        msg = QMessageBox(self)
        msg.setWindowTitle("จัดการรายการอาหาร")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText(f"เมนู: {item_name}\nจำนวนปัจจุบัน: {item_qty} รายการ\n\nคุณต้องการทำอะไร?")

        btn_decrease = msg.addButton("ลดจำนวนลง 1", QMessageBox.ButtonRole.ActionRole)
        btn_delete = msg.addButton("เคลียร์ทั้งหมด", QMessageBox.ButtonRole.DestructiveRole)
        btn_cancel = msg.addButton("ยกเลิก", QMessageBox.ButtonRole.RejectRole)

        msg.exec()

        if msg.clickedButton() == btn_decrease:
            if self.cart.items[item_id]["qty"] > 1:
                self.cart.items[item_id]["qty"] -= 1
            else:
                self.cart.remove_item(item_id)
            self.update_ui()

        elif msg.clickedButton() == btn_delete:
            self.cart.remove_item(item_id)
            self.update_ui()

    def save_current_order(self):
        items = self.cart.get_all_items()

        if len(items) == 0:
            QMessageBox.warning(self, "แจ้งเตือน", "ยังไม่มีรายการอาหารในบิลนี้")
            return
        if not hasattr(self, "current_table"):
            QMessageBox.warning(self, "แจ้งเตือน", "กรุณาเลือกโต๊ะก่อนทำรายการ")
            return

        table_no = self.current_table
        cust_no = getattr(self, 'current_customers', 1)
        total = self.cart.get_total_price()

        confirm = QMessageBox.question(
            self, "ยืนยันการบันทึก",
            f"ต้องการบันทึกออเดอร์ โต๊ะที่ {table_no} ยอดรวม {total:,.2f} บาท ใช่หรือไม่?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            if hasattr(self, "current_db_order_id"):
                success = self.db.update_existing_order(self.current_db_order_id, total, items, status="unpaid")
            else:
                success = self.db.save_order(self.current_order_id, table_no, cust_no, total, items, status="unpaid")

            if success:
                QMessageBox.information(self, "สำเร็จ", "บันทึกรายการอาหารเรียบร้อยแล้ว!")

                self.reset_ui_after_order()
    def clear_all_order(self):
        if len(self.cart.get_all_items()) == 0:
            return
        clr_msg = QMessageBox(self)
        clr_msg.setWindowTitle("ยืนยันการเคลียร์รายการอาหาร")
        clr_msg.setIcon(QMessageBox.Icon.Warning)
        clr_msg.setText("ต้องการเคลียร์รายการอาหารทั้งหมด และยกเลิกบิลนี้ใช่หรือไม่?")
        clr_msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if clr_msg.exec() == QMessageBox.StandardButton.Yes:
            self.reset_ui_after_order()

            #cleared successfully
            clred_msg = QMessageBox(self)
            clred_msg.setIcon(QMessageBox.Information)
            clred_msg.setText(f"เคลียร์รายการสำเร็จ")
            clred_msg.setWindowTitle("Cleared")
            clred_msg.exec()


    #ui_table page
    def open_table_window(self):
        self.table_window = QWidget()
        self.ui_table = Ui_TableWindow()
        self.ui_table.setupUi(self.table_window)

        self.ui_table.tbtn_table1.clicked.connect(lambda: self.select_table("1"))
        self.ui_table.tbtn_table2.clicked.connect(lambda: self.select_table("2"))
        self.ui_table.tbtn_table3.clicked.connect(lambda: self.select_table("3"))
        self.ui_table.tbtn_table4.clicked.connect(lambda: self.select_table("4"))
        self.ui_table.tbtn_table5.clicked.connect(lambda: self.select_table("5"))
        self.ui_table.tbtn_table6.clicked.connect(lambda: self.select_table("6"))
        self.ui_table.tbtn_table7.clicked.connect(lambda: self.select_table("7"))
        self.ui_table.tbtn_table8.clicked.connect(lambda: self.select_table("8"))

        self.ui_table.num0.clicked.connect(lambda: self.press_numpad("0"))
        self.ui_table.num1.clicked.connect(lambda: self.press_numpad("1"))
        self.ui_table.num2.clicked.connect(lambda: self.press_numpad("2"))
        self.ui_table.num3.clicked.connect(lambda: self.press_numpad("3"))
        self.ui_table.num4.clicked.connect(lambda: self.press_numpad("4"))
        self.ui_table.num5.clicked.connect(lambda: self.press_numpad("5"))
        self.ui_table.num6.clicked.connect(lambda: self.press_numpad("6"))
        self.ui_table.num7.clicked.connect(lambda: self.press_numpad("7"))
        self.ui_table.num8.clicked.connect(lambda: self.press_numpad("8"))
        self.ui_table.num9.clicked.connect(lambda: self.press_numpad("9"))
        self.ui_table.delete1.clicked.connect(self.backspace_numpad)

        self.ui_table.pbtn_confirm.clicked.connect(self.confirm_table)

        self.table_window.show()

    def select_table(self, table_no):
        self.current_table = table_no
        self.ui_table.lbl_table_header.setText(f"ภายใน โต๊ะที่ {table_no}")

    def press_numpad(self, number):
        current_text = self.ui_table.lineEdit.text()
        if current_text == "0":
            current_text = ""
        self.ui_table.lineEdit.setText(current_text + number)

    def backspace_numpad(self):
        current_text = self.ui_table.lineEdit.text()
        self.ui_table.lineEdit.setText(current_text[:-1])

    def confirm_table(self):
        cust_qty_str = self.ui_table.lineEdit.text()

        if not cust_qty_str or int(cust_qty_str) <= 0 or int(cust_qty_str) > 10:
            #show error box
            err_msg = QMessageBox()
            err_msg.setIcon(QMessageBox.Critical)
            err_msg.setText("โปรดกรอกจำนวนลูกค้าให้ถูกต้อง")
            err_msg.setWindowTitle("Error!")
            err_msg.exec()
            return

        if not hasattr(self, "current_table"):
            self.current_table = "1"

        self.current_customers = int(cust_qty_str)

        #confirm dialog
        confirm_msg = QMessageBox(self.table_window)
        confirm_msg.setIcon(QMessageBox.Question)
        confirm_msg.setText(f"ยืนยันการเปิดโต๊ะ\nโต๊ะที่ {self.current_table}\nจำนวนลูกค้า {cust_qty_str} ท่าน")
        confirm_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = confirm_msg.exec()

        if result == QMessageBox.Yes:
            success_msg = QMessageBox(self.table_window)
            success_msg.setIcon(QMessageBox.Information)
            success_msg.setText(f"เพิ่มข้อมูลลูกค้าสำเร็จ")
            success_msg.setInformativeText(f"โต๊ะที่ {self.current_table}\nจำนวนลูกค้าทั้งหมด {cust_qty_str} ท่าน")
            success_msg.setWindowTitle("Success!")
            success_msg.exec()
            self.ui.lbl_current_table.setText(f"โต๊ะที่ {self.current_table}\nลูกค้า {cust_qty_str} ท่าน")
            self.table_window.close()
            self.table_window.close()
            self.load_unpaid_order()

    # ui_payment page
    def load_unpaid_order(self):
        if not hasattr(self, "current_table"):
            return
        order_data = self.db.get_unpaid_order(self.current_table)

        if order_data:
            self.current_db_order_id = order_data["order_id"]
            self.current_order_id = order_data["order_no"]
            self.ui.lbl_order_id.setText(f"{self.current_order_id}")
            self.cart.clear_cart()
            for item in order_data["items"]:
                self.cart.add_item(item["menu_order"], item["menu_order"], item['price'], item['qty'])

            self.update_ui()
            QMessageBox.information(self, "ดึงบิลที่ยังไม่จ่ายสำเร็จ", f"ดึงรายการค้างจ่ายของโต๊ะ {self.current_table} กลับมาแล้ว")
        else:
            if hasattr(self, "current_db_order_id"):
                del self.current_db_order_id
            self.cart.clear_cart()
            self.update_ui()
            QMessageBox.information(self, "Cleared!", f"โต๊ะ {self.current_table} ว่างแล้ว พร้อมรับออเดอร์ใหม่")
    def open_payment_window(self):
        items = self.cart.get_all_items()

        if len(items) == 0:
            QMessageBox.warning(self, "แจ้งเตือน", "ยังไม่มีรายการอาหารในบิลนี้")
            return
        if not hasattr(self, "current_table"):
            QMessageBox.warning(self, "แจ้งเตือน", "กรุณาเลือกโต๊ะก่อนทำรายการ")
            return

        self.payment_window = QDialog(self)
        self.ui_payment = Ui_PaymentWindow()
        self.ui_payment.setupUi(self.payment_window)

        self.ui_payment.table_order.setRowCount(len(items))
        for row_index, item in enumerate(items):
            self.ui_payment.table_order.setItem(row_index, 0, QTableWidgetItem(item["name"]))
            self.ui_payment.table_order.setItem(row_index, 1, QTableWidgetItem(str(item["qty"])))
            total_price = item["price"] * item["qty"]
            self.ui_payment.table_order.setItem(row_index, 2, QTableWidgetItem(f"{total_price:,.2f}"))

        subtotal = self.cart.get_total_price()
        discount = 0.00
        vat = subtotal * 0.07
        net_total = subtotal + vat - discount

        self.btn_confirm_pay = QPushButton("ยืนยันการรับเงิน")
        self.btn_confirm_pay.setMinimumHeight(40)
        self.btn_confirm_pay.setStyleSheet(
        "background-color: #079757; color: white; font-size: 20px; font-weight: bold; border-radius: 10px;")

        self.ui_payment.table_summary.setColumnCount(1)
        self.ui_payment.table_summary.horizontalHeader().setVisible(False)
        self.ui_payment.table_summary.setItem(0, 0, QTableWidgetItem(f"{discount:,.2f}"))
        self.ui_payment.table_summary.setItem(1, 0, QTableWidgetItem(f"{vat:,.2f}"))
        self.ui_payment.table_summary.setItem(2, 0, QTableWidgetItem(f"{net_total:,.2f}"))
        self.ui_payment.verticalLayout_2.insertWidget(2, self.btn_confirm_pay)
        self.ui_payment.label_total.setText(f"{net_total:,.2f} บาท")
        self.ui_payment.pbtn_back.clicked.connect(self.payment_window.close)

        self.btn_confirm_pay.clicked.connect(lambda: self.confirm_payment(net_total))

        mock_text = f"สแกนเพื่อชำระเงิน\nยอดรวมทั้งสิ้น: {net_total:,.2f} บาท"
        qr_img = qrcode.make(mock_text)
        qr_img.save("mock_qr.png")

        pixmap = QPixmap("mock_qr.png")
        self.ui_payment.lbl_qr.setPixmap(pixmap.scaled(220, 220, Qt.KeepAspectRatio))
        self.ui_payment.lbl_qr.setAlignment(Qt.AlignCenter)

        self.payment_window.exec()




    def confirm_payment(self, net_total):
        table_no = self.current_table
        cust_no = getattr(self, "current_customers", 1)
        cart_items = self.cart.get_all_items()

        subtotal = self.cart.get_total_price()
        discount = 0.00
        vat = subtotal * 0.07

        if hasattr(self, "current_db_order_id"):
            success = self.db.update_existing_order(self.current_db_order_id, net_total, cart_items, status="paid")
        else:
            success = self.db.save_order(self.current_order_id, table_no, cust_no, net_total, cart_items, status="paid")

        if success:
            import random
            word = ["ขอให้วันนี้เป็นวันที่ดี", "ขอบคุณที่ใช้บริการ", "ไว้แวะมาอุดหนุนใหม่นะคะ", "เพราะกำลังใจที่มีค่า มาจากคุณลูกค้า", "ขอให้สุขภาพแข็งแรงและประสบความสำเร็จในทุกสิ่ง"]
            QMessageBox.information(self.payment_window, "ชำระเงินสำเร็จ", f"{random.choice(word)}")

            self.print_receipt(self.current_order_id, table_no, cust_no, cart_items, subtotal, discount, vat, net_total)

            self.payment_window.close()
            self.reset_ui_after_order()

    def reset_ui_after_order(self):
        self.cart.clear_cart()
        self.update_ui()
        self.ui.lbl_current_table.setText("")
        for attr in ["current_db_order_id", "current_table", "current_customers"]:
            if hasattr(self, attr): delattr(self, attr)
        self.generate_order_id()

    def print_receipt(self, order_no, table_no, cust_no, cart_items, subtotal, discount, vat, net_total, word=None):
        if not os.path.exists("receipts"):
            os.makedirs("receipts")
        filename = f"receipt/{order_no}.txt"
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        receipt = f"============================================\n"
        receipt += f"ร้านอาหารเล็ก ๆ ของฉัน\n"
        receipt += f"============================================\n"
        receipt += f"เลขที่บิล : {order_no}\n"
        receipt += f"วันที่    : {now}\n"
        receipt += f"โต๊ะ      : {table_no}   |   ลูกค้า : {cust_no} ท่าน\n"
        receipt += f"--------------------------------------------\n"
        receipt += f"รายการอาหาร                  รวม(บาท)\n"
        receipt += f"--------------------------------------------\n"

        for item in cart_items:
            name = item['name'][:20]
            qty = item['qty']
            price_total = item['price'] * qty
            receipt += f"{name:<20} x{qty:<2} {price_total:>10,.2f}\n"

        receipt += f"--------------------------------------------\n"
        receipt += f"ยอดรวม (Subtotal) :       {subtotal:>10,.2f}\n"
        receipt += f"ส่วนลด (Discount) :       {discount:>10,.2f}\n"
        receipt += f"ภาษี 7% (VAT 7%)  :       {vat:>10,.2f}\n"
        receipt += f"ยอดสุทธิ (NET)    :       {net_total:>10,.2f}\n"
        receipt += f"============================================\n"
        word = ["ขอให้วันนี้เป็นวันที่ดี", "ขอบคุณที่ใช้บริการ", "ไว้แวะมาอุดหนุนใหม่นะคะ",
                "เพราะกำลังใจที่มีค่า มาจากคุณลูกค้า", "ขอให้สุขภาพแข็งแรงและประสบความสำเร็จในทุกสิ่ง"]
        receipt += f"{random.choice(word)}\n"
        receipt += f"============================================\n"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(receipt)

        print(f"พิมพ์ใบเสร็จสำเร็จ: {filename}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = POS_system()
    window.show()
    sys.exit(app.exec())