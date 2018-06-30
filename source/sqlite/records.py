import os
import sqlite3

DB_DIR = './resources'

if not os.path.exists(DB_DIR):
    os.mkdir(DB_DIR)

DB_NAME = '/main.db'


class Record:
    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.value = value

    def __getitem__(self, item_name):
        if item_name == 'score':
            return self.value
        elif item_name == 'player':
            return self.name

        return self.id


class Records:
    def __init__(self):
        self._connection = sqlite3.connect(DB_DIR + DB_NAME)

        cursor = self._connection.cursor()
        cursor.executescript("""
        create table if not exists records (
            id integer primary key autoincrement,
            name varchar(128) not null,
            value integer default 0
        );
        """)

        self._connection.commit()
        cursor.close()

    def __del__(self):
        self._connection.close()

    def get(self, count=5):
        cursor = self._connection.cursor()
        cursor.row_factory = lambda c, line: Record(line[0], line[1], line[2])
        cursor.execute("select * from records order by value desc;")

        result = cursor.fetchmany(count)
        self._connection.commit()
        cursor.close()

        return result
