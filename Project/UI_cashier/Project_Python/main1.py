import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt

#ไฟล์ที่แปลงมาจาก menu.ui
from ui_menu import Ui_MainWindow


#สร้างคลาสเมนู
class POSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        print("แอปกำลังเริ่มทำงาน.....")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbl_total.setText("0.00")
        self.menu_grid = self.ui.food_menu.widget().layout()

        #สั่งให้ Layout ดันปุ่มขึ้นไปแถวบนสุดเสมอ
        self.menu_grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        #เชื่อมปุ่ม หมวดหมู่
        self.ui.tbtn_all.clicked.connect(lambda: self.filter_menu("all"))
        self.ui.tbtn_cat_steak.clicked.connect(lambda: self.filter_menu("steak"))
        self.ui.tbtn_cat_burger.clicked.connect(lambda: self.filter_menu("burger"))
        self.ui.tbtn_cat_spaghetti.clicked.connect(lambda: self.filter_menu("spaghetti"))
        self.ui.tbtn_cat_salad.clicked.connect(lambda: self.filter_menu("salad"))
        self.ui.tbtn_cat_snack.clicked.connect(lambda: self.filter_menu("snack"))
        self.ui.tbtn_cat_drink.clicked.connect(lambda: self.filter_menu("drink"))

        #ข้อมูลเมนูอาหารทั้งหมด
        self.menu_items = {
            "btn_steak_garlic": {"name": "Garlic pork", "price": "139", "category": "steak", "img": "img/steak_garlic.jpg"},
            "btn_steak_pepper": {"name": "Black pepper pork", "price": "139", "category": "steak", "img": "img/steak_pepper.jpg"},
            "btn_steak_porkchop": {"name": "Pork chop", "price": "169", "category": "steak", "img": "img/steak_porkchop.jpeg"},
            "btn_steak_spicy": {"name": "Spicy Grilled Chicken", "price": "119", "category": "steak", "img": "img/steak_spicy.jpg"},
            "btn_steak_teriyaki": {"name": "Teriyaki Chicken", "price": "119", "category": "steak", "img": "img/steak_teriyaki.jpg"},
            "btn_steak_hamcheese": {"name": "Chicken roll with ham and cheese", "category": "steak", "price": "139", "img": "img/steak_hamcheese.jpg"},
            "btn_steak_grillfish": {"name": "Grilled fish", "price": "139", "category": "steak", "img": "img/steak_grillfish.jpeg"},
            "btn_steak_friedfish": {"name": "Fried fish", "price": "129", "category": "steak", "img": "img/steak_friedfish.jpg"},
            "btn_burger_bacon": {"name": "Bacon Cheese", "price": "159", "category": "burger", "img": "img/burger_bacon.jpg"},
            "btn_burger_spicy": {"name": "Spicy Chicken", "price": "139", "category": "burger", "img": "img/burger_spicy.jpeg"},
            "btn_burger_fish": {"name": "Fish", "price": "139", "category": "burger", "img": "img/burger_fish.jpg"},
            "btn_burger_teriyaki": {"name": "Teriyaki pork", "price": "149", "category": "burger", "img": "img/burger_teriyaki.jpg"},
            "btn_spaghetti_drunk": {"name": "Seafood drunk", "price": "159", "category": "spaghetti", "img": "img/spaghetti_drunk.jpg"},
            "btn_spaghetti_carbonara": {"name": "Carbonara", "price": "159", "category": "spaghetti", "img": "img/spaghetti_carbonara.jpg"},
            "btn_spaghetti_tomyum": {"name": "Seafood tom yum", "price": "139", "category": "spaghetti", "img": "img/spaghetti_tomyum.jpg"},
            "btn_salad_tuna": {"name": "Tuna", "price": "159", "category": "salad", "img": "img/salad_tuna.png"},
            "btn_salad_apple": {"name": "Apple", "price": "139", "category": "salad", "img": "img/salad_apple.jpg"},
            "btn_salad_vegetable": {"name": "Fresh vegetable", "category": "salad", "price": "109", "img": "img/salad_vegetable.jpg"},
            "btn_frenchfries": {"name": "French fries", "price": "69", "category": "snack", "img": "img/frenchfries.jpg"},
            "btn_bread": {"name": "Cheese bread", "price": "15", "category": "snack", "img": "img/bread.jpg"},
            "btn_potatoes": {"name": "Mashed potatoes", "price": "55", "category": "snack", "img": "img/potatoes.jpg"},
            "btn_onion": {"name": "Fried onion", "price": "59", "category": "snack", "img": "img/onion.jpg"},
            "btn_spinach": {"name": "Baked spinach with cheese", "category": "snack", "price": "99", "img": "img/spinach.jpg"},
            "btn_coke_glass": {"name": "Coke glass", "price": "30", "category": "drink", "img": "img/coke_glass.jpeg"},
            "btn_coke_jug": {"name": "Coke jug", "price": "90", "category": "drink", "img": "img/coke_jug.jpeg"},
            "btn_lemontea": {"name": "Lemon tea", "price": "40", "category": "drink", "img": "img/lemontea.jpg"},
            "btn_bluehawaiian": {"name": "Blue hawaiian soda", "price": "40", "category": "drink", "img": "img/bluehawaiian.png"},
            "btn_redsoda": {"name": "Red soda", "price": "40", "category": "drink", "img": "img/redsoda.jpg"},
            "btn_passionfruit": {"name": "Passion fruit soda", "price": "40", "category": "drink", "img": "img/passionfruit.jpg"},
            "btn_water": {"name": "Water", "price": "10", "category": "drink", "img": "img/water.jpeg"},
            "btn_ice": {"name": "ice", "price": "2", "category": "drink", "img": "img/ice.jpg"}
        }

        #เรียกใช้งานฟังก์ชัน
        self.setup_buttons()

    #ตั้งค่ารูปและข้อความ ปุ่มเมนูอาหาร
    def setup_buttons(self):

        #วนลูปตามชื่อปุ่ม
        for btn_name, data in self.menu_items.items():

            #ตรวจสอบว่าใน self.ui มีปุ่มชื่อนี้อยู่จริงไหม
            if hasattr(self.ui, btn_name):
                btn = getattr(self.ui, btn_name)

                #จัด format ของปุ่มอาหาร
                #รูปภาพอยู่บนข้อความ
                btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
                btn.setText(f"{data['name']}\n฿{data['price']}")

                #เช็กรูปภาพ
                image_path = data['img']
                if os.path.exists(image_path):
                    btn.setIcon(QIcon(image_path))
                    btn.setIconSize(QSize(100, 80))
                else:
                    print(f"หาไฟล์รูปไม่เจอ : {image_path} (เช็กชื่อไฟล์ในโฟลเดอร์ img อีกครั้ง)")

                #เชื่อมต่อการคลิก
                btn.clicked.connect(lambda ch=False, d=data: self.add_to_order(d))

    def filter_menu(self, category):
        #ล้างปุ่มออกจาก Grid ชั่วคราว เพื่อวางตำแหน่งเมนูใหม่
        for i in reversed(range(self.menu_grid.count())):
            widget = self.menu_grid.itemAt(i).widget()
            if widget:
                self.menu_grid.removeWidget(widget)

        #นำปุ่มอาหารที่ตรงกับหมวดหมู่มาวางใหม่
        row, col = 0, 0
        max_cols = 4

        #วน loop เช็กทุกปุ่มในเมนู
        for btn_name, data in self.menu_items.items():
            if hasattr(self.ui, btn_name):
                btn = getattr(self.ui, btn_name)

                #ถ้าหมวดหมู่ตรงกับอาหารในหมวดหมู่นั้น
                if category == "all" or data["category"] == category:
                    btn.show()
                    self.menu_grid.addWidget(btn, row, col)  #วางปุ่มเมนูในช่องที่ว่างอยู่
                    col += 1
                    if col >= max_cols:
                        col = 0
                        row += 1
                else:
                    btn.hide()

#สั่งให้โปรแกรมเริ่มทำงาน (run)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = POSApp()
    window.show()
    sys.exit(app.exec())