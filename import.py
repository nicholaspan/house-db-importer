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


def main(argv):
    import_file = ''
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
    print("Importing " + import_file + "...")

    # Open characters.csv in read-only mode
    with open(import_file, newline='') as csvfile:
        char_reader = csv.reader(csvfile, delimiter=',')
        # Skip first line
        next(char_reader)
        for row in char_reader:
            full_name = row[0]
            print(full_name)
            full_name = full_name.split(' ')
            print(full_name)
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

# Helper function 
def insert_to_db(first, middle, last, house, birth):
    """ Takes in values to insert into SQLite3 database...
    first: STRING : first name
    middle: STRING : middle name
    last: STRING : last name
    house: STRING : Harry Potter house that character is a member of
    birth: STRING : birthday of character"""
    print("Inside insert_to_db!")
    pass


if __name__ == "__main__":
    main(sys.argv[1:])