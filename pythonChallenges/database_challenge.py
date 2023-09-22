
# Import Modules
import sqlite3



# Creating a connection to our database in our RAM memory
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Creating our table "Roster"
cursor.execute("""CREATE TABLE Roster (
                Name TEXT,
                Species TEXT,
                IQ INTEGER
                )""")

# Populating our table with values
cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", ('Jean-Baptiste Zorg', 'Human', 122))
cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", ('Korben Dallas', 'Meat Popsicle', 100))
cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", ('Ak\'not', 'Mangalore', -5))

# Update the Species of Korben Dallas to be Human
cursor.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")

# Display the names and IQs of everyone classified as Human
cursor.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
humans = cursor.fetchall()

for human in humans:
    print("Name:", human[0])
    print("IQ:", human[1])
    print() #Added an extra print statement for readabilty purposes.

# Close the connection
conn.close()

a = range(0,10)
print(a)

for i in a:
    print(i)
