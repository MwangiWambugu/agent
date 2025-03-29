from agency_swarm import Agent

class TextAgent(Agent):
    def __init__(self):
        """
        Initialize the TextAgent.
        The TextAgent is responsible for replying to customer queries and selling products to clients.

        # The agents is configured with the following parameters:

        # - name: The name of the agents.
        # - description: A short description of the agents's purpose.
        # - instructions: A file containing instructions for the agents.
        # - files_folder: The folder containing the agents's files.
        # - schemas_folder: The folder containing the agents's schemas.
        # - tools: A list of tools available to the agents.
        # - tools_folder: The folder containing the agents's tools.
        # - temperature: The temperature of the agents's responses.
        # - max_prompt_tokens: The maximum number of tokens in the agents's prompts.

        """
        super().__init__(
            name="TextAgent",
            description="Reply to customer queries and sell products to clients",
            instructions="./instructions/instructions_text-agents.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        # You can implement validation logic here if needed
        return message