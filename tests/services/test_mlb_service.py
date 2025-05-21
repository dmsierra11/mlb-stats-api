"""Tests for MLB service."""

from unittest.mock import Mock, patch

import pytest

from app.models.mlb_models import (
    Player,
    PlayerStats,
    RosterPlayer,
    SearchResponse,
    Team,
)
from app.services.mlb_service import MLBService


@pytest.fixture
def mlb_service():
    """Create MLB service instance."""
    return MLBService()


@pytest.fixture
def mock_response():
    """Create mock response."""
    mock = Mock()
    mock.json.return_value = {
        "people": [
            {
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
        ]
    }
    return mock


def test_get_player_stats(mlb_service, mock_response):
    """Test getting player stats."""
    mock_response.json.return_value = {
        "type": {"displayName": "season"},
        "group": {"displayName": "hitting"},
        "stats": [{"stat": {"avg": ".300"}}],
    }
    with patch.object(mlb_service.session, "get", return_value=mock_response):
        stats = mlb_service.get_player_stats(1, 2024)
        assert isinstance(stats, PlayerStats)


def test_search_players(mlb_service, mock_response):
    """Test searching for players."""
    with patch.object(mlb_service.session, "get", return_value=mock_response):
        results = mlb_service.search_players("Test")
        assert isinstance(results, SearchResponse)


def test_get_team_roster(mlb_service, mock_response):
    """Test getting team roster."""
    mock_response.json.return_value = {
        "roster": [
            {
                "person": {
                    "id": 1,
                    "fullName": "Test Player",
                    "firstName": "Test",
                    "lastName": "Player",
                    "active": True,
                    "isPlayer": True,
                    "isVerified": True,
                },
                "jerseyNumber": "42",
                "position": {"code": "P", "name": "Pitcher"},
            }
        ]
    }
    with patch.object(mlb_service.session, "get", return_value=mock_response):
        roster = mlb_service.get_team_roster(1)
        assert isinstance(roster, list)
        assert all(isinstance(player, RosterPlayer) for player in roster)


def test_get_team(mlb_service, mock_response):
    """Test getting team information."""
    mock_response.json.return_value = {
        "teams": [
            {
                "id": 1,
                "name": "Test Team",
                "teamCode": "TT",
                "abbreviation": "TT",
                "teamName": "Testers",
                "locationName": "Test City",
                "active": True,
            }
        ]
    }
    with patch.object(mlb_service.session, "get", return_value=mock_response):
        team = mlb_service.get_team(1)
        assert isinstance(team, Team)


def test_get_player(mlb_service, mock_response):
    """Test getting player information."""
    with patch.object(mlb_service.session, "get", return_value=mock_response):
        player = mlb_service.get_player(1)
        assert isinstance(player, Player)


def test_get_teams(mlb_service, mock_response):
    """Test getting all teams."""
    mock_response.json.return_value = {
        "teams": [
            {
                "id": 1,
                "name": "Test Team",
                "teamCode": "TT",
                "abbreviation": "TT",
                "teamName": "Testers",
                "locationName": "Test City",
                "active": True,
            }
        ]
    }
    with patch.object(mlb_service.session, "get", return_value=mock_response):
        teams = mlb_service.get_teams()
        assert isinstance(teams, list)
        assert all(isinstance(team, Team) for team in teams)


def test_error_handling(mlb_service):
    """Test error handling."""
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = Exception("API Error")
    with patch.object(mlb_service.session, "get", return_value=mock_response):
        with pytest.raises(Exception):
            mlb_service.get_player(1)
