class ValidationAgent:
    def validate(self, restaurant, items, budget_result):
        if restaurant is None:
            return False, "No suitable restaurant found"

        if budget_result["status"] != "PASS":
            return False, "Budget constraint failed"

        if not items:
            return False, "No items selected"

        return True, "Order validated successfully"
