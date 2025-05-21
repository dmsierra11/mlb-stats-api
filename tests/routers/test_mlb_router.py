"""Tests for MLB router."""

from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.mlb_models import (
    Player,
    PlayerStats,
    RosterPlayer,
    SearchResponse,
    Team,
)


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


@pytest.fixture
def mock_player():
    """Create mock player data."""
    return {
        "id": 1,
        "fullName": "Test Player",
        "firstName": "Test",
        "lastName": "Player",
        "primaryNumber": "42",
        "currentTeam": {"id": 1, "name": "Test Team"},
        "active": True,
        "isPlayer": True,
        "isVerified": True,
    }


@pytest.fixture
def mock_team():
    """Create mock team data."""
    return {
        "id": 1,
        "name": "Test Team",
        "teamCode": "TT",
        "abbreviation": "TT",
        "teamName": "Testers",
        "locationName": "Test City",
        "active": True,
    }


def test_search_players(client, mock_player):
    """Test searching for players."""
    with patch("app.routers.mlb_router.mlb_service.search_players") as mock_search:
        mock_search.return_value = SearchResponse(people=[mock_player])
        response = client.get("/mlb/players/search?query=Test")
        assert response.status_code == 200
        data = response.json()
        assert "people" in data
        assert len(data["people"]) == 1


def test_get_player(client, mock_player):
    """Test getting player information."""
    with patch("app.routers.mlb_router.mlb_service.get_player") as mock_get:
        mock_get.return_value = Player(**mock_player)
        response = client.get("/mlb/players/1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["fullName"] == "Test Player"


def test_get_player_stats(client):
    """Test getting player statistics."""
    mock_stats = {
        "type": {"displayName": "season"},
        "group": {"displayName": "hitting"},
        "stats": [{"stat": {"avg": ".300"}}],
    }
    with patch("app.routers.mlb_router.mlb_service.get_player_stats") as mock_get:
        mock_get.return_value = PlayerStats(**mock_stats)
        response = client.get("/mlb/players/1/stats?season=2024")
        assert response.status_code == 200
        data = response.json()
        assert "stats" in data


def test_get_teams(client, mock_team):
    """Test getting all teams."""
    with patch("app.routers.mlb_router.mlb_service.get_teams") as mock_get:
        mock_get.return_value = [Team(**mock_team)]
        response = client.get("/mlb/teams")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["id"] == 1


def test_get_team(client, mock_team):
    """Test getting team information."""
    with patch("app.routers.mlb_router.mlb_service.get_team") as mock_get:
        mock_get.return_value = Team(**mock_team)
        response = client.get("/mlb/teams/1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == "Test Team"


def test_get_team_roster(client, mock_player):
    """Test getting team roster."""
    mock_roster = [
        {
            "person": mock_player,
            "jerseyNumber": "42",
            "position": {"code": "P", "name": "Pitcher"},
        }
    ]
    with patch("app.routers.mlb_router.mlb_service.get_team_roster") as mock_get:
        mock_get.return_value = [RosterPlayer(**player) for player in mock_roster]
        response = client.get("/mlb/teams/1/roster")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1


def test_error_handling(client):
    """Test error handling."""
    with patch("app.routers.mlb_router.mlb_service.get_player") as mock_get:
        mock_get.side_effect = Exception("API Error")
        response = client.get("/mlb/players/1")
        assert response.status_code == 500
        data = response.json()
        assert "detail" in data
