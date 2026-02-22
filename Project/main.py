import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QPushButton
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_profile_images()
        self.setup_button_icons()
        self.cart = []
        self.update_cart_count()


        # ================= MENU DATA =================
        self.menu_data = [
            # steak
            {"name": "Garlic pork", "price": 139, "image": "image/steak_gp.jpg", "category": "steak"},
            {"name": "Black pepper pork", "price": 139, "image": "image/steak_bpp.jpg", "category": "steak"},
            {"name": "Pork chop", "price": 169, "image": "image/steak_pch.jpg", "category": "steak"},
            {"name": "Spicy Grilled Chicken", "price": 119, "image": "image/steak_sgc.jpg", "category": "steak"},
            {"name": "Teriyaki Chicken", "price": 119, "image": "image/steak_tch.jpg", "category": "steak"},
            {"name": "Chicken roll with ham and cheese", "price": 139, "image": "image/steak_crwhac.jpg", "category": "steak"},
            {"name": "Grilled fish", "price": 139, "image": "image/steak_gf.jpg", "category": "steak"},
            {"name": "Fried fish", "price": 129, "image": "image/steak_ff.jpg", "category": "steak"},

            # burger
            {"name": "Bacon Cheese", "price": 159, "image": "image/burger_bc.jpg", "category": "burger"},
            {"name": "Spicy Chicken", "price": 139, "image": "image/burger_sc.jpg", "category": "burger"},
            {"name": "Fish Burger", "price": 139, "image": "image/burger_fish.jpg", "category": "burger"},
            {"name": "Teriyaki Pork", "price": 149, "image": "image/burger_tp.jpg", "category": "burger"},

            # pasta
            {"name": "Seafood Drunk Pasta", "price": 159, "image": "image/pasta_sd.jpg", "category": "pasta"},
            {"name": "Carbonara", "price": 159, "image": "image/pasta_c.jpg", "category": "pasta"},
            {"name": "Seafood Tom Yum", "price": 139, "image": "image/pasta_sty.jpg", "category": "pasta"},

            # salad
            {"name": "Tuna Salad", "price": 159, "image": "image/salad_tu.jpg", "category": "salad"},
            {"name": "Apple Salad", "price": 139, "image": "image/salad_ap.jpg", "category": "salad"},
            {"name": "Fresh Vegetable Salad", "price": 109, "image": "image/salad_fv.jpg", "category": "salad"},

            # snack
            {"name": "French Fries", "price": 69, "image": "image/snack_ff.jpg", "category": "snack"},
            {"name": "Cheese Bread", "price": 15, "image": "image/snack_cb.jpg", "category": "snack"},
            {"name": "Mashed Potatoes", "price": 55, "image": "image/snack_mp.jpg", "category": "snack"},
            {"name": "Fried Onion", "price": 59, "image": "image/snack_fo.jpg", "category": "snack"},
            {"name": "Baked Spinach with Cheese", "price": 99, "image": "image/snack_bswc.jpg", "category": "snack"},

            # drink
            {"name": "Coke Glass", "price": 30, "image": "image/drink_cg.jpg", "category": "drink"},
            {"name": "Coke Jug", "price": 90, "image": "image/drink_cj.jpg", "category": "drink"},
            {"name": "Lemon Tea", "price": 40, "image": "image/drink_lt.jpg", "category": "drink"},
            {"name": "Blue Hawaiian Soda", "price": 40, "image": "image/drink_bhs.jpg", "category": "drink"},
            {"name": "Red Soda", "price": 40, "image": "image/drink_rs.jpg", "category": "drink"},
            {"name": "Passion Fruit Soda", "price": 40, "image": "image/drink_pfs.jpg", "category": "drink"},
            {"name": "Water", "price": 10, "image": "image/drink_water.jpg", "category": "drink"},
            {"name": "Ice", "price": 2, "image": "image/drink_ice.jpg", "category": "drink"},
        ]

        # สร้างตัวแปรเก็บจำนวน
        self.current_item = None
        self.current_qty = 1

        # ปุ่ม category
        self.ui.btn_all.clicked.connect(
              lambda: (self.load_menu(), self.set_active_category(self.ui.btn_all))
        )

        self.ui.btn_steak.clicked.connect(
            lambda: (self.load_menu("steak"), self.set_active_category(self.ui.btn_steak))
        )

        self.ui.btn_burger.clicked.connect(
              lambda: (self.load_menu("burger"), self.set_active_category(self.ui.btn_burger))
        )

        self.ui.btn_pasta.clicked.connect(
            lambda: (self.load_menu("pasta"), self.set_active_category(self.ui.btn_pasta))
        )

        self.ui.btn_salad.clicked.connect(
            lambda: (self.load_menu("salad"), self.set_active_category(self.ui.btn_salad))
        )

        self.ui.btn_snack.clicked.connect(
            lambda: (self.load_menu("snack"), self.set_active_category(self.ui.btn_snack))
        )

        self.ui.btn_drink.clicked.connect(
            lambda: (self.load_menu("drink"), self.set_active_category(self.ui.btn_drink))
        )

        # ปุ่มกลับมาหน้า home
        self.ui.btn_detail_to_home.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_home)
        )

        self.ui.btn_cart_to_home.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_home)
        )

        # ปุ่มไปหน้า cart
        self.ui.btn_home_to_cart.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cart)
        )

 
        # เชื่อมปุ่มเพิ่ม/ลดรายกการอาหาร
        self.ui.btn_add.clicked.connect(self.increase_qty)
        self.ui.btn_delete.clicked.connect(self.decrease_qty)
        self.ui.btn_add_to_cart.clicked.connect(self.add_to_cart)

        # โหลดเมนู
        self.load_menu()
        self.set_active_category(self.ui.btn_all)

    # รูปแบบปุ่ม category
    def set_active_category(self, active_btn):

        # list ปุ่มทั้งหมด
        buttons = [
            self.ui.btn_all,
            self.ui.btn_steak,
            self.ui.btn_burger,
            self.ui.btn_pasta,
            self.ui.btn_salad,
            self.ui.btn_snack,
            self.ui.btn_drink
        ]

        # รีเซ็ตทุกปุ่มก่อน
        for btn in buttons:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    font-size: 13px;
                    padding: 6px 12px;
                }
                QPushButton:hover {
                    color: #e53935;
                }
            """)

        # ทำให้ปุ่มที่ถูกเลือกเป็นสีเทา
        active_btn.setStyleSheet("""
            QPushButton {
                background-color: #f2f2f2;
                font-weight: bold;
                font-size: 13px;
                padding: 6.5px 16px;
            }
        """)


    # ฟังก์ชันใส่รูป icon
    def setup_button_icons(self):
        from PySide6.QtGui import QIcon
        from PySide6.QtCore import QSize
        import os

        base_path = os.path.dirname(__file__)

        # ปุ่มกลับ
        self.ui.btn_detail_to_home.setIcon(
            QIcon(os.path.join(base_path, "image/cross.png"))
        )
        self.ui.btn_detail_to_home.setIconSize(QSize(24, 24))

        self.ui.btn_cart_to_home.setIcon(
            QIcon(os.path.join(base_path, "image/cross.png"))
        )
        self.ui.btn_cart_to_home.setIconSize(QSize(24, 24))

        # ปุ่มเพิ่ม
        self.ui.btn_add.setIcon(
            QIcon(os.path.join(base_path, "image/add.png"))
        )
        self.ui.btn_add.setIconSize(QSize(20, 20))

        # ปุ่มลบ
        self.ui.btn_delete.setIcon(
            QIcon(os.path.join(base_path, "image/delete.png"))
        )
        self.ui.btn_delete.setIconSize(QSize(20, 20))

    # รูป profile
    def setup_profile_images(self):
        from PySide6.QtGui import QPixmap
        from PySide6.QtCore import Qt
        import os

        base_path = os.path.dirname(__file__)

        # ----------------- Background -----------------
        bg_path = os.path.join(base_path, "image/background.jpg")
        bg_pixmap = QPixmap(bg_path)

        self.ui.label_background_shop.setPixmap(bg_pixmap)
        self.ui.label_background_shop.setScaledContents(True)

        # ----------------- Logo -----------------
        logo_path = os.path.join(base_path, "image/logo.png")
        logo_pixmap = QPixmap(logo_path)

        self.ui.label_logo_shop.setPixmap(
            logo_pixmap.scaled(
                120, 120,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )


    # ล้าง layout
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    
    # สร้าง widget เมนู 
    def create_menu_widget(self, item):
        from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
        from PySide6.QtGui import QIcon
        from PySide6.QtCore import Qt, QSize
        import os

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, item["image"])

        container = QWidget()
        container.setFixedWidth(150)
        container.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)

        vbox = QVBoxLayout(container)
        vbox.setSpacing(6)
        vbox.setContentsMargins(8,8,8,8)

        # ================= รูปเป็นปุ่ม =================
        img_button = QPushButton()
        img_button.setFixedSize(130,130)
        img_button.setIcon(QIcon(image_path))
        img_button.setIconSize(QSize(120,120))

        img_button.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: #f5f5f5;
            }
            QPushButton:hover {
                background-color: #f0d1cf;
            }
            QPushButton:pressed {
                background-color: #ffffff;
            }
        """)

        img_button.clicked.connect(
        lambda checked, i=item: self.open_detail_page(i)
        )

        # ================= ชื่อ =================
        name_label = QLabel(item["name"])
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;
        """)

        # ================= ราคา =================
        price_label = QLabel(f"฿{item['price']}")
        price_label.setAlignment(Qt.AlignCenter)
        price_label.setStyleSheet("""
            color: #e53935;
            font-size: 13px;
            font-weight: bold;
        """)


        vbox.addWidget(img_button, alignment=Qt.AlignCenter)
        vbox.addWidget(name_label)
        vbox.addWidget(price_label)

        return container


    # ----------------------------
    # โหลดเมนูทั้งหมด 2 คอลัมน์
    # ----------------------------
    def load_menu(self, category=None):
        grid = self.ui.gridLayout_all_item
        self.clear_layout(grid)

        # ================= ตั้งชื่อหัวข้อ =================
        category_name = {
            None: "ทั้งหมด",
            "steak": "สเต็ก",
            "burger": "เบอร์เกอร์",
            "pasta": "สปาเกตตี",
            "salad": "สลัด",
            "snack": "ของทานเล่น",
            "drink": "เครื่องดื่ม"
        }

        self.ui.label_all_title.setText(category_name.get(category, "ทั้งหมด"))

         # ================= ตั้งค่า grid =================
        grid.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        grid.setHorizontalSpacing(0)

        row = 0
        col = 0

        for item in self.menu_data:
            if category and item["category"] != category:
                continue

            widget = self.create_menu_widget(item)
            grid.addWidget(widget, row, col)

            col += 1
            if col == 2:
                col = 0
                row += 1


    # ----------------------------
    # เปิดหน้า detail
    # ----------------------------
    def open_detail_page(self, item):
        from PySide6.QtGui import QPixmap
        from PySide6.QtCore import Qt
        import os

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, item["image"])

        # ------------------ ตั้งค่ารูป ------------------
        pixmap = QPixmap(image_path)

        self.ui.label_food_image.setPixmap(
            pixmap.scaled(
                250, 250,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        # ------------------ ตั้งชื่อ ------------------
        self.ui.label_food_name.setText(item["name"])

        # ------------------ ตั้งราคา ------------------
        self.ui.label_food_price.setText(f"฿{item['price']}")

        # ------------------ เปลี่ยนหน้า ------------------
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_detail)
        

        self.current_item = item
        self.current_qty = 1
        self.ui.label_qty_list.setText("1")

    # เพิ่มจำนวนในหน้า detail
    def increase_qty(self):
        self.current_qty += 1
        self.ui.label_qty_list.setText(str(self.current_qty))


    # ลดจำนวนในหน้า detail
    def decrease_qty(self):
        if self.current_qty > 1:
            self.current_qty -= 1
            self.ui.label_qty_list.setText(str(self.current_qty))


    # จำนวนรายการอาหารทั้งหมด
    def update_cart_count(self):
        total_qty = sum(item["qty"] for item in self.cart)
        total_price = sum(item["price"] * item["qty"] for item in self.cart)

        # -------- หน้า HOME (ปุ่มเดียวรวมข้อความ) --------
        if total_qty == 0:
            self.ui.btn_home_to_cart.setText("0 รายการ | ฿0.00")
        else:
            self.ui.btn_home_to_cart.setText(
            f"{total_qty} รายการ | ฿{total_price:.2f}"
        )

        # -------- หน้า CART (แสดงแยก) --------
        self.ui.label_total_item.setText(f"{total_qty} รายการ")
        self.ui.label_total_price.setText(f"฿{total_price:.2f}")

    # เพิ่มรายการอาหารลงตะกร้า
    def add_to_cart(self):
        if not self.current_item:
            return

        name = self.current_item["name"]

        # ถ้ามีอยู่แล้วให้รวมจำนวน
        for item in self.cart:
            if item["name"] == name:
                item["qty"] += self.current_qty
                break
        else:
            # ถ้ายังไม่มี → เพิ่มใหม่
            self.cart.append({
                "name": self.current_item["name"],
                "price": self.current_item["price"],
                "image": self.current_item["image"],
                "qty": self.current_qty
            })

        self.load_cart_page()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_cart)

    # โหลด รายการที่เลือกทั้งหมด
    def load_cart_page(self):
        layout = self.ui.verticalLayout_cart
        self.clear_layout(layout)
        self.update_cart_count()

        from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
        from PySide6.QtGui import QPixmap
        from PySide6.QtCore import Qt
        import os

        base_path = os.path.dirname(__file__)

        total_price = 0

        for index, item in enumerate(self.cart):

            container = QWidget()
            hbox = QHBoxLayout(container)

            # ---------- รูป ----------
            img_label = QLabel()
            image_path = os.path.join(base_path, item["image"])
            pixmap = QPixmap(image_path)
            img_label.setPixmap(pixmap.scaled(70, 70, Qt.KeepAspectRatio))

            # ---------- ชื่อ ----------
            name_label = QLabel(item["name"])


            # ---------- จำนวน ----------
            qty_label = QLabel(f"x{item['qty']}  ")


            # ---------- ราคา ----------
            item_total = item["price"] * item["qty"]
            total_price += item_total
            price_label = QLabel(f"฿{item_total}")

            # ---------- layout ----------
            hbox.addWidget(img_label)
            hbox.addWidget(name_label)
            hbox.addStretch()
            hbox.addWidget(qty_label)
            hbox.addWidget(price_label)
            layout.addWidget(container)

        layout.addStretch()

        self.ui.label_total_price.setText(f"฿{total_price:.2f}")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())