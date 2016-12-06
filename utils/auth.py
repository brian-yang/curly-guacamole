import hashlib
import sqlite3

def register(user, password):
    f = "data/users.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    check_user = "SELECT * FROM user_credentials WHERE user=?"
    entry = c.execute(check_user, (user,)).fetchone()
    if entry is None:
        register_user = "INSERT INTO user_credentials (username, password) VALUES (?, ?)"
        c.execute(register_user, (user, hashlib.sha512(password).hexdigest()))
        success = True
    else:
        success = False

    c.close()
    db.commit()
    db.close()

    return success

def login(user, password):
    f = "data/users.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    check_user = "SELECT * FROM user_credentials WHERE user=?"
    entry = c.execute(check_user, (user,)).fetchone()

    c.close()
    db.commit()
    db.close()

    if entry is None:
        return False
    elif hashlib.sha512(password).hexdigest() != entry[1]:
        return False
    else:
        return True
