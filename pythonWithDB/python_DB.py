import sqlite3

conn = sqlite3.connect('School.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS school_table( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )')

    fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

    for x in fileList:
        if x.endswith('.txt'):
            cur.execute('INSERT INTO school_table (col_fname) VALUES (?)', (x,))
            print(x)

    cur.execute('DROP TABLE IF EXISTS school_table')

conn.commit()
conn.close()
