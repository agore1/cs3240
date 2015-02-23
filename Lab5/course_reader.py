__author__ = 'austin'

import csv
import sqlite3


def load_course_database(db_name, csv_filename):
    conn = sqlite3.connect(db_name)
    with conn:
        curr = conn.cursor()
        with open(csv_filename, 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(tuple(row))
                sql_cmd = "insert into coursedata values(?,?,?,?,?,?,?)"
                curr.execute(sql_cmd, tuple(row))


if __name__ == '__main__':
    load_course_database('course1.db', 'seas-courses-5years.csv')