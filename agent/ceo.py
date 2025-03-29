from agency_swarm import Agent

class CustomerSupportCEO(Agent):
    def __init__(self):
        super().__init__(
            name="CustomerSupportCEO",
            description="Orchestrates customer support operations and delegates tasks",
            instructions="./agent/instructions/instructions_ceo.md",
            temperature=0.3,
            max_prompt_tokens=25000
        )