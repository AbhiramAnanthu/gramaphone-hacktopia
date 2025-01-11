from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")



