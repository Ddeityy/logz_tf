from pydantic import BaseModel


class LogBase(BaseModel):
    log_id: int
    title: str
    map: str
    date: int
    views: int
    player_count: str
    players: str


class LogCreate(LogBase):
    pass


class LogSchema(LogBase):
    id: int

    class Config:
        orm_mode = True
