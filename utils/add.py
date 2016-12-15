import sqlite3
from time import strftime

def get_date():
    return strftime("%Y-%m-%d")

def add_meal(username, meal_name, calories):
    f = "data/users.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    date = get_date()
    check_calories_today = "SELECT meals, calorie_count FROM calorie_tracker WHERE username=? AND date=?"
    rows = c.execute(check_calories_today, (username, date)).fetchone()

    if not rows:
        add_calories = "INSERT INTO calorie_tracker (username, date, meals, calorie_count) VALUES(?, ?, ?, ?)"
        c.execute(add_calories, (username, get_date(), meal_name, calories));
    else:
        add_calories = "UPDATE calorie_tracker SET meals=?, calorie_count=? WHERE username=? AND date=?"
        c.execute(add_calories, (str(rows[0]) + "|" + meal_name, float(rows[1]) + float(calories), username, date))

    c.close()

    db.commit()
    db.close()

def add_profile(username, gender, age, height, weight):
    f = "data/users.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    add_calories = "INSERT INTO user_diagnostics (username, gender, age, height, weight) VALUES(?, ?, ?, ?, ?)"
    c.execute(add_calories, (username, gender, age, height, weight));

    c.close()

    db.commit()
    db.close()
