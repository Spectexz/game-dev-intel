#this file is only to define tables.

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from app.database import Base
from datetime import datetime, timezone, timedelta


wib = timezone(timedelta(hours=7))
last_updated = datetime.now(wib)

class GameSnapshot(Base):
    __tablename__ = 'game_snapshot'

    steam_appid = Column(Integer, primary_key=True)
    name = Column(String(255))
    short_desc = Column(Text, nullable=True) 
    header_image = Column(Text, nullable=True)
    genres = Column(String(255))
    devs = Column(String(255))
    metacritic_score = Column(Integer)
    recommendations = Column(Integer) 
    is_free = Column(Boolean)
    release_date = Column(String(255)) 
    last_updated = Column(DateTime, default=datetime.utcnow, nullable=False)


class TrendingRepo(Base):
    __tablename__ = 'trending_repos'

    repo_name = Column(String, primary_key=True)
    language = Column(String, nullable=True)
    Stars = Column(Integer, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow, nullable=False)