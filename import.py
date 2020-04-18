#/usr/bin/python

""" Import script that takes in a file characters.csv 
and puts each line that represents a student into
database: students.db (sqlite3)

characters.csv schema: name, house, birth 
Example row: Adelaide Murton,Slytherin,1982"""


import csv
import getopt
import sqlite3
import sys


# Tweak this variable if SQLite DB name changes...
SQLITE_DATABASE='students.db'


def main(argv):
    import_file = ''
    if not argv:
        print("ERROR... Please supply an import file...")
        print("ERROR... Correct usage: import.py -i <import_file>")
        sys.exit(2)
    try:
        opts, args = getopt.getopt(argv, "hi:",["input"])
    except getopt.GetoptError:
        print("ERROR... Correct usage: import.py -i <import_file>")
        sys.exit(2)
    # Define logic for -h and -i arguments
    for opt, arg in opts:
        if opt == '-h':
            print('import.py -i <import_file>')
            sys.exit()
        elif opt in ("-i", "--input"):
            import_file = arg
    print("You have chosen to import file:  " + import_file + "!")

    # Open characters.csv in read-only mode
    with open(import_file, newline='') as csvfile:
        char_reader = csv.reader(csvfile, delimiter=',')
        # Skip first line
        next(char_reader)
        for row in char_reader:
            full_name = row[0]
            full_name = full_name.split(' ')
            # Length of full name list is 2 meaning just full name, last name
            if len(full_name) == 2:
                first_name = full_name[0]
                middle_name = ''
                last_name = full_name[1]
            else:
                first_name = full_name[0]
                middle_name = full_name[1]
                last_name = full_name[2]   
            house = row[1]
            birth_year = row[2]
            insert_to_db(first_name, middle_name, last_name, house, birth_year)
    
    print(import_file + " has been imported into database: " + SQLITE_DATABASE)

# Helper function 
def insert_to_db(first, middle, last, house, birth):
    """ Takes in values to insert into SQLite3 database...
    first: STRING : first name
    middle: STRING : middle name
    last: STRING : last name
    house: STRING : Harry Potter house that character is a member of
    birth: STRING : birthday of character"""
    
    if middle == '':
        student = (first, last, house, birth)
        sql = '''   INSERT INTO students(first, last, house, birth)
                    VALUES(?,?,?,?)   '''
    else:
        student = (first, middle, last, house, birth)
        sql = '''   INSERT INTO students(first, middle, last, house, birth)
                    VALUES(?,?,?,?,?)   '''
    # Build connection to students.db database
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()


if __name__ == "__main__":
    main(sys.argv[1:])