from sqlalchemy import Column, Integer, String

from db import Base


class LogModel(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    log_id = Column(Integer, index=True)
    title = Column(String)
    map = Column(String, index=True)
    date = Column(Integer)
    views = Column(Integer)
    player_count = Column(Integer)
    players = Column(String, index=True)
    file_path = Column(String)
