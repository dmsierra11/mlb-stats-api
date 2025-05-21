"""MLB Stats API models."""

from typing import List, Optional

from pydantic import BaseModel, Field


class Player(BaseModel):
    """Player model."""

    id: int
    fullName: str
    firstName: str
    lastName: str
    primaryNumber: Optional[str] = None
    birthDate: Optional[str] = None
    currentAge: Optional[int] = None
    birthCity: Optional[str] = None
    birthCountry: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[int] = None
    active: bool
    primaryPosition: Optional[dict] = None
    useName: Optional[str] = None
    middleName: Optional[str] = None
    boxscoreName: Optional[str] = None
    gender: Optional[str] = None
    isPlayer: bool
    isVerified: bool
    draftYear: Optional[int] = None
    mlbDebutDate: Optional[str] = None
    batSide: Optional[dict] = None
    pitchHand: Optional[dict] = None
    nameFirstLast: Optional[str] = None
    nameSlug: Optional[str] = None
    firstLastName: Optional[str] = None
    lastFirstName: Optional[str] = None
    lastInitName: Optional[str] = None
    initLastName: Optional[str] = None
    fullFMLName: Optional[str] = None
    fullLFMName: Optional[str] = None
    strikeZoneTop: Optional[float] = None
    strikeZoneBottom: Optional[float] = None


class PlayerStats(BaseModel):
    """Player statistics model."""

    type: dict
    group: dict
    stats: List[dict]
    season: Optional[str] = None


class Team(BaseModel):
    """Team model."""

    id: int
    name: str
    teamCode: str
    fileCode: Optional[str] = None
    abbreviation: str
    teamName: str
    locationName: str
    firstYearOfPlay: Optional[str] = None
    league: Optional[dict] = None
    division: Optional[dict] = None
    sport: Optional[dict] = None
    shortName: Optional[str] = None
    franchiseName: Optional[str] = None
    clubName: Optional[str] = None
    allStarStatus: Optional[str] = None
    active: bool
    springLeague: Optional[dict] = None
    link: Optional[str] = None
    season: Optional[int] = None
    venue: Optional[dict] = None
    springVenue: Optional[dict] = None


class RosterPlayer(BaseModel):
    """Roster player model."""

    person: dict  # Contains id, fullName, and link
    jerseyNumber: Optional[str] = None
    position: dict
    status: Optional[dict] = None
    parentTeamId: Optional[int] = None


class SearchResponse(BaseModel):
    """Search response model."""

    people: List[Player] = Field(default_factory=list)
    totalSize: int = 0
