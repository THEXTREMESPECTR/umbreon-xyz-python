import sqlite3

conn = sqlite3.connect("test.sqlite")

cursor = conn.cursor()

create_user_table = """CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    username VARCHAR(16),
    password VARCHAR(22),
    banned VARCHAR(3)
);
"""

insert_into_user = ''' INSERT INTO users(id,username,password,banned)               VALUES(1,"THEXTREMESPECTR","Deadpool98","n") '''

