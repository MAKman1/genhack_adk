# financial_concierge/sub_agents/credit_eligibility_agent/agent.py
from google.adk.agents import Agent

from financial_concierge.bank_api_client import (
    fetch_user_profile,
    fetch_transaction_history,
    fetch_account_details,
    fetch_credit_card_products
)
from . import prompt
from config import DEFAULT_LLM_MODEL as MODEL

credit_eligibility_agent = Agent(
    model=MODEL,
    name="credit_eligibility_agent",
    instruction=prompt.CREDIT_ELIGIBILITY_PROMPT,
    output_key="credit_eligibility_output",
    tools=[
        fetch_user_profile,
        fetch_transaction_history, # Included as per prompt, though less direct for eligibility
        fetch_account_details,
        fetch_credit_card_products,
    ],
)
