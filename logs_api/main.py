from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session
import uvicorn

from crud import *
from models import *
from schemas import *
from db import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/logs/", response_model=list[Log])
def read_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logs = get_logs(db)
    return logs


@app.get("/logs/{log_id}")
def read_user(log_id: int, db: Session = Depends(get_db)):
    log = get_log(db, log_id=log_id)
    if log is None:
        raise HTTPException(status_code=404, detail="User not found")
    return log


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
