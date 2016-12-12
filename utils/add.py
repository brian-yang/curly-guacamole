import sqlite3
from time import strftime

def add_meal(username, meal_name, calories):
    f = "data/storyteller.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    date = get_date()
    check_calories_today = "SELECT * FROM calorie_count WHERE username=? AND date=?"
    rows = c.execute(check_calorie_today, (username, date))

    if not rows:
        # add story to the next row
        add_calories = "INSERT INTO calorie_count (username, date, meals, calories) VALUES(?, ?, ?, ?)"
        c.execute(add_story, (username, get_time(), title, creator, base_content))

    update_story_ids = "UPDATE users SET story_ids=? where user=?"
    c.execute(update_story_ids, (id_list, creator))
        
    c.close()
    
    db.commit()
    db.close()
    

def get_date():
    return strftime("%Y-%m-%d")
