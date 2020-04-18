#/usr/bin/python

""" Roster script that will accept a particular Harry Potter
house and output the names & birth years of students in tha
particular house.

Sample usage: roster.py -h gryffindor
Sample output: Harry James Potter, born 1980"""


import csv
import getopt
import sqlite3
import sys

def main(argv):
    house = ''
    try:
        opts, args = getopt.getopt(argv, "h:",["house"])
    except getopt.GetoptError:
        print("ERROR... Correct usage: import.py -h <house>")
        sys.exit(2)
    if not argv:
        print("ERROR... Correct usage: import.py -h <house>")
        sys.exit(2)
    # Define logic for -h argument
    for opt, arg in opts:
        if opt in ("-h", "--house"):
            house = arg
    # Check input to confirm it is a valid Harry Potter house
    if house.lower() not in ("gryffindor", "slytherin", "hufflepuff", "ravenclaw"):
        print("ERROR... Please choose a correct house!")
        print("Valid house values: gryffindor, slytherin, hufflepuff, ravenclaw.")
        sys.exit(2)
    print("You have chosen to check roster of house: " + house + "!")
    house = house[0].upper() + house[1:] # Force first letter capitalized
    students_in_house = query_db_for_house(house)
    for student in students_in_house:
        if student[1]:
            print(student[0]+" "+student[1]+" "+student[2]+", born "+str(student[3]))
        else:
            print(student[0]+" "+student[2]+", born "+str(student[3]))

def query_db_for_house(house):
    """ Takes in a house and returns list of tuples 
    [(first, middle, last, birth)... n]"""
    
    # Build connection to students.db database
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()

    sql = '''   SELECT first, middle, last, birth FROM students 
                WHERE house=? ORDER BY last, first'''

    cur.execute(sql, (house,))
    return cur.fetchall()


if __name__ == "__main__":
    main(sys.argv[1:])