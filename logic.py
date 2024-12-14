from bot import info
import sqlite3

class DB_Manager:
        def __init__(self, database):
            self.database = database # имя базы данных
            
        def create_tables(self):
            conn = sqlite3.connect(self.database)
            with conn:
                conn.execute("""
    CREATE TABLE Questions(chatid TEXT, name TEXT, message TEXT);""")
                conn.commit()
        def new_question(self):
            conn = sqlite3.connect(self.database)
            with conn:
                conn.execute(f"""
    INSERT INTO Questions (chatid, name, message) VALUES ({info});""")    