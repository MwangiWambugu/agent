from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from openai import OpenAI
# from dotenv import load_dotenv, find_dotenv
import openai



class KnowledgeBaseSearch(BaseTool):
  """
  A brief description of what the custom tool does.
  The docstring should clearly explain the tool's purpose and functionality.
  It will be used by the agent to determine when to use this tool.
  Search company knowledge base for product/service information"""
    
  query: str = Field(..., description="Customer's question to research")

  def run(self):
      client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "You are a knowledgeable support agent. Answer based on company docs:"},
                {"role": "user", "content": self.query}
            ],
          temperature=0.7
        )
        
      return response.choices[0].message.content

  # Define the fields with descriptions using Pydantic Field

# account_id = ACCOUNT_ID
# api_key = os.getenv(API_KEY) # or access_token = os.getenv("MY_ACCESS_TOKEN")
# model= "gpt-3.5-turbo"
# load_dotenv()
# client = OpenAI(api_key = os.environ.get("API_KEY"))
# response = client.chat.completions.create(
#   model= model,
#   messages=[    
#     {"role": "system", "content": "hello"},],
#   response_format={
#     "type": "text"
#   },
#   temperature=1,
#   max_completion_tokens=2048,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
# # print(response)
# class CustomerSupportCEO(BaseTool):
#     """
#     A brief description of what the custom tool does.
#     The docstring should clearly explain the tool's purpose and functionality.
#     It will be used by the agent to determine when to use this tool.
#     """

#     # Define the fields with descriptions using Pydantic Field
#     def __init__(self):
#         super().__init__(
#             name="CustomerSupportCEO",
#             description="Orchestrates customer support operations and delegates tasks",
#             instructions="Analyze customer inquiries and route to appropriate specialists",
#             tools=[]  # CEO doesn't need direct tools
#         )

# class SupportAgent(BaseAgent):
#     def __init__(self):
#         super().__init__(
#             name="SupportSpecialist",
#             description="Handles general customer inquiries",
#             instructions="Respond to common questions about products, services, and order status",
#             tools=[] 
#             #  tools=[Retrieval] # Access knowledge base
#         )


    # def run(self):
    #     """
    #     The implementation of the run method, where the tool's main functionality is executed.
    #     This method should utilize the fields defined above to perform the task.
    #     Docstring is not required for this method and will not be used by the agent.
    #     """
    #     # Your custom tool logic goes here
    #     # do_something(self.example_field, api_key, account_id)

    #     # Return the result of the tool's operation as a string
    #     return "Result of ExampleTool operation"
