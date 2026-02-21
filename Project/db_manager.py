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
            print("Error")
            return None

    def save_order(self, table_no, cust_no, total, cart_items, status="paid"):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                cursor.execute(
                    "INSERT INTO orders (table_no, cust_no, total, status) VALUES (?, ?, ?, ?)",
                    (str(table_no), int(cust_no), float(total), status)
                )

                new_order_id = cursor.lastrowid

                for item in cart_items:
                    cursor.execute(
                        "INSERT INTO order_item (order_id, menu_order, qty, price) VALUES (?, ?, ?, ?)",
                        (new_order_id, item["name"], item["qty"], item["price"])
                    )

                print("Successfully")
                return True

        except Exception as e:
            print("Error")
            return False
