import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from pysteamsignin.steamsignin import SteamSignIn
from sqlalchemy.orm import Session
import requests
import os
from dotenv import load_dotenv

from crud import get_log, get_logs, get_user_logs, create_data, get_logs_total
from db import SessionLocal, engine, Base
from schemas import LogSchema
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["http://localhost", "http://localhost:5174", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/auth")
def main():
    steamLogin = SteamSignIn()
    return steamLogin.ConstructURL("http://localhost:5174/processlogin")


@app.get("/")
def index_redirect():
    return RedirectResponse("http://localhost:8003/logs")


@app.get("/user/info/{user_id}")
async def get_user_info(user_id: int):
    load_dotenv()
    key = os.getenv("STEAM_API")
    resp = requests.get(
        f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={user_id}"
    )
    data = resp.json()
    return data


@app.get("/user/{user_id}", response_model=list[LogSchema])
def read_user_logs(user_id: int, db: Session = Depends(get_db)):
    logs = get_user_logs(user_id, db)
    return logs


@app.get("/create/")
def create(db: Session = Depends(get_db)):
    create_data(db)
    return True


@app.get("/total/")
def read_total_logs(db: Session = Depends(get_db)):
    return get_logs_total(db)


@app.get("/logs/", response_model=list[LogSchema])
def read_logs(
    offset: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    players: str | None = None,
):
    logs = get_logs(db, skip=offset, limit=limit)
    return logs


@app.get("/logs/{log_id}")
def read_user(log_id: int, db: Session = Depends(get_db)):
    log = get_log(db, log_id=log_id)
    if log is None:
        raise HTTPException(status_code=404, detail="User not found")
    return log


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
