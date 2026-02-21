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

    def get_all_orders(self):
        try:
            import sqlite3
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM "orders" ORDER BY "id" DESC')
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            print(f"Error fetching history: {e}")
            return []

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
            print(f"Database Error: {e}")
            return False

    def get_unpaid_order(self, table_no):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()

                cursor.execute(
                    'SELECT "id", "order_no" FROM "orders" WHERE "table_no" = ? AND "status" = "unpaid" ORDER BY "id" DESC LIMIT 1',
                    (str(table_no),))

                order = cursor.fetchone()
                if order:
                    order_id = order["id"]
                    order_no = order["order_no"]
                    cursor.execute("SELECT menu_order, qty, price FROM order_item WHERE order_id = ?",
                                   (order_id,))
                    items = cursor.fetchall()

                    return {"order_id": order_id, "order_no": order_no, "items": [dict(i) for i in items]}
                return None
        except Exception as e:
            print(f"Error fetching unpaid order: {e}")
            return None

    def update_order_status(self, order_id, status="paid"):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE "orders" SET "status" = ? WHERE "id" = ?', (status, order_id))
                return True
        except Exception as e:
            print(f"Error updating status: {e}")
            return False

    def save_order(self, order_no, table_no, cust_no, total, cart_items, status = "paid"):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO orders (order_no, table_no, cust_no, total, status) VALUES (?, ?, ?, ?, ?)",
                    (order_no, str(table_no), int(cust_no), float(total), status)
                )
                new_order_id = cursor.lastrowid
                for item in cart_items:
                    cursor.execute(
                'INSERT INTO "order_item" (order_id, menu_order, qty, price) VALUES (?, ?, ?, ?)',
                (new_order_id, item["name"], item["qty"], item["price"])
                    )
                return True
        except Exception as e:
            print(f"Database Error (save_order): {e}")
            return False

    def update_existing_order(self, order_id, total, cart_items, status):
        try:
            import sqlite3
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                cursor.execute('UPDATE "orders" SET "total" = ?, "status" = ? WHERE "id" = ?',
                               (float(total), status, order_id))

                cursor.execute('DELETE FROM "order_item" WHERE "order_id" = ?', (order_id,))

                for item in cart_items:
                    cursor.execute(
                        'INSERT INTO "order_item" (order_id, menu_order, qty, price) VALUES (?, ?, ?, ?)',
                        (order_id, item["name"], item["qty"], item["price"])
                    )
                return True
        except Exception as e:
            print(f"Error updating existing order: {e}")
            return False
