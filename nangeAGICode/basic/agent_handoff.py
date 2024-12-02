# 功能:将对话从一个Agent移交给另一个Agent

from swarm import Swarm, Agent
import os


os.environ["OPENAI_BASE_URL"] = "https://api.wlai.vip/v1"
os.environ["OPENAI_API_KEY"] = "sk-kFvJf1sAzdI2ArvhDoeBlkyvwy7v08pdMEcClT6xzA4JZYGz"


# 实例化Swarm
client = Swarm()

# 定义Agent
english_agent = Agent(
    name="English Agent",
    model="gpt-4o-mini",
    instructions="You only speak English.",
)

# 定义Agent
chinese_agent = Agent(
    name="Chinese Agent",
    model="gpt-4o-mini",
    instructions="You only speak Chinese.",
)


def transfer_to_chinese_agent():
    """立即移交给会说中文的Agent"""
    return chinese_agent


english_agent.functions.append(transfer_to_chinese_agent)

messages = [{"role": "user", "content": "你好！"}]
# messages = [{"role": "user", "content": "Hello！"}]

response = client.run(agent=english_agent, messages=messages)

print("response:",response)
print(response.messages[-1]["content"])
