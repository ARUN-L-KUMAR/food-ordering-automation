from agents.planner import PlannerAgent

def main():
    print("=== Food Ordering Automation System ===")

    people = int(input("Enter number of people: "))
    budget = int(input("Enter budget (INR): "))
    food_type = input("Food type (veg / non-veg): ")

    planner = PlannerAgent()
    plan = planner.plan(people, budget, food_type)

    print("\nGenerated Task Plan:")
    print(plan)

if __name__ == "__main__":
    main()
