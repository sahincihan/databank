import sqlite3

connection = sqlite3.connect('reports.db')
cursor = connection.cursor()

# Create table reports
cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (
    file_hash TEXT PRIMARY KEY,
    file_name TEXT
)
""")

cursor.execute("""

INSERT OR IGNORE INTO  reports (file_hash, file_name) VALUES 
(1111, 'test_file'),
(2222, 'test_file_2'),
(3333, 'test_file_3')
""")


def load_reports():
    connection = sqlite3.connect('reports.db')
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM reports
    """)
    results = cursor.fetchall()
    print(results)
    connection.commit()
    connection.close()



connection.commit()
connection.close()