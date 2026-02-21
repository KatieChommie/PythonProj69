import sqlite3

from PySide6.QtWidgets import QMessageBox


class DBManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.tables = ["menus", "snacks", "burger", "pasta", "salad", "drinks"]

    def fetch_all(self, table_name):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            return f"Error: {e}"

    def get_menu_item(self, table_name, item_id):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(f"SELECT name, price FROM {table_name} WHERE id = ?", (item_id,))
                rows = cursor.fetchone()
                if rows:
                    return {"id": item_id, "name": rows["name"], "price": rows["price"]}
                return None
        except Exception as e:
            err_msg = QMessageBox()
            err_msg.setIcon(QMessageBox.Critical)
            err_msg.setText("Error!")
            err_msg.setWindowTitle("Error!")
            err_msg.exec_()
            return None


if __name__ == "__main__":

    db = DBManager("D:/code/python/forproj2026/menu.db")

    tables = ["menus", "snacks", "burger", "pasta", "salad", "drinks"]
    tb = int(input("1. Menus\n2. Snacks\n3. Burger\n4. Pasta\n5. Salad\n6. Drinks\nEnter the number: "))
    data = db.fetch_all(tables[tb-1])

    dr_cat = ["soft_drink", "juice", "water", "ice"]


    print("\n" + "=" * 50)
    if isinstance(data, list):
        print(f"พบข้อมูล {len(data)} รายการ จากหมวดหมู่ {tables[tb-1]}")
        for item in data:
            print(f"- {item['name']} ราคา {item['price']} บาท") #หมวดหมู่: {item['type']}
    else:
        print(data)
    print("=" * 50)