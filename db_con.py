# -*- coding : utf-8 -*-

import MySQLdb as mdb

def connection_mysql():
    try:
        con = mdb.connect('localhost', 'root', 'Drc@1234', 'mydb');
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        ver = cur.fetchone()
        print "databse mydb created"
        print "mysql Database version : %s " % ver
        return con

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)