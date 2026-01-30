class QuantityAgent:
    def calculate_quantities(self, items, people):
        # Simple rule: 1 item per person
        selected_items = []

        for item in items:
            selected_items.append({
                "name": item["name"],
                "price": item["price"],
                "quantity": people
            })

        return selected_items
