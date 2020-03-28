#!/usr/bin/python3
"""Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv


def main():
    """main method of module"""

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cqry = db.cursor()
    name = argv[4]
    cqry.execute("""SELECT * FROM states WHERE BINARY name = %s""", (name,))
    rows = cqry.fetchall()
    for r in rows:
        print(r)
    cqry.close()
    db.close()

if __name__ == "__main__":
    main()
