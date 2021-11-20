import sqlite3

def check_db():
    databaseFile = ("data.db")
    db = sqlite3.connect(databaseFile, check_same_thread=False)
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        print("DB was(1/2) found")
    except sqlite3.OperationalError:
        print("DB was(1/2) not found")
        cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT)")
        print("DB was(1/2) create...")

def get_users_exist(user_id):
    db = sqlite3.connect("data.db", check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id, ))
    if cursor.fetchone() is None:
        return False
    else:
        return True

def add_user_to_db(user_id):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    user = [user_id]
    cursor.execute(f'''INSERT INTO users(user_id) VALUES(?)''', user)
    db.commit()

def add_new_file(user_id, type, code, file_id):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    data = [user_id, type, code, file_id]
    cursor.execute(f'''INSERT INTO files(user_id, type, code, file_id) VALUES(?,? ,? ,?)''', data)
    db.commit()

def get_file(code):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT file_id FROM files WHERE code=?", (code, ))
    fileID = cursor.fetchone()
    cursor.execute("SELECT type FROM files WHERE code=?", (code, ))
    type_file = cursor.fetchone()
    return type_file, fileID

def get_files_user(user_id):
    db = sqlite3.connect('data.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("SELECT code FROM files WHERE user_id=?", (user_id, ))
    fileIDs = cursor.fetchall()
    cursor.execute("SELECT type FROM files WHERE user_id=?", (user_id, ))
    types_my_file = cursor.fetchall()
    return types_my_file, fileIDs