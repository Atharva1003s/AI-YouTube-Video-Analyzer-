# Importing Team
from agno.team import Team


# Importing Agents
from agno.agent import Agent


# Importing Models
from agno.models.groq import Groq


# Importing Web Search Tools
# from agno.tools.duckduckgo import DuckDuckGoTools
# from agno.tools.websearch import WebSearchTools
# from agno.tools.yfinance import YFinanceTools

# Importing API Keys
from dotenv import load_dotenv
load_dotenv()



# Defining different Agents
english_agent = Agent(name="English Agent", role="You answer questions in English")
chineese_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")
hindi_agent = Agent(name="Hindi Agent", role="You answer questions in Hindi")




# Building Team
team = Team(
    name = "Answer & Translation Team",
    role = "You are a team of translation experts that can translate text between different languages.",
    members = [english_agent , chineese_agent , hindi_agent],
    model = Groq(id = "llama-3.3-70b-versatile"),
    markdown=True,
    show_members_responses=True,
    instructions = "All members should respond to the question in their respective languages.Do not pick only one member to answer the question. ",
)











# In response the agent not translates and give anwer because agent picks the best translation agent and give answer in that language. For example if the question is in Hindi then the agent will pick the Hindi agent and give answer in Hindi. If the question is in English then the agent will pick the English agent and give answer in English. If the question is in Chinese then the agent will pick the Chinese agent and give answer in Chinese.
if __name__ == "__main__":
    # --- Sync ---
    team.print_response("What is the capital of India")