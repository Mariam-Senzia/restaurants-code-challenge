import sqlite3

CONN = sqlite3.connect('hospitality.db')
CURSOR = CONN.cursor()