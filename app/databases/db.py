import sqlite3

# Create a connection and cursor for the SQLite database
conn = sqlite3.connect('app/database.db')
cursor = conn.cursor()