import sqlite3    # Imports the sqlite3 module.

conn = sqlite3.connect('School.db') # Connect to the SQLite database

with conn:    #With our connection open...
    cur = conn.cursor() # This allows us to make changes within the Database.
    #Creating our table if it doesn't already exists
    cur.execute('CREATE TABLE IF NOT EXISTS school_table( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )')


# List of file names
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')



# Loop through the items in "fileList"
for x in fileList:
    """
        If the item ends with '.txt', execute the insert statement
        in SQL, substituting the '?' for the 'x' which is our current item
        and finally printing it.
    """
    if x.endswith('.txt'):
        cur.execute('INSERT INTO school_table (col_fname) VALUES (?)', (x,))
        print(x)



conn.commit() # Commit the changes to the database.
conn.close() # Close our connection to the database.

