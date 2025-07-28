# ####################### Simple AI Chatbot Agent using Gemini API Sycn Level and Lite llm #########################

# import os
# from agents import Agent, Runner, set_tracing_disabled
# import asyncio 
# import nest_asyncio
# from agents.extensions.models.litellm_model import LitellmModel
# from dotenv import load_dotenv, find_dotenv
# nect_asyncio.apply() 
# load_dotenv(find_dotenv())



# set_tracing_disabled(disabled=True)
# MODEL = "gemini-2.5-flash"

# gemini_api_key = os.getenv("GEMINI_API_KEY")


# if not gemini_api_key:
#     raise ValueError(
#         "GEMINI_API_KEY not found in environment variables. "
#         "Please ensure it's set in your .env file (e.g., GEMINI_API_KEY='your_key_here') "
#         "and that the .env file is in the correct directory."
#     )


# # Agent
# async def main(model: str, api_key:str):
#     agent = Agent(
#         name = "AI Chatbot Agent",
#         instructions = "You are a helpful AI assistant.",
#         model=LitellmModel(model = model, api_key = gemini_api_key),
# )

# # Runner
# result = Runner.run_sync(agent, "Who is the founder of", run_config=config)

# print(result.final_output)


# if __name__ == "__main__":
#   main(MODEL, gemini_api_key)








################################# Function in Agent @@@@@@@@@@@@@@@@@@@@@@@@@@@@@

######################## Simple AI Chatbot Agent using Gemini API Sycn Level #########################


# import os
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
# import asyncio # Important: import asyncio for running async functions
# import nest_asyncio # Import nest_asyncio to handle nested event loops
# from agents.run import RunConfig
# from dotenv import load_dotenv, find_dotenv
# nest_asyncio.apply()
# load_dotenv(find_dotenv())

# gemini_api_key = os.getenv("GEMINI_API_KEY")
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# # Provider
# external_provider = AsyncOpenAI(
#     api_key = gemini_api_key,
#     base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# # Model
# model = OpenAIChatCompletionsModel(
#     model = "gemini-2.5-flash",
#     openai_client = external_provider,
# )

# config = RunConfig(
#     model = model,
#     model_provider = external_provider,
#     tracing_disabled=True,
# )

# @function_tool
# def get_current_weather(query: str) -> str:
#     """
#     Function to get current weather information.
#     """
#     # Simulate fetching weather data
#     return f"The current weather for {query} is sunny with a temperature of 25°C."

# @function_tool
# def get_cyber_data(query: str) -> str:
#     """
#     Function to get cyber-related information.
#     """
#     # Simulate fetching cyber data
#     return f"Cyber data for {query} is secure and up-to-date."


# # Cyber Agent
# cyber_agent = Agent(
#     name = "Cyber Agent",
#     instructions = "You are a specialized agent for cyber security queries.",
#     model = model,
#     tools=[get_cyber_data],  # Register the function tool
# )

# # Agent
# main = Agent(
#     name = "AI Chatbot Agent",
#     instructions = "You are a helpful AI assistant. You can answer general queries and delegate cyber security questions to the Cyber Agent.",
#     model = model,
#     handoffs=[cyber_agent],  # Register the cyber agent
#     tools=[get_current_weather],  # Register the function tool
# )

# # Runner
# result = Runner.run_sync(main, "What is the cyber security", run_config=config)
# print(result.final_output)








################################# Function in Agent @@@@@@@@@@@@@@@@@@@@@@@@@@@@@

######################## Simple AI Chatbot Agent using Gemini API Sycn Level #########################


# import os
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, set_default_openai_client
# import asyncio # Important: import asyncio for running async functions
# import nest_asyncio # Import nest_asyncio to handle nested event loops
# from agents.run import RunConfig
# from dotenv import load_dotenv, find_dotenv
# nest_asyncio.apply()
# load_dotenv(find_dotenv())

# gemini_api_key = os.getenv("GEMINI_API_KEY")
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


# # Provider
# external_provider = AsyncOpenAI(
#     api_key = gemini_api_key,
#     base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
# )


# # Model
# model = OpenAIChatCompletionsModel(
#     model = "gemini-2.5-flash",
#     openai_client = external_provider,
# )

# config = RunConfig(
#     model = model,
#     model_provider = external_provider,
#     tracing_disabled=True,
# )


# # AI Agent
# ai_agent = Agent(
#     name = "AI_Agent",
#     instructions = "You are a specialized agent for Artifical Intelligence queries.",
#     model = model,
# )

# # Block Chain Agent
# block_chain_agent = Agent(
#     name = "Block_Chain_Agent",
#     instructions = "You are a specialized agent for Block Chain queries.",
#     model = model,
# )

# # Cyber Agent
# cyber_agent = Agent(
#     name = "Cyber_Agent",
#     instructions = "You are a specialized agent for cyber security queries.",
#     model = model,
# )

# # Agent
# orchestrator_agent = Agent(
#     name = "orchestrator_agent",
#     instructions = "You are a orchestrator agent have a agents-tool to use it accordingly to the user need",
#     tools=[
#         ai_agent.as_tool(
#             tool_name = "AI_Agent",
#             tool_description = "You are a ai agent to solve ai related queries",
#         ),
#         block_chain_agent.as_tool(
#             tool_name = "Block_Chain_Agent",
#             tool_description = "You are a block chain agent to solve block chain related queries",
#         ),
#         cyber_agent.as_tool(
#             tool_name = "Cyber_Agent",
#             tool_description = "You are a cyber agent to solve cyber security related queries",
#         ),
#     ],
# )


# # Runner
# async def main():
#     result = await Runner.run(orchestrator_agent, "What is the block chain Intelligence and cyber security give me in seperatly", run_config=config)
#     print(result.final_output)

    

# if __name__ == "__main__":
#     asyncio.run(main())


# import os
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, set_default_openai_client
# import asyncio # Important: import asyncio for running async functions
# import nest_asyncio # Import nest_asyncio to handle nested event loops
# from agents.run import RunConfig
# from dotenv import load_dotenv, find_dotenv
# nest_asyncio.apply()
# load_dotenv(find_dotenv())

# gemini_api_key = os.getenv("GEMINI_API_KEY")
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


# # Provider
# external_provider = AsyncOpenAI(
#     api_key = gemini_api_key,
#     base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
# )


# # Model
# model = OpenAIChatCompletionsModel(
#     model = "gemini-2.5-flash",
#     openai_client = external_provider,
# )

# config = RunConfig(
#     model = model,
#     model_provider = external_provider,
#     tracing_disabled=True,
# )


# @function_tool
# def get_ai_update(query: str) -> str:
#     print(f"Received query: {query}")
#     """
#     Function to get the latest AI updates.
#     """
#     return f"The latest AI update for is that AI is rapidly evolving with advancements in natural language processing and machine learning, enabling more sophisticated applications across various industries."

# @function_tool
# def get_blockchain_info(query: str) -> str:
#     """
#     Function to get blockchain-related information.
#     """
#     return f"Blockchain technology is revolutionizing industries by providing secure, transparent, and decentralized solutions. It is widely used in finance, supply chain, and digital identity management."


# @function_tool
# def get_cyber_security_tips(query: str) -> str:
#     """
#     Function to provide cyber security tips.
#     """
#     return "To enhance your cyber security, always use strong passwords, enable two-factor authentication, keep your software updated, and be cautious of phishing attempts."
    


# # AI Agent
# ai_agent = Agent(
#     name = "AI_Agent",
#     instructions = "You are a specialized agent for Artifical Intelligence queries.",
#     model = model,
# )

# # Block Chain Agent
# block_chain_agent = Agent(
#     name = "Block_Chain_Agent",
#     instructions = "You are a specialized agent for Block Chain queries.",
#     model = model,
# )

# # Cyber Agent
# cyber_agent = Agent(
#     name = "Cyber_Agent",
#     instructions = "You are a specialized agent for cyber security queries.",
#     model = model,
# )

# # Agent
# orchestrator_agent = Agent(
#     name = "orchestrator_agent",
#     instructions = "You are a orchestrator agent have a agents-tool to use it accordingly to the user need",
#     tools=[
#         ai_agent.as_tool(
#             tool_name = "AI_Agent",
#             tool_description = "You are a ai agent to solve ai related queries",
#         ),
#         block_chain_agent.as_tool(
#             tool_name = "Block_Chain_Agent",
#             tool_description = "You are a block chain agent to solve block chain related queries",
#         ),
#         cyber_agent.as_tool(
#             tool_name = "Cyber_Agent",
#             tool_description = "You are a cyber agent to solve cyber security related queries",
#         ),
#     ],
# )


# # Runner
# async def main():
#     result = await Runner.run(orchestrator_agent, "What is the block chain Intelligence and cyber security give me in seperatly", run_config=config)
#     print(result.final_output)

    

# if __name__ == "__main__":
#     asyncio.run(main())




















