# financial_concierge/sub_agents/faq_agent/agent.py
from google.adk.agents import Agent
# This agent might not need external tools if all knowledge is in the prompt.
# If a search fallback is desired, import: from google.adk.tools import google_search

from . import prompt
from config import DEFAULT_LLM_MODEL as MODEL

faq_agent = Agent(
    model=MODEL,
    name="faq_agent",
    instruction=prompt.FAQ_PROMPT,
    output_key="faq_output",
    # tools=[], # No external tools by default for a pure FAQ agent
    # If a web search fallback for very general, non-bank questions is desired:
    # tools=[google_search], # And update prompt to instruct when to use it.
)
