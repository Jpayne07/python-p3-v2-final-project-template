import sqlite3

CONN = sqlite3.connect('jobboard.db')
CURSOR = CONN.cursor()
