import sqlite3, unirest

# ====================================
def getAPIKeys(pos):
    try:
        f = open("keys.txt","r")
        api_keys = f.readlines()
        return api_keys[pos].strip('\n')
    except:
        print pos
        print "No API keys found."

# ====================================

def get_calories(username):
    db = sqlite3.connect('data/users.db')
    c = db.cursor()

    query = 'SELECT date, meals, calorie_count FROM calorie_tracker WHERE username=?'
    dates = c.execute(query, (username,))

    calorie_tracker = {}
    if not dates:
        return {}
    else:
        for date in dates:
            if not date[1]:
                calorie_tracker[date[0]] = 0
            else:
                calorie_tracker[date[0]] = [date[1], date[2]]

    c.close()
    db.commit()
    db.close()

    return calorie_tracker


def get_user_data(username):
    db = sqlite3.connect('data/users.db')
    c = db.cursor()

    query = 'SELECT * FROM user_diagnostics WHERE username=?'
    info = c.execute(query, (username,)).fetchone()

    c.close()
    db.commit()
    db.close()

    return [info[1], info[2], info[3], info[4]]

def get_bmi(username):
    # Get bmi api key
    api_key_bmi = getAPIKeys(1)

    url = "https://bmi.p.mashape.com/"
    headers = {
        "X-Mashape-Key": api_key_bmi,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    info = get_user_data(username)
    gender = info[0]
    age = info[1]
    height = info[2] * 2.54 #in to cm
    weight = info[3] * 0.45 #lbs to kg
    params = "{\"weight\":{\"value\":\"%s\",\"unit\":\"kg\"},\"height\":{\"value\":\"%s\",\"unit\":\"cm\"},\"sex\":\"%s\",\"age\":\"%s\"}"%(weight, height, gender, age)
    response = unirest.post(url, headers = headers, params = params)
    return response.body
