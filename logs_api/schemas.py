from pydantic import BaseModel


class LogBase(BaseModel):
    log_id: int
    title: str
    map: str
    date: int
    views: int
    players: str
    file_path: str


class LogCreate(LogBase):
    pass


class Log(LogBase):
    id: int

    class Config:
        orm_mode = True
