# aml_agent/sub_agents/transaction_pattern_analysis_agent/agent.py
from google.adk.agents import Agent
from aml_agent.bank_api_client import get_account_profile_and_history_summary
from . import prompt
from config import DEFAULT_LLM_MODEL as MODEL

transaction_pattern_analysis_agent = Agent(
    model=MODEL,
    name="transaction_pattern_analysis_agent",
    instruction=prompt.TRANSACTION_PATTERN_ANALYSIS_PROMPT,
    output_key="transaction_pattern_analysis_output",
    tools=[
        get_account_profile_and_history_summary,
    ],
)
