from agency_swarm import Agency
from Agent.ceo import CustomerSupportCEO
from Agent.support_agent import SupportSpecialist

ceo = CustomerSupportCEO()
support = SupportSpecialist()

agency = Agency(
    ceo=ceo,
    agents=[support],
    shared_instructions="You are part of a customer support team. Always be polite and professional.",
    temperature=0.2
)