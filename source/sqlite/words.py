import os
import sqlite3
from functools import reduce

DB_DIR = './resources'

if not os.path.exists(DB_DIR):
    os.mkdir(DB_DIR)

DB_NAME = '/main.db'


class Word:
    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.value = value

    def __getitem__(self, item_name):
        if item_name == 'word':
            return self.name
        elif item_name == 'value':
            return self.value

        return self.id


class Words:
    def __init__(self):
        self._connection = sqlite3.connect(DB_DIR + DB_NAME)

        cursor = self._connection.cursor()
        cursor.executescript("""
        create table if not exists words (
            id integer primary key autoincrement,
            name varchar(128) not null,
            value integer default 0
        );
        """)

        self._connection.commit()
        cursor.close()

    def __del__(self):
        self._connection.close()

    def get_not(self, ids=None):
        if ids is None:
            ids = []

        cursor = self._connection.cursor()
        cursor.row_factory = lambda c, line: Word(line[0], line[1], line[2])
        statement = "" \
            if len(ids) == 0 \
            else " where id not in (" + reduce(
                lambda id1, id2: str(id1) + ", " + str(id2),
                ids,
                ""
            ).lstrip(",") + ")"
        cursor.execute("select * from words" + statement)

        result = cursor.fetchone()
        self._connection.commit()
        cursor.close()

        return result
