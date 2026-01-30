import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from config.settings import llm


class PlannerAgent:
    def __init__(self):
        self.parser = JsonOutputParser()

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a task planning agent."),
            ("human",
             """
             Create a task plan for food ordering automation.

             Inputs:
             - People: {people}
             - Budget: {budget}
             - Food Type: {food_type}

             Return ONLY valid JSON in this format:
             {{
               "tasks": ["select_restaurant", "select_menu_items", "calculate_quantity", "check_budget", "validate_order"]
             }}
             """)
        ])

    def plan(self, people, budget, food_type):
        chain = self.prompt | llm | self.parser

        return chain.invoke({
            "people": people,
            "budget": budget,
            "food_type": food_type
        })
