import sqlite3

def get_info(username, query):
    db = sqlite3.connect('data/users.db')
    c = db.cursor()
    s = c.execute(query, (username,))
    return s.fetchone()

def get_calories(username):
    query = 'SELECT * FROM calorie_tracker WHERE username=?'
    info = get_info(username, query)
    return [info[1], info[2], info[3]]

def get_user_data(username):
    query = 'SELECT * FROM user_diagnostics WHERE username=?'
    info = get_info(username, query)
    return [info[1], info[2], info[3], info[4]]

#def get_bmi():
    
