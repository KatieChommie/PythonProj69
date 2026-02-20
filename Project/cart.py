class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, price, qty = 1):
        if item_id in self.items:
            self.items[item_id]["qty"] += qty
        else:
            self.items[item_id] = {
                "name": name,
                "price": price,
                "qty": qty
            }
        print(f"{name} is added!")

    def remove_item(self, item_id):
        if item_id in self.items:
            removed_name = self.items[item_id]["name"]
            del self.items[item_id]
            print(f"deleted {removed_name}")

    def get_total_price(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["qty"]
        return total

    def clear_cart(self):
        self.items.clear()
        print("cleared")

    def get_all_items(self):
        result_list = []

        for key, val in self.items.items():
            item_data = {
                "id": key,
                "name": val["name"],
                "price": val["price"],
                "qty": val["qty"]
            }
            result_list.append(item_data)

        return result_list