import sqlite3
from time import strftime

def add_meal(username, meal_name, calories):
    f = "data/users.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    date = get_date()
    check_calories_today = "SELECT meals FROM calorie_count WHERE username=? AND date=?"
    rows = c.execute(check_calorie_today, (username, date))

    if not rows:
        # add story to the next row
        add_calories = "INSERT INTO calorie_count (username, date, meals, calories) VALUES(?, ?, ?, ?)"
        c.execute(add_calories, (username, get_date(), meal_name, calories));
    else:
        add_calories = "UPDATE calorie_count"
        c.execute(add_calories, (username, get_date(), rows[0] + "|" + meal_name, calories))

    c.close()
    
    db.commit()
    db.close()
    
def get_date():
    return strftime("%Y-%m-%d")

def add_profile(username, gender, age, height, weight):
    f = "data/users.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    # add story to the next row
    add_calories = "INSERT INTO user_diagnostics (username, gender, age, height, weight) VALUES(?, ?, ?, ?, ?)"
    c.execute(add_calories, (username, gender, age, height, weight));

    c.close()
    
    db.commit()
    db.close()    
