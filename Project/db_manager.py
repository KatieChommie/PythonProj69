import sqlite3

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

    def fetch_some(self, table_name, category):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {table_name} WHERE {category}")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            return f"Error: {e}"


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