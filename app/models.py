from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()


class Team(Base):
    """Model representing an EPL team."""
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    short_name = Column(String(10), unique=True, nullable=False)
    code = Column(String(3), unique=True, nullable=False)
    founded_year = Column(Integer)
    stadium = Column(String(100))
    manager = Column(String(100))
    logo_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    home_matches = relationship(
        'Match',
        foreign_keys='Match.home_team_id',
        back_populates='home_team',
        cascade='all, delete-orphan'
    )
    away_matches = relationship(
        'Match',
        foreign_keys='Match.away_team_id',
        back_populates='away_team',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"<Team {self.name}>"


class Match(Base):
    """Model representing an EPL match."""
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    home_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    away_team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    kickoff_time = Column(DateTime, nullable=False, index=True)
    season = Column(Integer, nullable=False)  # e.g., 2024 for 2024-2025 season
    gameweek = Column(Integer, nullable=False)
    status = Column(String(20), default='scheduled')  # scheduled, ongoing, completed
    home_score = Column(Integer)
    away_score = Column(Integer)
    result = Column(String(1))  # 'H' for home win, 'D' for draw, 'A' for away win
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Foreign keys
    home_team = relationship(
        'Team',
        foreign_keys=[home_team_id],
        back_populates='home_matches'
    )
    away_team = relationship(
        'Team',
        foreign_keys=[away_team_id],
        back_populates='away_matches'
    )

    # Relationships
    predictions = relationship(
        'Prediction',
        back_populates='match',
        cascade='all, delete-orphan'
    )
    statistics = relationship(
        'MatchStatistic',
        back_populates='match',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"<Match {self.home_team.name} vs {self.away_team.name} ({self.kickoff_time})>"


class PredictionOutcome(str, enum.Enum):
    """Enum for prediction outcomes."""
    HOME_WIN = "H"
    DRAW = "D"
    AWAY_WIN = "A"


class Prediction(Base):
    """Model representing a prediction for a match."""
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'), nullable=False, index=True)
    predicted_outcome = Column(Enum(PredictionOutcome), nullable=False)  # H, D, A
    confidence = Column(Float, nullable=False)  # 0.0 to 1.0
    predicted_home_score = Column(Integer)
    predicted_away_score = Column(Integer)
    model_version = Column(String(50))  # e.g., "v1.0", "v2.1"
    is_correct = Column(Boolean)  # True if prediction matches result, False otherwise
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    match = relationship('Match', back_populates='predictions')

    def __repr__(self):
        return f"<Prediction Match {self.match_id} - {self.predicted_outcome} ({self.confidence:.2%})>"


class MatchStatistic(Base):
    """Model representing match statistics and detailed metrics."""
    __tablename__ = 'match_statistics'

    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'), nullable=False, index=True)
    
    # Home team stats
    home_possession = Column(Float)  # Percentage
    home_shots = Column(Integer)
    home_shots_on_target = Column(Integer)
    home_corners = Column(Integer)
    home_fouls = Column(Integer)
    home_yellow_cards = Column(Integer)
    home_red_cards = Column(Integer)
    home_passes = Column(Integer)
    home_pass_accuracy = Column(Float)  # Percentage
    home_tackles = Column(Integer)
    home_interceptions = Column(Integer)
    
    # Away team stats
    away_possession = Column(Float)  # Percentage
    away_shots = Column(Integer)
    away_shots_on_target = Column(Integer)
    away_corners = Column(Integer)
    away_fouls = Column(Integer)
    away_yellow_cards = Column(Integer)
    away_red_cards = Column(Integer)
    away_passes = Column(Integer)
    away_pass_accuracy = Column(Float)  # Percentage
    away_tackles = Column(Integer)
    away_interceptions = Column(Integer)
    
    # Additional metrics
    total_shots = Column(Integer)
    total_shots_on_target = Column(Integer)
    expected_goals_home = Column(Float)  # xG for home team
    expected_goals_away = Column(Float)  # xG for away team
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    match = relationship('Match', back_populates='statistics')

    def __repr__(self):
        return f"<MatchStatistic Match {self.match_id}>"
