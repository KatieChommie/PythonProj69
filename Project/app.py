import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QDialog
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

        #buttons commands
        self.ui.btn_burger_bacon.clicked.connect(lambda: self.add_to_cart(1, "Bacon Cheese Burger", 159))
        self.ui.btn_burger_spicy.clicked.connect(lambda: self.add_to_cart(2, "Spicy Chicken Burger", 139))
        self.ui.btn_coke_jug.clicked.connect(lambda: self.add_to_cart(3, "Jar of Coca-Cola", 90))

        self.ui.pbtn_table.clicked.connect(self.open_table_window)
        self.ui.pbtn_pay.clicked.connect(self.open_payment_window)

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
        self.ui.label_total.setText(f"{total:,.2f}")

    def open_table_window(self):
        self.table_window = QWidget()
        self.ui_table = Ui_TableWindow()
        self.ui_table.setupUi(self.table_window)
        self.table_window.show()

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