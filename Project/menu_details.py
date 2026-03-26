
class FoodNutrients:
    def __init__(self, cal: int = 0, protein: int = 0, carbs: int = 0, fat: int = 0):
        self.cal = cal
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    def get_info_string(self):
        return f"Calories: {self.cal} kcal (Protein: {self.protein}g Carbs: {self.carbs}g Fats: {self.fat}g)"

class DrinkNutrients:
    def __init__(self, cal: int = 0, sugar: int = 0):
        self.cal = cal
        self.sugar = sugar

    def get_info_string(self):
        return f"Calories: {self.cal} kcal (Sugar: {self.sugar}g)"

class MenuItem:
    def __init__(self, name: str, price: float, image: str, category: str, mood: list = None, nutrients=None):
        self.name = name
        self.price = price
        self.image = image
        self.category = category
        self.mood = mood if mood else ["General"]
        self.nutrients = nutrients

    def get_mood_string(self):
        return ", ".join(self.mood)

    def get_nutrients_string(self):
        if self.nutrients:
            return self.nutrients.get_info_string()
        return "no nutrition data"