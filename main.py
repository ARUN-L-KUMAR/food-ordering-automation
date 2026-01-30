from agents.planner import PlannerAgent
from agents.menu_agent import MenuAgent
from agents.quantity_agent import QuantityAgent
from agents.budget_agent import BudgetAgent
from agents.validation_agent import ValidationAgent

def main():
    print("=== Food Ordering Automation (Stage 6) ===")

    people = int(input("Enter number of people: "))
    budget = int(input("Enter budget (INR): "))
    food_type = input("Food type (veg / non-veg): ")

    # Initialize agents
    planner = PlannerAgent()
    menu_agent = MenuAgent()
    quantity_agent = QuantityAgent()
    budget_agent = BudgetAgent()
    validation_agent = ValidationAgent()

    # Planner
    plan = planner.plan(people, budget, food_type)
    print("\nPlanner Output:", plan)

    # Menu selection
    restaurant = menu_agent.select_restaurant_and_items(food_type)
    print("\nSelected Restaurant:", restaurant["name"])

    # Quantity calculation
    items_with_quantity = quantity_agent.calculate_quantities(
        restaurant["items"], people
    )
    print("\nItems with Quantity:", items_with_quantity)

    # Budget check
    budget_result = budget_agent.check_budget(
        items_with_quantity, budget
    )
    print("\nBudget Check:", budget_result)

    # Validation
    is_valid, message = validation_agent.validate(
        restaurant, items_with_quantity, budget_result
    )

    print("\nValidation Result:", message)

    if is_valid:
        print("\n✅ Order can be processed")
    else:
        print("\n❌ Order rejected")

if __name__ == "__main__":
    main()
