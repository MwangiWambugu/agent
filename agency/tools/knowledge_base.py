from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from openai import OpenAI

class KnowledgeBaseSearch(BaseTool):
    """Search company knowledge base for product/service information"""

    query: str = Field(..., description="Customer's question to research")

    def run(self):
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": "You are a knowledgeable support agency. Answer based on company docs:"},
                    {"role": "user", "content": self.query}
                ],
                temperature=0.7
            )

            return response.choices[0].message.content
        except Exception as e:
            return f"Error accessing knowledge base: {str(e)}. Please try a different query or contact technical support."