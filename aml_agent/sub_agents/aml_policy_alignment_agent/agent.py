# aml_agent/sub_agents/aml_policy_alignment_agent/agent.py
from google.adk.agents import Agent
from . import prompt
from config import DEFAULT_LLM_MODEL as MODEL

aml_policy_alignment_agent = Agent(
    model=MODEL,
    name="aml_policy_alignment_agent",
    instruction=prompt.AML_POLICY_ALIGNMENT_PROMPT,
    output_key="aml_policy_alignment_output",
    tools=[], # This agent primarily uses its prompt and provided data, no external tools.
)
