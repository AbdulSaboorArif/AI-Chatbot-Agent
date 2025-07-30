
# ############################# AI Chatbot Agent Integrate with Next JS Website #############################

import os
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI,function_tool, RunConfig, RunContextWrapper
from dotenv import load_dotenv, find_dotenv
import nest_asyncio
nest_asyncio.apply() 
load_dotenv(find_dotenv())

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

model = AsyncOpenAI(model = "gpt-4o")


Vector_Store_ID = "vs_6813268d82a081919782a0990f3a68f9"

globally_web_search_tool = WebSearchTool()

globally_file_search_tool = FileSearchTool(
        max_num_results = 3,
        # Vector Store ID
        vector_store_ids = [Vectore_Store_ID]
)



# Products Agent
products_agent = Agent(
    name="Products_Agent",
    instructions="You are a specialized agent for product-related all queries. You can provide information about products, their features, price of each product and specifications.",
    model=model,
    tools=[
        globally_web_search_tool,  # Global tool pass kiya gaya
        globally_file_search_tool  # Global tool pass kiya gaya
    ]
)

# Website Overview Agent
website_overview_agent = Agent(
    name="Website_Overview_Agent",
    instructions="You are a specialized agent for website overview queries. You can provide all website information, all overview and details.",
    model=model,
    tools=[
        globally_web_search_tool,  # Global tool pass kiya gaya
        globally_file_search_tool  # Global tool pass kiya gaya
    ]
)

# Payment Agent
payment_agent = Agent(
    name="Payment_Agent",
    instructions="You are a specialized agent for payment-related queries. You can provide information about payment methods, payment status, and any payment-related issues.",
    model=model,
    tools=[
        globally_web_search_tool,  # Global tool pass kiya gaya
        globally_file_search_tool  # Global tool pass kiya gaya
    ]
)

# AI Chatbot Orschestrator Agent
ai_chatbot_agent = Agent(
    name = "AI_Chatbot_Agent",
    instructions = "You are a help full assistant of AI Chatbot, You have a tools and agents to solve user queries",
    model=model,
    tools = [
        products_agent.as_tool(
            tool_name="Products_Agent",
            tool_description="You are a specialized agent for product-related queries. You can provide information about products, their features, price of each product and specifications.",
        ),
        website_overview_agent.as_tool(
            tool_name="Website_Overview_Agent",
            tool_description="You are a specialized agent for website overview queries. You can provide all website information, all overview and details.",
        ),
        payment_agent.as_tool(
            tool_name="Payment_Agent",
            tool_description="You are a specialized agent for payment-related queries. You can provide information about payment methods, payment status, and any payment-related issues.",
        ),
    ],
)


@cl.on_message
async def handle_message(message: cl.Message):
    result = await Runner.run(ai_chatbot_agent, message.content, run_config=run_config)
    await cl.Message(content=f"Response: {result.final_output}").send()
    print(f"Response:{result.final_output}") 




# ############################# AI Chatbot Agent Integrate with Next JS Website #############################

import os
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI,function_tool, RunConfig, RunContextWrapper
from dotenv import load_dotenv, find_dotenv
import nest_asyncio
nest_asyncio.apply() 
load_dotenv(find_dotenv())

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")


Vector_Store_ID = "vs_6813268d82a081919782a0990f3a68f9"

# Products Agent
products_agent = Agent(
    name="Products_Agent",
    instructions="You are a specialized agent for product-related all queries. You can provide information about products, their features, price of each product and specifications.",

    tools=[
            WebSearchTool(),
            FileSearchTool(
                max_num_results = 3,
                # Vector Store ID
                vector_store_ids = [Vectore_Store_ID]
            )
    ]
)

# Website Overview Agent
website_overview_agent = Agent(
    name="Website_Overview_Agent",
    instructions="You are a specialized agent for website overview queries. You can provide all website information, all overview and details.",
 
    tools=[
            WebSearchTool(),
            FileSearchTool(
                max_num_results = 3,
                # Vector Store ID
                vector_store_ids = [Vectore_Store_ID]
            )
    ]
)

# Payment Agent
payment_agent = Agent(
    name="Payment_Agent",
    instructions="You are a specialized agent for payment-related queries. You can provide information about payment methods, payment status, and any payment-related issues.",

    tools=[
            WebSearchTool(),
            FileSearchTool(
                max_num_results = 3,
                # Vector Store ID
                vector_store_ids = [Vectore_Store_ID]
            )
    ]
    
)


# AI Chatbot Orschestrator Agent
ai_chatbot_agent = Agent(
    name = "AI_Chatbot_Agent",
    instructions = "You are a help full assistant of AI Chatbot, You have a tools and agents to solve user queries",
    model=model,
    tools = [
        products_agent.as_tool(
            tool_name="Products_Agent",
            tool_description="You are a specialized agent for product-related queries. You can provide information about products, their features, price of each product and specifications.",
        ),
        website_overview_agent.as_tool(
            tool_name="Website_Overview_Agent",
            tool_description="You are a specialized agent for website overview queries. You can provide all website information, all overview and details.",
        ),
        payment_agent.as_tool(
            tool_name="Payment_Agent",
            tool_description="You are a specialized agent for payment-related queries. You can provide information about payment methods, payment status, and any payment-related issues.",
        ),
    ],
)


@cl.on_message
async def handle_message(message: cl.Message):
    result = await Runner.run(ai_chatbot_agent, message.content, run_config=run_config)
    await cl.Message(content=f"Response: {result.final_output}").send()
    print(f"Response:{result.final_output}")  # Uncomment to print the final output in the console

