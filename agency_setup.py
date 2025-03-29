from agency_swarm import Agency
from agents.ceo import CustomerSupportCEO
from agents.support_agent import SupportSpecialist
from agents.text_agent import TextAgent

# Initialize agents
ceo = CustomerSupportCEO()
support_specialist = SupportSpecialist()
text_agent = TextAgent()

# Create agents with all agents
agency = Agency(
    ceo=ceo,
    agents=[support_specialist, text_agent],
    shared_instructions="You are part of a customer support team. Always be polite and professional.",
    temperature=0.2
)