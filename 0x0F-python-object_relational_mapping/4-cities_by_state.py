#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


def main():
    """main method"""

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cqry = db.cursor()
    cqry.execute("""SELECT c.id, c.name, s.name
    FROM cities AS c
    JOIN states AS s
    WHERE c.state_id = s.id
    ORDER BY c.id ASC""")
    rows = cqry.fetchall()
    for r in rows:
        print(r)
    cqry.close()
    db.close()

if __name__ == "__main__":
    main()
