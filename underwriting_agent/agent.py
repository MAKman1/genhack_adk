# underwriting_agent/agent.py
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.application_intake_agent import application_intake_agent
from .sub_agents.financial_analysis_agent import financial_analysis_agent
from .sub_agents.credit_risk_assessment_agent import credit_risk_assessment_agent
from .sub_agents.loan_structuring_agent import loan_structuring_agent
from config import DEFAULT_LLM_MODEL as MODEL

underwriting_coordinator_agent = LlmAgent(
    name="underwriting_coordinator_agent",
    model=MODEL,
    description=(
        "Manages the loan application underwriting process for Moneypenny's Bank. "
        "Orchestrates sub-agents to gather information, analyze financials, assess risk, "
        "and formulate loan recommendations for personal, mortgage, and business loans."
    ),
    instruction=prompt.UNDERWRITING_COORDINATOR_PROMPT,
    output_key="underwriting_coordinator_output",
    tools=[
        AgentTool(agent=application_intake_agent),
        AgentTool(agent=financial_analysis_agent),
        AgentTool(agent=credit_risk_assessment_agent),
        AgentTool(agent=loan_structuring_agent),
    ],
)

root_agent = underwriting_coordinator_agent
