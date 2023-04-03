import sqlite3 as lite

person = (
    (1,'James','Smith',41),
    (2,'Diana','Greene',23),
    (3,'Sara','White',27),
    (4,'William','Gibson',23)
)

pet = (
    (1,'Rusty','Dalmation',4,1),
    (2,'Bella','Alaskan Malamute',3,0),
    (3,'Max','Cocker Spaniel',1,0),
    (4,'Rocky','Beagle',7,0),
    (5,'Rufus','Cocker Spaniel',1,0),
    (6,'Spot','Bloodhound',2,1)
)

person_pet = (
    (1,1),
    (1,2),
    (2,3),
    (2,4),
    (3,5),
    (4,6)
)
con = lite.connect('pets.db')

with con:

    cur = con.cursor()

    # Creating the person table
    cur.execute("DROP TABLE IF EXISTS person")
    cur.execute("CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
    cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", person)

    # Creating the pet table
    cur.execute("DROP TABLE IF EXISTS pet")
    cur.execute("CREATE TABLE pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
    cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pet)

    # Creating the person_pet table
    # 2. What is the purpose of the person_pet table?
    # The purpose of the person_pet table is to establish relationships between the person and pet data,
    # It will be easier to query specific columns from both the pet and person tables and join them 
    cur.execute("DROP TABLE IF EXISTS person_pet")
    cur.execute("CREATE TABLE person_pet(person_id INTEGER, pet_id INTEGER)")
    cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)

