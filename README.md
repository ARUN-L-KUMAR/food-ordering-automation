# Food Ordering Automation System 🍽️

An intelligent multi-agent system for automating food orders based on user requirements like number of people, budget, and food preferences. Built using LangChain and LangGraph with AI-powered decision making.

## 🌟 Features

- **AI-Powered Planning**: Automatically breaks down food ordering into structured subtasks
- **Multi-Agent Architecture**: Specialized agents for different aspects of order processing
- **Budget Management**: Ensures orders stay within specified budget constraints
- **Menu Intelligence**: Smart menu item selection based on preferences and constraints
- **Quantity Optimization**: Calculates optimal quantities for group orders
- **Order Validation**: Validates orders before final submission
- **Free LLM Integration**: Uses DeepSeek-R1 model via OpenRouter (free tier)

## 🏗️ Architecture

The system follows a multi-agent architecture with specialized agents:

- **Planner Agent**: Breaks down the ordering task into sequential subtasks
- **Menu Agent**: Handles restaurant and menu item selection
- **Quantity Agent**: Calculates optimal food quantities for the group
- **Budget Agent**: Manages budget constraints and cost optimization
- **Validation Agent**: Validates the complete order before processing
- **Execution Agent**: Executes the final order
- **Coordinator**: Orchestrates communication between all agents

## 📋 Prerequisites

- Python 3.8+
- OpenRouter API Key (for free DeepSeek-R1 model access)
- Internet connection for API calls

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/ARUN-L-KUMAR/food-ordering-automation.git
cd food-ordering-automation
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the root directory:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

To get a free OpenRouter API key:
- Visit [OpenRouter.ai](https://openrouter.ai/)
- Sign up for a free account
- Generate an API key from your dashboard

## 💻 Usage

Run the application:
```bash
python main.py
```

You'll be prompted to enter:
- Number of people
- Budget (in INR)
- Food type preference (veg/non-veg)

Example interaction:
```
=== Food Ordering Automation System ===
Enter number of people: 5
Enter budget (INR): 1000
Food type (veg / non-veg): veg

Generated Task Plan:
{
  "tasks": [
    "select_restaurant",
    "select_menu_items",
    "calculate_quantity",
    "check_budget",
    "validate_order"
  ]
}
```

## 📁 Project Structure

```
Food_Ordering/
├── agents/                    # Agent implementations
│   ├── __init__.py
│   ├── planner.py            # Task planning agent
│   ├── menu_agent.py         # Menu selection agent
│   ├── quantity_agent.py     # Quantity calculation agent
│   ├── budget_agent.py       # Budget management agent
│   ├── validation_agent.py   # Order validation agent
│   ├── execution_agent.py    # Order execution agent
│   └── coordinator.py        # Agent coordinator
├── config/                    # Configuration files
│   └── settings.py
├── data/                      # Data files
│   └── menu.json             # Restaurant menu database
├── graph/                     # LangGraph definitions
│   ├── __init__.py
│   └── agent_graph.py        # Agent workflow graph
├── prompts/                   # LLM prompts
│   └── planner_prompt.txt    # Planner agent prompt
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🍴 Menu Database

The system includes a sample menu database (`data/menu.json`) with restaurants and items:

- **A2B Veg Restaurant** (Vegetarian)
  - Veg Meals: ₹180
  - Paneer Butter Masala: ₹220

- **SS Hyderabad** (Non-Vegetarian)
  - Chicken Biryani: ₹250
  - Chicken 65: ₹180

You can extend the menu by adding more restaurants and items to the JSON file.

## 🔧 Technologies Used

- **LangChain**: Framework for building LLM applications
- **LangGraph**: Framework for building multi-agent workflows
- **DeepSeek-R1**: Free reasoning model via OpenRouter
- **Python-dotenv**: Environment variable management
- **Pydantic**: Data validation
- **JSON**: Data storage and exchange

## 🛠️ Development Status

This is a Final Year Project currently under development. The following components are implemented:

- ✅ Planner Agent
- ✅ Menu Database
- ✅ Basic CLI Interface
- ✅ LLM Integration (DeepSeek-R1)
- 🚧 Menu Agent (In Progress)
- 🚧 Budget Agent (In Progress)
- 🚧 Quantity Agent (In Progress)
- 🚧 Validation Agent (In Progress)
- 🚧 Execution Agent (In Progress)
- 🚧 Agent Graph Workflow (In Progress)

## 🤝 Contributing

This is an academic project. Suggestions and feedback are welcome!

## 📝 License

This project is developed as a Final Year Project for educational purposes.

## 👨‍💻 Author

**Arun L Kumar**
- GitHub: [@ARUN-L-KUMAR](https://github.com/ARUN-L-KUMAR)

## 🙏 Acknowledgments

- LangChain and LangGraph communities
- OpenRouter for providing free access to DeepSeek-R1
- All contributors and supporters of this project

---

**Note**: This is an academic project for learning and demonstration purposes. For production use, additional features like error handling, logging, authentication, and comprehensive testing should be implemented.
