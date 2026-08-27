import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

def create_model():
    """
    creatre and return the configured chat model
    
    """
    api_key=os.getenv("GROQ_API_KEY")
    model_name=os.getenv("MODEL_NAME","openai/gpt-oss-120b")
    model_provider=os.getenv("MODEL_PROVIDER","groq")
   
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in the .env file.")
    llm=init_chat_model(model=model_name,model_provider=model_provider,
                        api_key=api_key)
    return llm
    

