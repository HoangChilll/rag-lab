from importlib.metadata import version

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openrouter import ChatOpenRouter

def main() -> None:
    load_dotenv()
    print(f"LangChain Core Version: {version('langchain-core')}")
    print(f"LangGraph Version: {version('langgraph')}")
    llm = ChatOpenRouter(model="inclusionai/ling-3.2-flash:free", temperature=0)
    response = llm.invoke("say 'setup complete!' in one word")
    print(f"OpenRouter Response: {response.content}")



if __name__ == "__main__":
    main()
