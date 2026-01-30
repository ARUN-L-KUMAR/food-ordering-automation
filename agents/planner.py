import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

class PlannerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="deepseek/deepseek-r1",  # FREE on OpenRouter
            temperature=0,
            base_url="https://openrouter.ai/api/v1"
        )

        with open("prompts/planner_prompt.txt") as f:
            template = f.read()

        self.prompt = ChatPromptTemplate.from_template(template)

    def plan(self, people: int, budget: int, food_type: str):
        response = self.llm.invoke(
            self.prompt.format_messages(
                people=people,
                budget=budget,
                food_type=food_type
            )
        )

        return json.loads(response.content)
