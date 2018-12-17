import sqlite3

conn = sqlite3.connect('barter.db')
print("Opened db succesfully!")

conn.execute('''CREATE TABLE ASSET_CATEGORY (ASSET_CAT_ID INT PRIMARY KEY NOT NULL, ASSET_CATEGORY_NAME TEXT NOT NULL)''')
conn.execute('''CREATE TABLE ASSET (ASSET_ID INT PRIMARY KEY NOT NULL, 
                        ASSET_CAT_ID  INT,
                        ASSET_NAME CHAR(100),
                        ASSET_AUTHOR CHAR(50),
                        ASSET_COMPANY CHAR(100))''')
conn.execute('''CREATE TABLE USER (USER_ID INT PRIMARY KEY NOT NULL,
                        USER_NAME CHAR(50),
                        USER_EMAIL CHAR(50))''')
conn.execute('''CREATE TABLE  MAP_USER_ASSET_OWNERSHIP_WISH (USER_ID INT, 
                                                ASSET_ID INT,
                                                ISOWNED BOOLEAN,
                                                ISWISH BOOLEAN)''')
print("Opened db succesfully!")
conn.close()

