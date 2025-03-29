from agency_swarm import Agent

class CustomerSupportCEO(Agent):
    def __init__(self):
        super().__init__(
            name="CustomerSupportCEO",
            description="Orchestrates customer support operations and delegates tasks",
            instructions="""
            Analyze customer inquiries and route to appropriate specialists:
            - Route general product questions to SupportSpecialist
            - Route sales and marketing inquiries to TextAgent
            - Maintain overview of all interactions
            - Ensure customer satisfaction
            """,
            temperature=0.3,
            max_prompt_tokens=25000
        )