from langchain.agents import create_agent
from langchain_core.messages import message_to_dict
from conf import model, tools, sys_prompt
import json


agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=sys_prompt,
)

def ask_agent(agent, user_msg):
    resp = agent.invoke({"messages": [{"role": "user", "content": user_msg}]})
    last_msg = message_to_dict(resp['messages'][-1])
    return last_msg

def main():
    while True:
        user_input = input("Ask any question: ")
        if user_input.strip().lower() in ("exit", "quit"):
            print("再见 👋")
            break
        answer = ask_agent(agent, user_input)['data']['content']
        print(answer)
    
if __name__ == "__main__":
    main()
