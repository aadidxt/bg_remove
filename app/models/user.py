from datetime import date
import uuid

DAILY_LIMIT = 2

# In-memory user usage store:
# {
#   "<uid>": {
#       "created_at": "YYYY-MM-DD",
#       "usage_by_day": {"YYYY-MM-DD": <count>}
#   }
# }
USERS = {}


def create_user():
    uid = str(uuid.uuid4())
    USERS[uid] = {
        "created_at": date.today().isoformat(),
        "usage_by_day": {},
    }
    return uid


def get_or_create_user(uid):
    if uid not in USERS:
        USERS[uid] = {
            "created_at": date.today().isoformat(),
            "usage_by_day": {},
        }
    return USERS[uid]


def get_today_usage(uid):
    user = get_or_create_user(uid)
    today = date.today().isoformat()
    used = user["usage_by_day"].get(today, 0)
    return {"uid": uid, "date": today, "used": used, "limit": DAILY_LIMIT}


def consume_usage(uid):
    user = get_or_create_user(uid)
    today = date.today().isoformat()
    used = user["usage_by_day"].get(today, 0)

    if used >= DAILY_LIMIT:
        return {"allowed": False, "uid": uid, "date": today, "used": used, "limit": DAILY_LIMIT}

    used += 1
    user["usage_by_day"][today] = used
    return {"allowed": True, "uid": uid, "date": today, "used": used, "limit": DAILY_LIMIT}


def get_users_register():
    today = date.today().isoformat()
    rows = []

    for uid, user in USERS.items():
        used = user["usage_by_day"].get(today, 0)
        rows.append({
            "uid": uid,
            "date": today,
            "used": used,
            "limit": DAILY_LIMIT,
            "remaining": max(0, DAILY_LIMIT - used),
            "created_at": user["created_at"],
        })

    rows.sort(key=lambda row: row["created_at"])
    return rows
