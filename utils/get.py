import urllib, urllib2
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

# def get_bmi(bmi_info):
#     method = "POST"
#     handler = urllib2.HTTPHandler()
#     opener = urllib2.build_opener(handler)
    
#     data = urllib.urlencode(bmi_info)
    
#     request = urllib2.Request("https://bmi.p.mashape.com/", data)
#     request.add_header("X-Mashape-Key", "jnUlXZCfZwmshKWvP2b4Sb1bEFwpp1GNDRcjsnsXHRQvWIdpkF")
#     request.add_header("Content-Type", "application/json")
#     request.add_header("Accept", "application/json")
#     request.get_method = lambda: method
    
#     try:
#         connection = opener.open(request)
#     except urllib2.HTTPError, e:
#         connection = e

#     if connection.code == 200:
#         result = connection.read()
#         print result
#     else:
#         print connection.code
        

# bmi = {"weight": {"value":"85.00","unit":"kg"},"height":{"value":"170.00","unit":"cm"},"sex":"m","age":"24"}
# get_bmi(bmi)
