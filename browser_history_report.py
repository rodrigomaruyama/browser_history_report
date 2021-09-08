import sqlite3
import datetime
from collections import Counter, OrderedDict
import os



def connect(filename):

        # date = datetime.datetime.strftime(date, '%Y-%m-%d')
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    return conn, c

def main():

    # path = '/home/rodrigo/Documents/logs/browser/'
    # browser_names = ['firefox' ,'chrome', 'chromium']
    # for browser_name in browser_names:
    #     files = os.listdir(path + browser_name)
    #     print(files)

    files = [
                '/home/rodrigo/.config/google-chrome/Default/History',
                '/home/rodrigo/.config/google-chrome/Profile\ 1/History',
                '/home/rodrigo/.config/google-chrome/Profile\ 2/History',
                '/home/rodrigo/.config/chromium/Default/History',
                '/home/rodrigo/.mozilla/firefox/vy7eb7by.default-release-1-1629388226911/places.sqlite'
    ]

    for file in files:
        conn, c = connect(file)
        if not 'mozilla' in file:

            query = ''

        else:

            query = """ SELECT datetime(visit_date/1000000,'unixepoch') AS visit_date, url,
            title, visit_count, frecency FROM moz_places, moz_historyvisits
            WHERE moz_places.id = moz_historyvisits.place_id """

            c.execute(query)
            for row in c.fetchall():
                print(row)


if __name__ == '__main__':
    main()

# query = 'SELECT * FROM button WHERE date >= "' + date + '" ORDER BY date DESC'
# c.execute(query)
# rows = c.fetchall()
# for row in rows:
#     date = row[-1].split(' ')[0]
