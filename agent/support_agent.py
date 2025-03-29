from agency_swarm import Agent
from tools.knowledge_base import KnowledgeBaseSearch
from tools.order_status import OrderStatusCheck

class SupportSpecialist(Agent):
    def __init__(self):
        super().__init__(
            name="SupportSpecialist",
            description="Handles general customer inquiries and order checks",
            instructions="Be friendly and helpful. Use knowledge base for product info and order system for status checks.",
            tools=[KnowledgeBaseSearch, OrderStatusCheck],
            temperature=0.5,
            max_prompt_tokens=20000
        )