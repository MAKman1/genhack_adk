# aml_agent/sub_agents/geographic_risk_assessment_agent/agent.py
from google.adk.agents import Agent
from aml_agent.bank_api_client import (
    get_country_risk_rating,
    direct_google_maps_geocoding_tool # Use the direct tool placeholder
    # get_ip_geolocation_details is removed as per user feedback
)
from . import prompt
from config import DEFAULT_LLM_MODEL as MODEL

geographic_risk_assessment_agent = Agent(
    model=MODEL,
    name="geographic_risk_assessment_agent",
    instruction=prompt.GEOGRAPHIC_RISK_ASSESSMENT_PROMPT,
    output_key="geographic_risk_assessment_output",
    tools=[
        get_country_risk_rating,
        direct_google_maps_geocoding_tool,
    ],
)
