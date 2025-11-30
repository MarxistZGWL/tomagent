from llm import Doubao
from tools import get_weather

def get_model():
    return Doubao

def get_tools():
    tools = []
    tools.append(get_weather)
    return tools

def get_sys_prompt():
    return "You are a helpful assistant"

model = get_model()
tools = get_tools()
sys_prompt = get_sys_prompt()