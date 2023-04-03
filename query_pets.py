import sqlite3 as lite
person_id_number = None

# connect to the databaste
con = lite.connect('pets.db')
cur = con.cursor()

# ask the user for a person's id number
while person_id_number != '-1':
    person_id_number = input("Please type in the person's ID number:")

    # if the id is -1, quit the program
    if person_id_number == '-1':
        print("Good Bye!")
        break

    # retrieve the data related to the person with the id
    cur.execute("""
    SELECT * FROM person
    WHERE person.id = {}
    """.format(person_id_number))
    person_selected = cur.fetchone()

    # if the person's id does not exist, display an error message and continue for input
    if person_selected == None:
        print("Sorry, the input id does not exist")

    # if person's id number exist:
        # print('the person's data')
        # print('all the pets that person has and their data)
    else:
        print("{} {}, {} years old.".format(person_selected[1], person_selected[2], person_selected[3]))
        cur.execute("""
        SELECT person.first_name, person.last_name, pet.name, pet.breed, pet.age, pet.dead FROM person
        INNER JOIN person_pet ON person.id = person_pet.person_id
        INNER JOIN pet ON pet.id = person_pet.pet_id
        WHERE person.id = {}
        """.format(person_id_number))

        person_selected_pets = cur.fetchall()

        for each_pet in person_selected_pets:
            if each_pet[5] == 1:
                print("{} {} owned {}, a {}, that was {} years old".format(each_pet[0], each_pet[1], each_pet[2], each_pet[3], each_pet[4]))
            else:
                print("{} {} owns {}, a {}, that is currently {} years old".format(each_pet[0], each_pet[1], each_pet[2], each_pet[3], each_pet[4]))

print("___END___")

if __name__ == "__main__":
    pass
