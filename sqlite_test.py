import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
# Setting up an SQLite database is nearly instant, there is no server to set up, no users to define, and no permissions to concern yourself with
#
# advantage:
#     edits do not require the entire file to be re-saved, it's just that part of the file.
#      A flat file will require a full load before you can start querying the full dataset, SQLite files don't work that way.
#
# disadvantage:
#     high volume input/output, especially with simultaneous queries, can be problematic and slow.
# < Note: SQLite is not blind to casing, but MySQL is. Python and most programming languages are not blind to casing >


# establish a connection and cursor. This is true with both SQLite and MySQL
conn = sqlite3.connect('test.db') # create one if not exist
c = conn.cursor()


# create table in db by cursor
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS basic(timeint INTEGER, datestamp TEXT, keyword TEXT, value REAL)")
    # DTYPE:
    # TEXT | NUMERIC | INTEGER | REAL | BLOB


# add entry to table
def add_data_to_basic(timeint, datestamp, keyword, value):
    # c.execute("INSERT INTO basic VALUES(145249219,'2016-01-11 13:53:39','Python',6)")
    c.execute("INSERT INTO basic (timeint, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (timeint, datestamp, keyword, value))


# read table
def read_basic(valuerange = None):
    if not valuerange:
        for row in c.execute("SELECT * FROM basic LIMIT 1"):
            print(row)
    else:
        lower = valuerange[0]
        upper = valuerange[1]
        c.execute("SELECT datestamp, keyword, value FROM basic WHERE {} < value < {}".format(lower,upper))
        data = c.fetchall() #c.fetchone()
        for row in data:
            print(row)


# plot table
def plot_basic():
    dates = []
    values = []
    for row in c.execute("SELECT datestamp, value FROM basic"):
        dates.append(row[0])
        values.append(row[1])

    plt.plot_date(dates,values,'-o')
    plt.show()


# del and update table
def del_and_update():
    # update
    c.execute('UPDATE basic SET keyword = "something" WHERE LENGTH(keyword) > 3')
    conn.commit()
    # delete
    c.execute('DELETE FROM basic WHERE value IN ( SELECT value FROM basic WHERE value > 0 LIMIT 1)')
    conn.commit()


if __name__ == "__main__":
    create_table()

    timeint = int(time.time())
    date = str(datetime.datetime.fromtimestamp(timeint).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Lenny'
    value = random.random()*10

    add_data_to_basic(timeint, date, keyword, value)
    conn.commit() # save change (do not need to commit after every INSERT)
    read_basic()

    del_and_update()
    read_basic([0,4])
    plot_basic()

    c.close() # close cursor
    conn.close() # close connection
