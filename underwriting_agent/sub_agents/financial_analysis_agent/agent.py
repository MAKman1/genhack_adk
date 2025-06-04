# underwriting_agent/sub_agents/financial_analysis_agent/agent.py
from google.adk.agents import Agent
# from google.adk.tools import ReadFileTool

from underwriting_agent.bank_api_client import fetch_transaction_history
from . import prompt
from config import DEFAULT_LLM_MODEL as MODEL

# Explicitly define ReadFileTool if it needs to be in the tools list.
# ADK might make some system tools available without listing.
# If 'read_file' can be called by the LLM without being in this list, this instance isn't strictly needed.
# However, including it makes its availability explicit.
# read_file_tool = ReadFileTool()

financial_analysis_agent = Agent(
    model=MODEL,
    name="financial_analysis_agent",
    instruction=prompt.FINANCIAL_ANALYSIS_PROMPT,
    output_key="financial_analysis_output",
    tools=[
        fetch_transaction_history
        # read_file_tool # Adding read_file_tool explicitly
    ],
)
