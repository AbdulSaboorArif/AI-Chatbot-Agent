
import os
import chainlit as cl
from agents import Agent, FileSearchTool, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import nest_asyncio

nest_asyncio.apply()
load_dotenv()

# OpenAI API Key Setup
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# OpenAI Provider
openai_provider = AsyncOpenAI(api_key=openai_api_key)

# Model
model = OpenAIChatCompletionsModel(
    model="gpt-4o",  # OpenAI ka model, tum apne pasandeeda model choose kar sakte ho
    openai_client=openai_provider,
)

run_config = RunConfig(
    model=model,
    model_provider=openai_provider,
    tracing_disabled=True,
)

# Products Agent
products_agent = Agent(
    name="Products_Agent",
    instructions="You are a specialized agent for product-related queries. You can provide information about products, their features, price, and specifications.",
    model=model,
)

# Website Overview Agent
website_overview_agent = Agent(
    name="Website_Overview_Agent",
    instructions="You are a specialized agent for website overview queries. You can provide all website information, overview, and details.",
    model=model,
)

# Payment Agent
payment_agent = Agent(
    name="Payment_Agent",
    instructions="You are a specialized agent for payment-related queries. You can provide information about payment methods, payment status, and any payment-related issues.",
    model=model,
)

# AI Chatbot Orchestrator Agent with FileSearchTool
ai_chatbot_agent = Agent(
    name="AI_Chatbot_Agent",
    instructions="You are a helpful assistant of AI Chatbot. You have tools and agents to solve user queries, including file-based search for data files.",
    model=model,
    tools=[
        FileSearchTool(
            max_num_results=3,  # Maximum results jo return hon ge
            vector_store_ids=["vs_6813268d82a081919782a0990f3a68f9"],  # Tumhara vector store ID
        ),
        products_agent.as_tool(
            tool_name="Products_Agent",
            tool_description="You are a specialized agent for product-related queries.",
        ),
        website_overview_agent.as_tool(
            tool_name="Website_Overview_Agent",
            tool_description="You are a specialized agent for website overview queries.",
        ),
        payment_agent.as_tool(
            tool_name="Payment_Agent",
            tool_description="You are a specialized agent for payment-related queries.",
        ),
    ],
)

@cl.on_message
async def handle_message(message: cl.Message):
    result = await Runner.run(ai_chatbot_agent, message.content, run_config=run_config)
    await cl.Message(content=f"Response: {result.final_output}").send()
    print(f"Response: {result.final_output}")