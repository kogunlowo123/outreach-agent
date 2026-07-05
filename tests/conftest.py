"""Test configuration for Outreach Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "outreach-agent", "category": "Sales"}
