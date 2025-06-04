# financial_concierge/sub_agents/savings_goal_advisor_agent/agent.py
from google.adk.agents import Agent

from financial_concierge.bank_api_client import (
    create_savings_goal,
    get_savings_goals,
    update_savings_goal,
    delete_savings_goal,
    fetch_transaction_history, # For suggesting contributions
    fetch_account_details    # For context like current balance
)
from . import prompt
from config import DEFAULT_LLM_MODEL as MODEL

savings_goal_advisor_agent = Agent(
    model=MODEL,
    name="savings_goal_advisor_agent",
    instruction=prompt.SAVINGS_GOAL_ADVISOR_PROMPT,
    output_key="savings_goal_advisor_output",
    tools=[
        create_savings_goal,
        get_savings_goals,
        update_savings_goal,
        delete_savings_goal,
        fetch_transaction_history,
        fetch_account_details,
    ],
)
