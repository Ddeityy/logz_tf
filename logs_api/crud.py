from sqlalchemy.orm import Session
from requests import get
from models import *
import json


def get_log(db: Session, log_id: int):
    q = db.query(Log).filter(Log.log_id == log_id).first()
    try:
        with open(q.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except:
        return


def get_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Log).offset(skip).limit(limit).all()


def create_data(db: Session):
    response = get("https://logs.tf/api/v1/log?limit=5000")
    gjdata = response.json()

    for i, log in enumerate(gjdata["logs"]):
        res = get(f"https://logs.tf/api/v1/log/{log['id']}")
        jdata = res.json()
        with open(f"logs/{log['id']}.json", "w", encoding="utf-8") as f:
            json.dump(jdata, f, ensure_ascii=False, indent=4)
            print(f"log {i}/{len(gjdata)}")

        l = Log(
            log_id=int(log["id"]),
            title=log["title"],
            date=int(log["date"]),
            map=log["map"],
            views=int(log["views"]),
            players=log["players"],
            file_path=f"logs/{log['id']}.json",
        )
        db.add(l)
        print("log added")
    db.commit()
