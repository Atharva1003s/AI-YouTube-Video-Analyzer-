# Importing Agents
from agno.agent import Agent


# Importing Models
from agno.models.groq import Groq


# Importing Web Search Tools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.websearch import WebSearchTools
from agno.tools.yfinance import YFinanceTools

# Importing API Keys
from dotenv import load_dotenv
load_dotenv()

def build_agent(self):
    return Agent(
        model = Groq(id = "llama-3.3-70b-versatile"),
        markdown=True,
        tools=[YFinanceTools(all=True)],
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible."],

       
        
    )


groq_agent = build_agent(None)


if __name__ == "__main__":
    # --- Sync ---
    groq_agent.print_response("Share the NVDA stock price and analyst recommendations")
    