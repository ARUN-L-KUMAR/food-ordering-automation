class BudgetAgent:
    def check_budget(self, items, budget):
        total_cost = sum(
            item["price"] * item["quantity"] for item in items
        )

        if total_cost <= budget:
            return {
                "status": "PASS",
                "total_cost": total_cost
            }
        else:
            return {
                "status": "FAIL",
                "total_cost": total_cost
            }
