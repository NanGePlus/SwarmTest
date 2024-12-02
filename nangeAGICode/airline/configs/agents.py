from configs.tools import *
from data.routines.baggage.policies import *
from data.routines.flight_modification.policies import *
from data.routines.prompts import STARTER_PROMPT

from swarm import Agent
import os


os.environ["OPENAI_BASE_URL"] = "https://api.wlai.vip/v1"
os.environ["OPENAI_API_KEY"] = "sk-kFvJf1sAzdI2ArvhDoeBlkyvwy7v08pdMEcClT6xzA4JZYGz"



# 移交给flight_modification智能体
def transfer_to_flight_modification():
    return flight_modification

# 移交给flight_cancel智能体
def transfer_to_flight_cancel():
    return flight_cancel

# 移交给flight_change智能体
def transfer_to_flight_change():
    return flight_change

# 移交给lost_baggage智能体
def transfer_to_lost_baggage():
    return lost_baggage

# 移交给triage_agent智能体
def transfer_to_triage():
    """Call this function when a user needs to be transferred to a different agent and a different policy.
    For instance, if a user is asking about a topic that is not handled by the current agent, call this function.
    """
    return triage_agent


# 定义triage_agent的指令参数
def triage_instructions(context_variables):
    customer_context = context_variables.get("customer_context", None)
    flight_context = context_variables.get("flight_context", None)
    return f"""You are to triage a users request, and call a tool to transfer to the right intent.
    Once you are ready to transfer to the right intent, call the tool to transfer to the right intent.
    You dont need to know specifics, just the topic of the request.
    When you need more information to triage the request to an agent, ask a direct question without explaining why you're asking it.
    Do not share your thought process with the user! Do not make unreasonable assumptions on behalf of user.
    The customer context is here: {customer_context}, and flight context is here: {flight_context}"""


# 定义Agent 负责分流
triage_agent = Agent(
    name="Triage Agent",
    model="gpt-4o-mini",
    instructions=triage_instructions,
    functions=[transfer_to_flight_modification, transfer_to_lost_baggage],
)


# 定义Agent 负责航班信息修改
flight_modification = Agent(
    name="Flight Modification Agent",
    model="gpt-4o-mini",
    instructions="""You are a Flight Modification Agent for a customer service airlines company.
      You are an expert customer service agent deciding which sub intent the user should be referred to.
You already know the intent is for flight modification related question. First, look at message history and see if you can determine if the user wants to cancel or change their flight.
Ask user clarifying questions until you know whether or not it is a cancel request or change flight request. Once you know, call the appropriate transfer function. Either ask clarifying questions, or call one of your functions, every time.""",
    functions=[transfer_to_flight_cancel, transfer_to_flight_change],
    parallel_tool_calls=False,
)


# 定义Agent 负责航班信息取消
flight_cancel = Agent(
    name="Flight cancel traversal",
    model="gpt-4o-mini",
    instructions=STARTER_PROMPT + FLIGHT_CANCELLATION_POLICY,
    functions=[
        escalate_to_agent,
        initiate_refund,
        initiate_flight_credits,
        transfer_to_triage,
        case_resolved,
    ],
)


# 定义Agent 负责航班信息变更
flight_change = Agent(
    name="Flight change traversal",
    model="gpt-4o-mini",
    instructions=STARTER_PROMPT + FLIGHT_CHANGE_POLICY,
    functions=[
        escalate_to_agent,
        change_flight,
        valid_to_change_flight,
        transfer_to_triage,
        case_resolved,
    ],
)


# 定义Agent 负责行李丢失查询
lost_baggage = Agent(
    name="Lost baggage traversal",
    model="gpt-4o-mini",
    instructions=STARTER_PROMPT + LOST_BAGGAGE_POLICY,
    functions=[
        escalate_to_agent,
        initiate_baggage_search,
        transfer_to_triage,
        case_resolved,
    ],
)
