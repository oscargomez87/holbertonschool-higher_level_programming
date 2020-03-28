#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb


def main():
    """maint method of module"""

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         port=3306, host="localhost")
    qry = db.cursor()
    qry.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    rows = qry.fetchall()
    for r in rows:
        print(r)
    qry.close()
    db.close()

if __name__ == "__main__":
    main()
