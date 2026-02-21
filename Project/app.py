import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QDialog, QMessageBox
from PySide6.QtGui import QIcon
from ui_menu import Ui_MainWindow
from ui_table import Ui_TableWindow
from ui_payment import Ui_PaymentWindow
from db_manager import DBManager
from cart import Cart

class POS_system(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = DBManager("D:/code/python/forproj2026/menu.db")
        self.cart = Cart()

        #image-steak
        self.ui.btn_steak_garlic.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_garlic.jpg"))
        self.ui.btn_steak_garlic.setIconSize(QSize(110, 100))
        self.ui.btn_steak_pepper.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_pepper.jpg"))
        self.ui.btn_steak_pepper.setIconSize(QSize(110, 100))
        self.ui.btn_steak_porkchop.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_porkchop.jpeg"))
        self.ui.btn_steak_porkchop.setIconSize(QSize(110, 100))
        self.ui.btn_steak_spicy.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_spicy.jpg"))
        self.ui.btn_steak_spicy.setIconSize(QSize(110, 100))
        self.ui.btn_steak_teriyaki.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_teriyaki.jpg"))
        self.ui.btn_steak_teriyaki.setIconSize(QSize(110, 100))
        self.ui.btn_steak_hamcheese.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_hamcheese.jpg"))
        self.ui.btn_steak_hamcheese.setIconSize(QSize(110, 100))
        self.ui.btn_steak_grillfish.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_grillfish.jpeg"))
        self.ui.btn_steak_grillfish.setIconSize(QSize(110, 100))
        self.ui.btn_steak_friedfish.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/steak_friedfish.jpg"))
        self.ui.btn_steak_friedfish.setIconSize(QSize(110, 100))
        #image-burger
        self.ui.btn_burger_bacon.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/burger_bacon.jpg"))
        self.ui.btn_burger_bacon.setIconSize(QSize(110, 100))
        self.ui.btn_burger_spicy.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/burger_spicy.jpeg"))
        self.ui.btn_burger_spicy.setIconSize(QSize(110, 100))
        self.ui.btn_burger_fish.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/burger_fish.jpg"))
        self.ui.btn_burger_fish.setIconSize(QSize(110, 100))
        self.ui.btn_burger_teriyaki.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/burger_teriyaki.jpg"))
        self.ui.btn_burger_teriyaki.setIconSize(QSize(110, 100))
        #image-spaghetti
        self.ui.btn_spaghetti_drunk.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/spaghetti_drunk.jpg"))
        self.ui.btn_spaghetti_drunk.setIconSize(QSize(110, 100))
        self.ui.btn_spaghetti_carbonara.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/spaghetti_carbonara.jpg"))
        self.ui.btn_spaghetti_carbonara.setIconSize(QSize(110, 100))
        self.ui.btn_spaghetti_tomyum.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/spaghetti_tomyum.jpg"))
        self.ui.btn_spaghetti_tomyum.setIconSize(QSize(110, 100))
        #image-salad
        self.ui.btn_salad_tuna.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/salad_tuna.png"))
        self.ui.btn_salad_tuna.setIconSize(QSize(110, 100))
        self.ui.btn_salad_apple.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/salad_apple.jpg"))
        self.ui.btn_salad_apple.setIconSize(QSize(110, 100))
        self.ui.btn_salad_vegetable.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/salad_vegetable.jpg"))
        self.ui.btn_salad_vegetable.setIconSize(QSize(110, 100))
        #image-snacks
        self.ui.btn_frenchfries.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/frenchfries.jpg"))
        self.ui.btn_frenchfries.setIconSize(QSize(110, 100))
        self.ui.btn_bread.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/bread.jpg"))
        self.ui.btn_bread.setIconSize(QSize(110, 100))
        self.ui.btn_potatoes.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/potatoes.jpg"))
        self.ui.btn_potatoes.setIconSize(QSize(110, 100))
        self.ui.btn_onion.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/onion.jpg"))
        self.ui.btn_onion.setIconSize(QSize(110, 100))
        self.ui.btn_spinach.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/spinach.jpg"))
        self.ui.btn_spinach.setIconSize(QSize(110, 100))
        #image-drinks
        self.ui.btn_coke_glass.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/coke_glass.jpeg"))
        self.ui.btn_coke_glass.setIconSize(QSize(110, 100))
        self.ui.btn_coke_jug.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/coke_jug.jpeg"))
        self.ui.btn_coke_jug.setIconSize(QSize(110, 100))
        self.ui.btn_lemontea.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/lemontea.jpg"))
        self.ui.btn_lemontea.setIconSize(QSize(110, 100))
        self.ui.btn_bluehawaiian.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/bluehawaiian.png"))
        self.ui.btn_bluehawaiian.setIconSize(QSize(110, 100))
        self.ui.btn_redsoda.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/redsoda.jpg"))
        self.ui.btn_redsoda.setIconSize(QSize(110, 100))
        self.ui.btn_passionfruit.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/passionfruit.jpg"))
        self.ui.btn_passionfruit.setIconSize(QSize(110, 100))
        self.ui.btn_water.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/water.jpeg"))
        self.ui.btn_water.setIconSize(QSize(110, 100))
        self.ui.btn_ice.setIcon(QIcon("D:/code/python/pythonProject/05016385/Project/img/ice.jpg"))
        self.ui.btn_ice.setIconSize(QSize(110, 100))

        #category actions
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


        #button actions
        self.ui.btn_steak_garlic.clicked.connect(lambda: self.add_to_cart(1, "Garlic Pork Steak", 139))

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

    def add_to_cart(self, item_id, name, price):
        self.cart.add_item(item_id, name, price, qty=1)
        self.update_ui()

    def update_ui(self):
        items = self.cart.get_all_items()
        self.ui.order.setRowCount(len(items))

        for row_index, item in enumerate(items):
            self.ui.order.setItem(row_index, 0, QTableWidgetItem(item["name"]))
            self.ui.order.setItem(row_index, 1, QTableWidgetItem(str(item["qty"])))

            total_price = item["price"] * item["qty"]
            self.ui.order.setItem(row_index, 2, QTableWidgetItem(str(total_price)))

        total = self.cart.get_total_price()
        self.ui.lbl_total.setText(f"{total:,.2f}")

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
            err_msg.exec_()
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

    def open_payment_window(self):
        if len(self.cart.get_all_items()) == 0:
            print("error")
            return
        self.payment_window = QDialog()
        self.ui_payment = Ui_PaymentWindow()
        self.ui_payment.setupUi(self.payment_window)
        total = self.cart.get_total_price()
        self.ui_payment.label_total.setText(f"{total:,.2f}")
        self.payment_window.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = POS_system()
    window.show()
    sys.exit(app.exec())