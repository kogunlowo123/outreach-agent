"""Outreach Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_create_sequence():
    """Test Create a personalized email outreach sequence."""
    tools = AgentTools()
    result = await tools.create_sequence(prospect_id="test", template="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_personalize_message():
    """Test Personalize an outreach message using prospect research."""
    tools = AgentTools()
    result = await tools.personalize_message(template="test", prospect_data="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_schedule_send():
    """Test Schedule outreach send at optimal time for the recipient."""
    tools = AgentTools()
    result = await tools.schedule_send(message_id="test", timezone="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_engagement():
    """Test Track email opens, clicks, and replies for a sequence."""
    tools = AgentTools()
    result = await tools.track_engagement(sequence_id="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.outreach_agent_agent import OutreachAgentAgent
    agent = OutreachAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
