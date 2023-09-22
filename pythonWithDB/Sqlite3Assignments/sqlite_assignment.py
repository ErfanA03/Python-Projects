"""
import sqlite3
connection = sqlite3.connect("test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, Age INT)")

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

connection.commit()

connection = sqlite3.connect(':memory:')

c.execute("DROP TABLE IF EXISTS People")

connection.close()

with sqlite3.connect("test_database.db") as connection:
    # perform any SQL operations using connection here
"""




"""
#If you want to run more than one SQL code at a time, there are a couple possible options.
#One is to use executescript() method and give it a string that represents a full script.

import sqlite3
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript(\"""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
                    \""")

#We can also execute many similar statements by using the executemany()
#method and supplying a tuple of tuples where each inner tuple supplies
#the information for a single command.

peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)
"""




"""
import sqlite3

#get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

# execute insert statement for supplied person data
with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName + "', '"+ lastName +"', " +str(age) +")"
    c.execute(line)
    print(line)

"""




"""
But what if the user's name includes a apostrophe? Try adding a
name with an apostrophe and you'll see that is breaks the code because the
apostrophe gets mixed up with the single quotes in the line, making it
appear that the SQL code ends earlier than expected.

In this case, our code only causes an error(Which is bad)
instead of corrupting the entire table (Which would be very bad),
but there are many other hard-to-predict cases that can break SQL
tables when not parameterizing your statements. To avoid this
in the future, we should use placeholders in our SQL code
and inserted the person data as a tuple.
"""


"""
import sqlite3

#get personal data from user and insert into a tuple
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName,lastName,age)

# execute insert statement for supplied person data
with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?,?,?)", personData)
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName =?",
              (45, "Luigi", "Vercotti"))
"""

import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?,?,?)",
                  peopleValues)

# select all first and last names from people over age 30
"""
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print(row)
"""


"""
    If we wanted to loop over our results rows one at a time instead of fetching
    them all at once, we would usually use a loop such as the following:
"""
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)

  


