#/usr/bin/python

""" Import script that takes in a file characters.csv 
and puts each line that represents a student into
database: students.db (sqlite3)

characters.csv schema: name, house, birth 
Example row: Adelaide Murton,Slytherin,1982"""

import csv

import getopt
import sys


def main(argv):
    import_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:",["input"])
    except getopt.GetoptError:
        print("USAGE... import.py -i <import_file>")
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
        for row in char_reader:
            print(row)

if __name__ == "__main__":
    main(sys.argv[1:])