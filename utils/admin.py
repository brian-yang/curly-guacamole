import sqlite3
import sys

f = "../data/users.db"

db = sqlite3.connect(f)
c = db.cursor()

def create_tables():
    create_users = "CREATE TABLE IF NOT EXISTS user_credentials (username STRING NOT NULL, password STRING NOT NULL);"
    c.execute(create_users)

    create_calorie_tracker = "CREATE TABLE IF NOT EXISTS calorie_tracker (username NOT NULL, date STRING NOT NULL, meals STRING, calorie_count REAL);"
    c.execute(create_calorie_tracker)

    create_user_diagnostics = "CREATE TABLE IF NOT EXISTS user_diagnostics (username STRING NOT NULL, gender STRING NOT NULL, age STRING NOT NULL, height INTEGER NOT NULL, weight INTEGER NOT NULL);"
    c.execute(create_user_diagnostics)

def clear_tables():
    query = "DROP TABLE user_credentials;";
    c.execute(query);

    query = "DROP TABLE calorie_tracker;";
    c.execute(query);

    query = "DROP TABLE user_diagnostics;";
    c.execute(query);

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "Format: python admin.py <0/1>"
    elif int(sys.argv[1]) == 0:
        print "Created tables!"
        create_tables()
    elif int(sys.argv[1]) == 1:
        print "Cleared tables!"
        clear_tables()

c.close()

db.commit()
db.close()
