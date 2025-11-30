from langchain.agents import create_agent
from langchain_core.messages import message_to_dict
from conf import model, tools, sys_prompt

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=sys_prompt,
)

result = agent.invoke({"messages": [{"role": "user", "content": "杭州天气怎么样？"}]})

msgs = result['messages']
answer = message_to_dict(msgs[-1])['data']['content']
print(answer)
