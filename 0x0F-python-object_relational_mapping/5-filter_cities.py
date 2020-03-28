#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


def main():
    """main method"""

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    s_name = argv[4]
    cqry = db.cursor()
    cqry.execute("""SELECT c.name
    FROM states AS s
    INNER JOIN cities AS c
    WHERE BINARY s.name = %s AND s.id = c.state_id""", (s_name,))
    res = ''
    rows = cqry.fetchall()
    r_len = len(rows) - 1
    for idx, row in enumerate(rows):
        if idx < r_len:
            res = res + ''.join(row) + ', '
        else:
            res = res + ''.join(row)
    print(res)
    cqry.close()
    db.close()

if __name__ == "__main__":
    main()
