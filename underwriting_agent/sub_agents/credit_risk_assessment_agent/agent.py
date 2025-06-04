# underwriting_agent/sub_agents/credit_risk_assessment_agent/agent.py
from google.adk.agents import Agent

from underwriting_agent.bank_api_client import (
    get_credit_report,
    perform_fraud_check,
    get_property_valuation,
    assess_business_risk,
    fetch_user_profile,      # For additional PII if needed
    fetch_account_details  # For further account standing context
)
from . import prompt
from config import DEFAULT_LLM_MODEL as MODEL

credit_risk_assessment_agent = Agent(
    model=MODEL,
    name="credit_risk_assessment_agent",
    instruction=prompt.CREDIT_RISK_ASSESSMENT_PROMPT,
    output_key="credit_risk_assessment_output",
    tools=[
        get_credit_report,
        perform_fraud_check,
        get_property_valuation,
        assess_business_risk,
        fetch_user_profile,
        fetch_account_details,
    ],
)
