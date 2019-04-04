import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('data.db')

c = conn.cursor()
insert = ''' UPDATE TrashTable
             SET trashLevel = 99
             WHERE trashID = 1
         '''
c.execute(insert)
conn.commit();


