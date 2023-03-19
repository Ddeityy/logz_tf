from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    log_id = Column(Integer, index=True)
    title = Column(String)
    map = Column(String)
    date = Column(Integer)
    views = Column(Integer)
    players = Column(Integer)
    file_path = Column(String)
