import json

from requests import get
from sqlalchemy.orm import Session
from steamid_converter.Converter import to_steamID3

from models import LogModel


def get_log(db: Session, log_id: int):
    q = db.query(LogModel).filter(LogModel.log_id == log_id).first()
    try:
        with open(q.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception as e:
        return e


def get_user_logs(user_id: int, db: Session):
    id = to_steamID3(user_id)
    return db.query(LogModel).filter(LogModel.players.contains(id)).all()


def get_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LogModel).offset(skip).limit(limit).all()


def create_data(db: Session):
    response = get("https://logs.tf/api/v1/log?limit=5000")
    gjdata = response.json()

    for i, log in enumerate(gjdata["logs"]):
        if int(log["players"]) == 12 or 18:
            res = get(f"https://logs.tf/api/v1/log/{log['id']}")
            jdata = res.json()
            with open(f"logs/{log['id']}.json", "w", encoding="utf-8") as f:
                json.dump(jdata, f, ensure_ascii=False, indent=4)
                print(f"log {i}/{len(gjdata['logs'])}")

            db.add(
                LogModel(
                    log_id=int(log["id"]),
                    title=log["title"],
                    date=int(log["date"]),
                    map=log["map"],
                    views=int(log["views"]),
                    player_count=log["players"],
                    file_path=f"logs/{log['id']}.json",
                    players=",".join([player for player in jdata["players"]]),
                )
            )
            print("log added")
            db.commit()
        else:
            print("log skipped")
