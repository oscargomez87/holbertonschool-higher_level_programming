#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


def main():
    """main method of module"""

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         port=3306, host="localhost")
    cqry = db.cursor()
    cqry.execute("""SELECT * FROM states
    WHERE name LIKE BINARY 'N%' ORDER BY id ASC""")
    rows = cqry.fetchall()
    for r in rows:
        print(r)
    cqry.close()
    db.close()

if __name__ == "__main__":
    main()
