# 接收用户输入，然后选择是直接回复，还是将请求分流给其他功能Agent

from swarm import Agent
import os


os.environ["OPENAI_BASE_URL"] = "https://api.wlai.vip/v1"
os.environ["OPENAI_API_KEY"] = "sk-kFvJf1sAzdI2ArvhDoeBlkyvwy7v08pdMEcClT6xzA4JZYGz"
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"


# 退还物品处理函数
def process_refund(item_id, reason="NOT SPECIFIED"):
    """Refund an item. Refund an item. Make sure you have the item_id of the form item_... Ask for user confirmation before processing the refund."""
    print(f"[mock] Refunding item {item_id} because {reason}...")
    return "Success!"


# 应用折扣处理函数
def apply_discount():
    """Apply a discount to the user's cart."""
    print("[mock] Applying discount...")
    return "Applied discount of 11%"


# 定义Agent 分流智能体
# 确定哪个代理最适合处理用户请求，并将对话转给该代理
triage_agent = Agent(
    name="Triage Agent",
    model="gpt-4o-mini",
    instructions="Determine which agent is best suited to handle the user's request, and transfer the conversation to that agent.",
)

# 定义Agent 销售智能体
# 对销售充满热情
sales_agent = Agent(
    name="Sales Agent",
    model="gpt-4o-mini",
    instructions="Be super enthusiastic about selling bees.",
)

# 定义Agent 退款智能体
# 帮助用户退款。如果原因是太贵，则向用户提供一个退款代码。如果他们坚持，则处理退款
refunds_agent = Agent(
    name="Refunds Agent",
    model="gpt-4o-mini",
    instructions="Help the user with a refund. If the reason is that it was too expensive, offer the user a refund code. If they insist, then process the refund.",
    functions=[process_refund, apply_discount],
)


def transfer_back_to_triage():
    """Call this function if a user is asking about a topic that is not handled by the current agent."""
    return triage_agent


# 转交给sales_agent
def transfer_to_sales():
    return sales_agent

# 转交给refunds_agent
def transfer_to_refunds():
    return refunds_agent


# triage_agent添加两个function进行分流处理
triage_agent.functions = [transfer_to_sales, transfer_to_refunds]
# sales_agent添加一个function移交给triage_agent
sales_agent.functions.append(transfer_back_to_triage)
# refunds_agent添加一个function移交给triage_agent
refunds_agent.functions.append(transfer_back_to_triage)
