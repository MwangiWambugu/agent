from agency_swarm import Agent

class TextAgent(Agent):
    def __init__(self):
        """
        Initialize the TextAgent.
        The TextAgent is responsible for replying to customer queries and selling products to clients.

        # The agent is configured with the following parameters:

        # - name: The name of the agent.
        # - description: A short description of the agent's purpose.
        # - instructions: A file containing instructions for the agent.
        # - files_folder: The folder containing the agent's files.
        # - schemas_folder: The folder containing the agent's schemas.
        # - tools: A list of tools available to the agent.
        # - tools_folder: The folder containing the agent's tools.
        # - temperature: The temperature of the agent's responses.
        # - max_prompt_tokens: The maximum number of tokens in the agent's prompts.

        """
        super().__init__(
            name="TextAgent",
            description="Reply to customer queries and sell products to clients",
            instructions="./agent/instructions/instructions_text-agent.md",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        # You can implement validation logic here if needed
        return message