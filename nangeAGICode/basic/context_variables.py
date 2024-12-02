# 功能:在Agent中使用上下文变量

from swarm import Swarm, Agent
import os


os.environ["OPENAI_BASE_URL"] = "https://api.wlai.vip/v1"
os.environ["OPENAI_API_KEY"] = "sk-kFvJf1sAzdI2ArvhDoeBlkyvwy7v08pdMEcClT6xzA4JZYGz"



# 实例化
client = Swarm()


# 定义instructions
def instructions(context_variables):
    name = context_variables.get("name", "User")
    return f"You are a helpful agent. Greet the user by name ({name})."


# 定义Function
def print_account_details(context_variables: dict):
    user_id = context_variables.get("user_id", None)
    name = context_variables.get("name", None)
    print(f"Account Details: {name} {user_id}")
    return "Success"


# 定义Agent
agent = Agent(
    name="Agent",
    model="gpt-4o-mini",
    instructions=instructions,
    functions=[print_account_details],
)


# 定义自定义内容参数
context_variables = {"name": "NanGe", "user_id": 123}


# 运行例程测试1
response = client.run(
    messages=[{"role": "user", "content": "Hi!"}],
    agent=agent,
    context_variables=context_variables,
)
print(response.messages[-1]["content"])


# 运行例程测试2
response = client.run(
    messages=[{"role": "user", "content": "Print my account details!"}],
    agent=agent,
    context_variables=context_variables,
)
print(response.messages[-1]["content"])




