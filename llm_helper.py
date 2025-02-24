from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-8b-instant")


if __name__ == "__main__":
    response = llm.invoke("How pets understand humans? ")
    print(response.content)





