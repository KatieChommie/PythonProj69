import csv
import random
from datetime import datetime, timedelta

menu_mock = [
    # --- Steak ---
    {"name": "Garlic pork", "price": 139, "cal": 520, "p": 35, "c": 5, "f": 38, "s": 0},
    {"name": "Black pepper pork", "price": 139, "cal": 500, "p": 35, "c": 5, "f": 35, "s": 0},
    {"name": "Pork chop", "price": 169, "cal": 550, "p": 35, "c": 5, "f": 40, "s": 0},
    {"name": "Spicy Grilled Chicken", "price": 129, "cal": 350, "p": 35, "c": 5, "f": 18, "s": 0},
    {"name": "Teriyaki Chicken", "price": 129, "cal": 380, "p": 35, "c": 15, "f": 20, "s": 0},
    {"name": "Chicken roll with ham and cheese", "price": 149, "cal": 450, "p": 30, "c": 15, "f": 25, "s": 0},
    {"name": "Grilled fish", "price": 159, "cal": 300, "p": 30, "c": 5, "f": 15, "s": 0},
    {"name": "Fried fish", "price": 159, "cal": 500, "p": 25, "c": 35, "f": 28, "s": 0},

    # --- Burger ---
    {"name": "Bacon Cheese", "price": 189, "cal": 680, "p": 35, "c": 45, "f": 40, "s": 0},
    {"name": "Spicy Chicken", "price": 149, "cal": 520, "p": 25, "c": 48, "f": 25, "s": 0},
    {"name": "Fish Burger", "price": 139, "cal": 450, "p": 20, "c": 45, "f": 20, "s": 0},
    {"name": "Teriyaki Pork", "price": 159, "cal": 550, "p": 28, "c": 50, "f": 25, "s": 0},

    # --- Pasta ---
    {"name": "Seafood Drunk Pasta", "price": 179, "cal": 450, "p": 25, "c": 55, "f": 12, "s": 0},
    {"name": "Carbonara", "price": 159, "cal": 650, "p": 20, "c": 60, "f": 35, "s": 0},
    {"name": "Seafood Tom Yum", "price": 179, "cal": 480, "p": 25, "c": 58, "f": 15, "s": 0},

    # --- Salad ---
    {"name": "Tuna Salad", "price": 99, "cal": 250, "p": 22, "c": 10, "f": 15, "s": 0},
    {"name": "Apple Salad", "price": 89, "cal": 180, "p": 2, "c": 30, "f": 6, "s": 0},
    {"name": "Fresh Vegetable Salad", "price": 79, "cal": 120, "p": 3, "c": 15, "f": 5, "s": 0},

    # --- Snack ---
    {"name": "French Fries", "price": 59, "cal": 365, "p": 4, "c": 45, "f": 18, "s": 0},
    {"name": "Cheese Bread", "price": 69, "cal": 280, "p": 10, "c": 25, "f": 15, "s": 0},
    {"name": "Mashed Potatoes", "price": 59, "cal": 220, "p": 4, "c": 30, "f": 10, "s": 0},
    {"name": "Fried Onion", "price": 69, "cal": 400, "p": 5, "c": 45, "f": 22, "s": 0},
    {"name": "Spinach", "price": 79, "cal": 320, "p": 12, "c": 10, "f": 25, "s": 0},

    # --- Drink ---
    {"name": "Coke Glass", "price": 25, "cal": 140, "p": 0, "c": 0, "f": 0, "s": 39},
    {"name": "Coke Jug", "price": 60, "cal": 420, "p": 0, "c": 0, "f": 0, "s": 117},
    {"name": "Lemon Tea", "price": 35, "cal": 120, "p": 0, "c": 0, "f": 0, "s": 28},
    {"name": "Blue Hawaiian Soda", "price": 45, "cal": 140, "p": 0, "c": 0, "f": 0, "s": 32},
    {"name": "Red Soda", "price": 35, "cal": 120, "p": 0, "c": 0, "f": 0, "s": 29},
    {"name": "Passion Fruit Soda", "price": 45, "cal": 130, "p": 0, "c": 0, "f": 0, "s": 30},
    {"name": "Water", "price": 15, "cal": 0, "p": 0, "c": 0, "f": 0, "s": 0},
    {"name": "Ice", "price": 5, "cal": 0, "p": 0, "c": 0, "f": 0, "s": 0}
]

csv_filename = "daily_sales.csv"

with open(csv_filename, mode='a', newline='', encoding='utf-8-sig') as csv_file:
    fieldnames = ['Date', 'Order_ID', 'Table_No', 'Menu_Name', 'Price_Per_Unit', 'Qty', 'Total_Price', 'Cal', 'Protein',
                  'Carb', 'Fat', 'Sugar']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    print("กำลังเสกประวัติยอดขายย้อนหลัง 7 วัน...")

    for i in range(100):
        days_ago = random.randint(1, 7)
        base_date = datetime.now() - timedelta(days=days_ago)

        random_hour = random.randint(17, 21)
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59)

        random_time = base_date.replace(hour=random_hour, minute=random_minute, second=random_second)

        item = random.choice(menu_mock)
        qty = random.randint(1, 3)

        order_no = f"INV-{random_time.strftime('%Y%m%d-%H%M%S')}"
        table_no = str(random.randint(1, 10))

        writer.writerow({
            'Date': random_time.strftime("%Y-%m-%d %H:%M:%S"),
            'Order_ID': order_no,
            'Table_No': table_no,
            'Menu_Name': item['name'],
            'Price_Per_Unit': item['price'],
            'Qty': qty,
            'Total_Price': item['price'] * qty,
            'Cal': item['cal'] * qty,
            'Protein': item['p'] * qty,
            'Carb': item['c'] * qty,
            'Fat': item['f'] * qty,
            'Sugar': item['s'] * qty
        })

print(f"สร้างประวัติการสั่งสำเร็จ! ข้อมูลถูกเพิ่มลงใน {csv_filename} เรียบร้อยแล้ว")