import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)
from PySide6.QtCore import Qt
from ui_main import Ui_MainWindow
from db_manager import DBManager
from datetime import datetime
from cart import Cart
from menu_details import MenuItem, FoodNutrients, DrinkNutrients
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_profile_images()
        self.setup_button_icons()

        self.db = DBManager("D:/code/python/forproj2026/menu.db")
        self.cart = Cart()
        self.update_cart_count()

        # ================= MENU DATA =================
        self.menu_data = [
            # steak
            MenuItem("Garlic Pork Steak", 139, "image/steak_gp.jpg", "steak", ["Energetic"], FoodNutrients(520, 35, 5, 38)),
            MenuItem("Pepper Pork Steak", 139, "image/steak_bpp.jpg", "steak", ["Energetic", "Spicy & Awake"], FoodNutrients(500, 35, 5, 35)),
            MenuItem("Porkchop Steak", 169, "image/steak_pch.jpg", "steak", ["Energetic", "Comfort & Healing"], FoodNutrients(550, 35, 5, 40)),
            MenuItem("Spicy Grilled Chicken", 119, "image/steak_sgc.jpg", "steak", ["Spicy & Awake", "Energetic"], FoodNutrients(350, 35, 5, 18)),
            MenuItem("Teriyaki Chicken Steak", 119, "image/steak_tch.jpg", "steak", ["Energetic"], FoodNutrients(380, 35, 15, 20)),
            MenuItem("Ham Cheese Chicken Roll", 139, "image/steak_crwhac.jpg", "steak", ["Comfort & Healing", "Energetic"], FoodNutrients(450, 30, 15, 25)),
            MenuItem("Grilled Fish Steak", 139, "image/steak_gf.jpg", "steak", ["Healthy & Light", "Energetic"], FoodNutrients(300, 30, 5, 15)),
            MenuItem("Crispy Fish Steak", 129, "image/steak_ff.jpg", "steak", ["Energetic", "Comfort & Healing"], FoodNutrients(500, 25, 35, 28)),
            # burger
            MenuItem("Bacon Cheese Burger", 159, "image/burger_bc.jpg", "burger", ["Comfort & Healing", "Energetic"], FoodNutrients(680, 35, 45, 40)),
            MenuItem("Spicy Chicken Burger", 139, "image/burger_sc.jpg", "burger", ["Spicy & Awake", "Energetic"], FoodNutrients(520, 25, 48, 25)),
            MenuItem("Fish Burger", 139, "image/burger_fish.jpg", "burger", ["Energetic", "Healthy & Light"], FoodNutrients(450, 20, 45, 20)),
            MenuItem("Teriyaki Pork Burger", 149, "image/burger_tp.jpg", "burger", ["Energetic", "Comfort & Healing"], FoodNutrients(550, 28, 50, 25)),
            # pasta
            MenuItem("Spicy Seafood Spaghetti", 159, "image/pasta_sd.jpg", "pasta", ["Spicy & Awake", "Energetic"], FoodNutrients(450, 25, 55, 12)),
            MenuItem("Carbonara Spaghetti", 159, "image/pasta_c.jpg", "pasta", ["Comfort & Healing"], FoodNutrients(650, 20, 60, 35)),
            MenuItem("Seafood Tom Yum Spaghetti", 139, "image/pasta_sty.jpg", "pasta", ["Spicy & Awake", "Energetic"], FoodNutrients(480, 25, 58, 15)),
            # salad
            MenuItem("Tuna Salad", 159, "image/salad_tu.jpg", "salad", ["Healthy & Light"], FoodNutrients(250, 22, 10, 15)),
            MenuItem("Apple Salad", 139, "image/salad_ap.jpg", "salad", ["Healthy & Light", "Refreshing"], FoodNutrients(180, 2, 30, 6)),
            MenuItem("Fresh Veg Salad", 109, "image/salad_fv.jpg", "salad", ["Healthy & Light"], FoodNutrients(120, 3, 15, 5)),
            # snack
            MenuItem("French Fries", 69, "image/snack_ff.jpg", "snack", ["Joyful & Sharing", "Comfort & Healing"], FoodNutrients(365, 4, 45, 18)),
            MenuItem("Cheese Toast", 15, "image/snack_cb.jpg", "snack", ["Joyful & Sharing", "Comfort & Healing"], FoodNutrients(280, 10, 25, 15)),
            MenuItem("Mashed Potato", 55, "image/snack_mp.jpg", "snack", ["Comfort & Healing"], FoodNutrients(220, 4, 30, 10)),
            MenuItem("Fried Onion Rings", 59, "image/snack_fo.jpg", "snack", ["Joyful & Sharing", "Comfort & Healing"], FoodNutrients(400, 5, 45, 22)),
            MenuItem("Cheesy Spinach", 99, "image/snack_bswc.jpg", "snack", ["Comfort & Healing", "Joyful & Sharing"], FoodNutrients(320, 12, 10, 25)),
            # drink
            MenuItem("Cup of Coca-Cola", 30, "image/drink_cg.jpg", "drink", ["Refreshing", "Comfort & Healing"], DrinkNutrients(140, 39)),
            MenuItem("Jar of Coca-Cola", 90, "image/drink_cj.jpg", "drink", ["Joyful & Sharing", "Refreshing"], DrinkNutrients(420, 117)),
            MenuItem("Iced Lemon Tea", 40, "image/drink_lt.jpg", "drink", ["Refreshing", "Healthy & Light"], DrinkNutrients(120, 28)),
            MenuItem("Blue Hawaii Soda", 40, "image/drink_bhs.jpg", "drink", ["Refreshing", "Joyful & Sharing"], DrinkNutrients(140, 32)),
            MenuItem("Red Lime Soda", 40, "image/drink_rs.jpg", "drink", ["Refreshing", "Spicy & Awake"], DrinkNutrients(120, 29)),
            MenuItem("Passion Fruit Soda", 40, "image/drink_pfs.jpg", "drink", ["Refreshing", "Healthy & Light"], DrinkNutrients(130, 30)),
            MenuItem("A Bottle of Water", 10, "image/drink_water.jpg", "drink", ["Healthy & Light", "Refreshing"], DrinkNutrients(0, 0)),
            MenuItem("Cup of Ice", 2, "image/drink_ice.jpg", "drink"),

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
        self.ui.btn_checkout.clicked.connect(self.checkout_order)

 
        # เชื่อมปุ่มเพิ่ม/ลดรายการอาหาร
        self.ui.btn_add.clicked.connect(self.increase_qty)
        self.ui.btn_delete.clicked.connect(self.decrease_qty)
        self.ui.btn_add_to_cart.clicked.connect(self.add_to_cart)

        # โหลดเมนู
        self.load_menu()
        self.set_active_category(self.ui.btn_all)

        # Surprise Menu
        self.ui.btnSurprise.clicked.connect(self.surprise_me)


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
        image_path = os.path.join(base_path, item.image)

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
        name_label = QLabel(item.name)
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;
        """)

        # ================= ราคา =================
        price_label = QLabel(f"฿{item.price}")
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
            None: "ไฮไลท์",
            "steak": "สเต็ก",
            "burger": "เบอร์เกอร์",
            "pasta": "สปาเกตตี",
            "salad": "สลัด",
            "snack": "ของทานเล่น",
            "drink": "เครื่องดื่ม"
        }

        ##new
        title_text = category_name.get(category, "ทั้งหมด")

        if category is None:
            from datetime import datetime
            current_hour = datetime.now().hour
            if 13 <= current_hour <= 16:
                title_text = "Afternoon Boost: เมนูปลุกความสดชื่น!"
            elif current_hour >= 17:
                title_text = "Dinner Time: เมนูฮีลใจหลังเลิกงาน"

        self.ui.label_all_title.setText(title_text)

         # ================= ตั้งค่า grid =================
        grid.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        grid.setHorizontalSpacing(0)

        row = 0
        col = 0

        for item in self.menu_data:
            if category and item.category != category:
                continue

            if category is None:
                if 13 <= current_hour <= 16:
                    target_moods = ["Refreshing", "Spicy & Awake", "Energetic", "Healthy & Light"]
                    if not any(m in item.mood for m in target_moods):
                        continue
                elif current_hour >= 17:
                    target_moods = ["Comfort & Healing", "Joyful & Sharing"]
                    if not any(m in item.mood for m in target_moods):
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
        image_path = os.path.join(base_path, item.image)

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
        self.ui.label_food_name.setText(item.name)

        # ------------------ ตั้งราคา ------------------
        self.ui.label_food_price.setText(f"฿{item.price}")

        # ------------------ แสดง Moods/Nutritions ------------------
        self.ui.label_mood.setText(f"Mood: {item.get_mood_string()}")
        self.ui.label_nutri.setText(f"{item.get_nutrients_string()}")

        #------------------ ล้างข้อความเพิ่มเติม ------------------
        self.ui.textEdit_message.clear()

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
        items = self.cart.get_all_items()
        total_qty = sum(item["qty"] for item in items)
        total_price = self.cart.get_total_price()

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

        name = self.current_item.name
        price = self.current_item.price

        allergy_note = self.ui.textEdit_message.toPlainText().strip()
        if allergy_note:
            name = f"{name}\n({allergy_note})"

        self.cart.add_item(item_id=name, name=name, price=price, qty=self.current_qty)

        self.load_cart_page()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_home)

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

        items = self.cart.get_all_items()
        total_price = self.cart.get_total_price()

        for item in items:
            container = QWidget()
            hbox = QHBoxLayout(container)

            # ---------- รูป ----------
            image_file = "image/logo.png"
            for menu in self.menu_data:
                if menu.name in item["name"]:
                    image_file = menu.image
                    break

            img_label = QLabel()
            image_path = os.path.join(base_path, image_file)
            pixmap = QPixmap(image_path)
            img_label.setPixmap(pixmap.scaled(70, 70, Qt.KeepAspectRatio))

            # ---------- ชื่อ ----------
            name_label = QLabel(item["name"])

            # ---------- จำนวน ----------
            qty_label = QLabel(f"{item['qty']}  ")

            # ---------- ราคา ----------
            item_total = item["price"] * item["qty"]
            price_label = QLabel(f"฿{item_total}")

            # ---------- เพิ่ม-ลดในตะกร้า ----------
            from PySide6.QtWidgets import QPushButton

            btn_minus = QPushButton("-")
            btn_minus.setFixedSize(30, 30)
            btn_minus.setStyleSheet("background-color: #f2f2f2; font-weight: bold; font-size: 16px;")
            btn_minus.clicked.connect(lambda checked, item_id=item["id"]: self.adjust_cart_qty(item_id, -1))

            btn_plus = QPushButton("+")
            btn_plus.setFixedSize(30, 30)
            btn_plus.setStyleSheet("background-color: #f2f2f2; font-weight: bold; font-size: 16px;")
            btn_plus.clicked.connect(lambda checked, item_id=item["id"]: self.adjust_cart_qty(item_id, 1))


            # ---------- layout ----------
            hbox.addWidget(img_label)
            hbox.addWidget(name_label)
            hbox.addStretch()
            hbox.addWidget(btn_minus)
            hbox.addWidget(qty_label)
            hbox.addWidget(btn_plus)
            hbox.addWidget(price_label)
            layout.addWidget(container)

        layout.addStretch()
        self.ui.label_total_price.setText(f"฿{total_price:.2f}")

    def adjust_cart_qty(self, item_id, amount):
        if item_id in self.cart.items:
            self.cart.items[item_id]["qty"] += amount

            if self.cart.items[item_id]["qty"] <= 0:
                self.cart.remove_item(item_id)

        self.load_cart_page()

        if len(self.cart.get_all_items()) == 0:
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_home)

    def checkout_order(self):
        items = self.cart.get_all_items()
        if len(items) == 0:
            return

        table_no = "4"
        cust_no = 1

        existing_order = self.db.get_unpaid_order(table_no)
        if existing_order:
            # Merge the bills
            order_id = existing_order["order_id"]
            old_items = existing_order["items"]

            merged_dict = {}

            for old in old_items:
                name = old["menu_order"]
                merged_dict[name] = {
                    "name": name,
                    "price": old["price"],
                    "qty": old["qty"]
                }

            for new in items:
                name = new["name"]
                if name in merged_dict:
                    merged_dict[name]["qty"] += new["qty"]
                else:
                    merged_dict[name] = {
                        "name": name,
                        "price": new["price"],
                        "qty": new["qty"]
                    }

            final_items = list(merged_dict.values())
            new_total = sum(item["price"] * item["qty"] for item in final_items)

            success = self.db.update_existing_order(order_id, new_total, final_items, status="unpaid")

        else:
            # New bill
            total = self.cart.get_total_price()
            now = datetime.now()
            order_no = f"INV-{now.strftime('%Y%m%d-%H%M%S')}"

            success = self.db.save_order(order_no, table_no, cust_no, total, items, status="unpaid")

        if success:
            QMessageBox.information(self, "Success!", "ส่งอาหารไปยังครัวกลางเรียบร้อยแล้ว!")
            self.cart.clear_cart()
            self.load_cart_page()
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_home)
        else:
            QMessageBox.critical(self, "ข้อผิดพลาด", "ไม่สามารถบันทึกข้อมูลได้ กรุณาลองใหม่")

    ##new function##
    #surprise_menu
    def surprise_me(self):
        from PySide6.QtWidgets import QMessageBox, QInputDialog
        import random
        exclude_names = ["Ice", "Water"]

        # --- เลือกโหมดการสุ่ม ---
        msg_mode = QMessageBox(self)
        msg_mode.setWindowTitle("Surprise Me!")
        msg_mode.setText("เลือกอาหารแบบไหนดี?")
        btn_mood = msg_mode.addButton("ตามอารมณ์", QMessageBox.ActionRole)
        btn_combo = msg_mode.addButton("จัดเซ็ตคู่ (อาหารและเครื่องดื่ม)", QMessageBox.ActionRole)
        btn_any = msg_mode.addButton("อะไรก็ได้", QMessageBox.ActionRole)
        msg_mode.addButton("ยกเลิก", QMessageBox.RejectRole)
        msg_mode.exec()

        clicked_mode = msg_mode.clickedButton()

        # --- สุ่มตาม Mood ---
        if clicked_mode == btn_mood:
            mood_map = {
                "อยากฮีลใจ": "Comfort & Healing",
                "อยากเติมพลัง": "Energetic",
                "อยากกินแซ่บ ๆ ": "Spicy & Awake",
                "อยากคลีน": "Healthy",
                "อยากสดชื่น": "Refreshing",
                "อยากกินได้หลายคน": "Joyful & Sharing"
            }
            mood_choice, ok = QInputDialog.getItem(self, "Surprise Me", "วันนี้รู้สึกยังไง?", list(mood_map.keys()), 0, False)
            if ok:
                target = mood_map[mood_choice]
                match = [item for item in self.menu_data if target in item.mood and item.name not in exclude_names]
                self.show_surprise_result(match, f"สาย{mood_choice}")

        # --- สุ่มแบบจับคู่ ---
        elif clicked_mode == btn_combo:
            foods = [i for i in self.menu_data if i.category != "drink"]
            drinks = [i for i in self.menu_data if i.category == "drink" and i.name not in exclude_names]
            if foods and drinks:
                f = random.choice(foods)
                d = random.choice(drinks)
                QMessageBox.information(self, "Surprise Combo!",
                    f"เซ็ตแนะนำสำหรับคุณ:\n\n{f.name}\n{d.name}\n\nราคารวม: {f.price + d.price} บาท")
                self.open_detail_page(f)

        # --- อะไรก็ได้ ---
        elif clicked_mode == btn_any:
            filtered_all = [i for i in self.menu_data if i.name not in exclude_names]
            self.show_surprise_result(filtered_all, "แบบอะไรก็ได้")

    def show_surprise_result(self, items, criteria=""):
        import random
        from PySide6.QtWidgets import QMessageBox

        if items:
            lucky = random.choice(items)
            QMessageBox.information(self, "Found!", f"เมนูสุ่ม{criteria} สำหรับคุณคือ:\n\n{lucky.name} ")
            self.open_detail_page(lucky)
        else:
            QMessageBox.warning(self, "ขออภัย", "ไม่พบเมนูที่ตรงตามเงื่อนไข")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())