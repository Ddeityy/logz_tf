import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from pysteamsignin.steamsignin import SteamSignIn
from sqlalchemy.orm import Session

from crud import get_log, get_logs, get_user_logs, create_data
from db import SessionLocal, engine, Base
from schemas import LogSchema
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:5173",
]

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
def main(login=None):
    if login is not None:
        steamLogin = SteamSignIn()
        # Flask expects an explicit return on the route.
        return steamLogin.RedirectUser(
            steamLogin.ConstructURL("http://localhost:8003/processlogin")
        )

    return HTMLResponse('Click <a href="auth/?login=true">to log in</a>')


@app.get("/processlogin/")
def process(request: Request):
    steamLogin = SteamSignIn()
    steamID = steamLogin.ValidateResults(request.query_params)

    if steamID is not False:
        return steamID
    else:
        return RedirectResponse("http://localhost:8003/")


@app.get("/")
def index_redirect():
    return RedirectResponse("http://localhost:8003/logs")


@app.get("/user/{user_id}", response_model=list[LogSchema])
def read_user_logs(user_id: int, db: Session = Depends(get_db)):
    logs = get_user_logs(user_id, db)
    return logs


@app.get("/create/")
def create(db: Session = Depends(get_db)):
    create_data(db)
    return True


@app.get("/logs/", response_model=list[LogSchema])
def read_logs(
    skip: int = 0,
    limit: int = 1000,
    db: Session = Depends(get_db),
    players: str | None = None,
):
    logs = get_logs(db, skip=skip, limit=limit)
    return logs


@app.get("/logs/{log_id}")
def read_user(log_id: int, db: Session = Depends(get_db)):
    log = get_log(db, log_id=log_id)
    if log is None:
        raise HTTPException(status_code=404, detail="User not found")
    return log


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
