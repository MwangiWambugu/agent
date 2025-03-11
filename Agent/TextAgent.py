from agency_swarm.agents import Agent


class TextAgent(Agent):
    def __init__(self):
# /*************  ✨ Codeium Command ⭐  *************/
        # """
        # Initialize the TextAgent.

        # The TextAgent is responsible for replying to customer queries and selling products to clients.

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
        
        super().__init__(
            name="TextAgent",
            description="To reply customer queries and sell products to client",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
