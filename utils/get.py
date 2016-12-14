import urllib, urllib2, sqlite3, unirest

f = open('keys.txt','r')
apikeys = []
for line in f:
    key = line.strip('\n')
    apikeys.append(key)
api_key = apikeys[1]

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

def get_bmi(username):
    url = "https://bmi.p.mashape.com/"
    headers = {
        "X-Mashape-Key": api_key,
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
