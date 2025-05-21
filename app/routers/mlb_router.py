"""MLB Stats API router."""

from typing import List

from fastapi import APIRouter, HTTPException

from app.models.mlb_models import Player, PlayerStats, RosterPlayer, Team
from app.services.mlb_service import MLBService

router = APIRouter(prefix="/mlb", tags=["mlb"])
mlb_service = MLBService()


@router.get("/players/{player_id}", response_model=Player)
def get_player(player_id: int) -> Player:
    """
    Get player information.

    Args:
        player_id: The MLB player ID

    Returns:
        Player information
    """
    try:
        return mlb_service.get_player(player_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/players/{player_id}/stats", response_model=PlayerStats)
def get_player_stats(
    player_id: int,
    season: int | None = None,
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
    try:
        return mlb_service.get_player_stats(
            player_id, season=season, stats_type=stats_type, group=group
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/teams", response_model=List[Team])
def get_teams() -> List[Team]:
    """
    Get all teams.

    Returns:
        List of teams
    """
    try:
        return mlb_service.get_teams()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/teams/{team_id}", response_model=Team)
def get_team(team_id: int) -> Team:
    """
    Get team information.

    Args:
        team_id: The MLB team ID

    Returns:
        Team information
    """
    try:
        return mlb_service.get_team(team_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/teams/{team_id}/roster", response_model=List[RosterPlayer])
def get_team_roster(team_id: int) -> List[RosterPlayer]:
    """
    Get team roster.

    Args:
        team_id: The MLB team ID

    Returns:
        List of players on the team
    """
    try:
        return mlb_service.get_team_roster(team_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
