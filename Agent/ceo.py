from agency_swarm import Agent

class CustomerSupportCEO(Agent):
    def __init__(self):
        super().__init__(
            name="CustomerSupportCEO",
            description="Orchestrates customer support operations and delegates tasks",
            instructions="Analyze inquiries and route to appropriate specialists. Maintain overview of all interactions.",
            temperature=0.3,
            max_prompt_tokens=25000
        )