from langchain_openai import ChatOpenAI
from .constant import *

# 豆包
Doubao = ChatOpenAI(
    model="ep-20251129230148-xzdpk",  # 替换为你的推理接入点 ID
    api_key=API_KEY_DOUBAO,
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    temperature=0,
)