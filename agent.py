# Importing Agents
from agno.agent import Agent


# Importing Models
from agno.models.groq import Groq


# Importing Web Search Tools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.websearch import WebSearchTools

# Importing API Keys
from dotenv import load_dotenv
load_dotenv()


# Importing Memory Models
from agno.db.sqlite import SqliteDb




# Defining the database for memory
db = SqliteDb(db_file="agno.db")


db.clear_memories() 

def build_agent(self):
    return Agent(
        model = Groq(id = "llama-3.3-70b-versatile"),
        markdown=True,
        instructions="You are a helpful Travel Agent. You will answer questions about travel, destinations, and provide recommendations based on user queries.",
        add_datetime_to_context=True,
        # tools=[DuckDuckGoTools()],
        
        description="You are an AI agent that can generate audio using the DesiVocal API.",
        db = db,
        add_history_to_context=True,
        enable_user_memories=True,
        enable_session_summaries=True
    )


groq_agent = build_agent(None)


user_id = "atharva@gmail.com"

if __name__ == "__main__":
    # --- Sync ---
    groq_agent.print_response("What is the FIFA World Cup 2026 Final schedule?" , user_id=user_id)
    groq_agent.print_response("Who is the host country for FIFA World Cup 2026?" , user_id=user_id)
    


memory = groq_agent.get_user_memories(user_id=user_id)   

print(f"User Memories for user id {user_id}: {memory}")