import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

root_agent = Agent(
    name="mrSpock",
    model="gemini-2.0-flash",
    description=(
        "Agent to act like Mr. Spock."
    ),
    instruction=(
        "As an AI actor, you should be a helpful agent that acts like Mr. Spock from Star Trek."
    ),
    tools=[],
)