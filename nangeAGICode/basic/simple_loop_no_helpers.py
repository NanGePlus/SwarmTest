# 简单交互测试

from swarm import Swarm, Agent
import os


os.environ["OPENAI_BASE_URL"] = "https://api.wlai.vip/v1"
os.environ["OPENAI_API_KEY"] = "sk-kFvJf1sAzdI2ArvhDoeBlkyvwy7v08pdMEcClT6xzA4JZYGz"


# 实例化
client = Swarm()


# 定义Agent
my_agent = Agent(
    name="Agent",
    model="gpt-4o-mini",
    instructions="You are a helpful agent.",
)


def pretty_print_messages(messages):
    for message in messages:
        if message["content"] is None:
            continue
        print(f"{message['sender']}: {message['content']}")


messages = []
agent = my_agent


while True:
    user_input = input("> ")
    messages.append({"role": "user", "content": user_input})

    response = client.run(agent=agent, messages=messages)
    messages = response.messages
    agent = response.agent
    pretty_print_messages(messages)
