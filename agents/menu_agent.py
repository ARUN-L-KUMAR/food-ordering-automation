import json

class MenuAgent:
    def __init__(self, data_path="data/menu.json"):
        with open(data_path, "r") as f:
            self.data = json.load(f)

    def select_restaurant_and_items(self, food_type):
        for restaurant in self.data["restaurants"]:
            if restaurant["type"] == food_type:
                return restaurant

        return None
