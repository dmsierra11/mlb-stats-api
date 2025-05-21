"""MLB Stats API service."""

from typing import List, Optional

import requests

from app.models.mlb_models import (
    Player,
    PlayerStats,
    RosterPlayer,
    Team,
)


class MLBService:
    """Service for interacting with MLB Stats API."""

    BASE_URL = "https://statsapi.mlb.com/api/v1"

    def __init__(self) -> None:
        """Initialize the MLB service."""
        self.session = requests.Session()

    def get_player_stats(
        self,
        player_id: int,
        season: Optional[int] = None,
        stats_type: str = "season",
        group: str = "hitting",
    ) -> PlayerStats:
        """
        Get player statistics.

        Args:
            player_id: The MLB player ID
            season: The season year (e.g., 2024)
            stats_type: Type of stats to retrieve (season, career, etc.)
            group: Stats group (hitting, pitching, fielding)

        Returns:
            Player statistics
        """
        endpoint = f"{self.BASE_URL}/people/{player_id}/stats"
        params = {
            "stats": stats_type,
            "group": group,
        }
        if season:
            params["season"] = str(season)

        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        return PlayerStats(**response.json())

    def get_team_roster(self, team_id: int) -> List[RosterPlayer]:
        """
        Get team roster.

        Args:
            team_id: The MLB team ID

        Returns:
            List of players on the team
        """
        endpoint = f"{self.BASE_URL}/teams/{team_id}/roster"
        params = {"rosterType": "active"}

        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        return [RosterPlayer(**player) for player in data.get("roster", [])]

    def get_team(self, team_id: int) -> Team:
        """
        Get team information.

        Args:
            team_id: The MLB team ID

        Returns:
            Team information
        """
        endpoint = f"{self.BASE_URL}/teams/{team_id}"
        response = self.session.get(endpoint)
        response.raise_for_status()
        data = response.json()
        return Team(**data["teams"][0])

    def get_player(self, player_id: int) -> Player:
        """
        Get player information.

        Args:
            player_id: The MLB player ID

        Returns:
            Player information
        """
        endpoint = f"{self.BASE_URL}/people/{player_id}"
        response = self.session.get(endpoint)
        response.raise_for_status()
        data = response.json()
        return Player(**data["people"][0])

    def get_teams(self) -> List[Team]:
        """
        Get all teams.

        Returns:
            List of teams
        """
        endpoint = f"{self.BASE_URL}/teams"
        params = {"sportId": 1}  # MLB
        response = self.session.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        return [Team(**team) for team in data["teams"]]
