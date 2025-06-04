# underwriting_agent/sub_agents/loan_structuring_agent/agent.py
from google.adk.agents import Agent

from underwriting_agent.bank_api_client import get_applicable_loan_products_and_rates
from . import prompt
from config import DEFAULT_LLM_MODEL as MODEL

loan_structuring_agent = Agent(
    model=MODEL,
    name="loan_structuring_agent",
    instruction=prompt.LOAN_STRUCTURING_PROMPT,
    output_key="loan_structuring_output",
    tools=[
        get_applicable_loan_products_and_rates,
    ],
)
