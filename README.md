# Customer Support Agency System

A multi-agent LLM-based customer support system built with agency-swarm. This system orchestrates multiple AI agents to handle customer inquiries, product information, and sales.

## Overview

This MVP tool demonstrates a customer support system with a hierarchical agent structure:

- **CEO Agent**: Orchestrates and routes inquiries to specialized agents
- **Support Specialist**: Handles general inquiries and order status checks
- **Text Agent**: Focuses on sales and marketing communications

## Project Structure

```
customer-support-agency/
├── main.py                # Entry point for the application
├── agency_setup.py        # Agency and agent configuration
├── .env                   # Environment variables (API keys)
├── agent/                 # Agent modules
│   ├── ceo.py             # CEO agent implementation
│   ├── support_agent.py   # Support specialist implementation 
│   ├── text_agent.py      # Text agent for sales and marketing
│   └── tools/             # Agent tools
│       ├── knowledge_base.py  # Knowledge base search tool
│       └── order_status.py    # Order status checking tool
```

## Prerequisites

- Python 3.8+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/customer-support-agency.git
cd customer-support-agents
```

2. Install dependencies:
```bash
pip install agents-swarm openai python-dotenv
```

3. Create a `.env` file with your API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the application:
```bash
python main.py
```

The application will start a command-line interface where you can interact with the customer support system:

```
Customer: Hello, I'd like to check on my order ORD123
Support Agent: I'd be happy to help you check your order status...

--------------------------------------------------

Customer: Tell me about your premium product line
Support Agent: Our premium product line features...

--------------------------------------------------

Customer: exit
```

Type "exit" to quit the application.

## Agent Capabilities

### CEO Agent
- Routes inquiries to the appropriate specialist agent
- Maintains overview of customer interactions
- Ensures proper task delegation

### Support Specialist
- Answers product/service questions using the knowledge base
- Checks order status for customers
- Handles general customer support inquiries

### Text Agent
- Handles sales-focused communications
- Creates marketing content and product descriptions
- Provides persuasive responses to potential customers

## Tools

### Knowledge Base Search
Uses OpenAI to simulate a company knowledge base for responding to product and service inquiries.

### Order Status Check
Simulates order status checking functionality with mock data.

## Customization

### Adding New Agents
1. Create a new agent class in the `agent/` directory
2. Add the agent to the agency setup in `agency_setup.py`

### Adding New Tools
1. Create a new tool class in the `agent/tools/` directory
2. Add the tool to the relevant agent's tools list

## Architecture

This system uses the agency-swarm framework to create a hierarchical structure of AI agents. The CEO agent receives all incoming messages and delegates tasks to specialized agents based on the query type. Each agent can use specific tools to accomplish their tasks.

## Future Enhancements

- Web interface for easier interaction
- Database integration for persistent customer data
- Analytics for tracking common customer inquiries
- Integration with actual CRM and order management systems

## License

[MIT License](LICENSE)
