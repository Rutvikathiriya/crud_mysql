# -*- coding : utf-8 -*-

import db_con
import MySQLdb as mdb
import sys
import warnings


def create_table_mysql(con):
        try:
            cur = con.cursor()
            cur.execute("CREATE TABLE student(Id INT PRIMARY KEY AUTO_INCREMENT,Firstname VARCHAR(10),City VARCHAR(20));")
        except Exception as e:
            print "Table is created"


def retrive_data_mysql(con): 
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM student")

        for i in range(cur.rowcount):
            row = cur.fetchone()
            print row["Id"], row["Firstname"], row["City"]

def insert_data_mysql(con):
        try:
            cur = con.cursor()
            Id = 0
            Firstname = raw_input("Enter Your First Name : ")
            City = raw_input("Enter Your City : ")
            cur.execute("INSERT INTO student VALUES (%s, %s, %s)",(Id, Firstname, City))
            print "Record Inserted"
        except mdb.Warning, e:
            pass

def update_data_mysql(con):
        firstname = raw_input('enter updated name:')
        id = raw_input('enter id where u can update ur name:')
        city = raw_input('enter city to update:')

        cur = con.cursor()
        cur.execute("UPDATE student SET Firstname = %s, City = %s  WHERE Id = %s",
                    (firstname, city, id))
        print "Number of rows updated:", cur.rowcount

def delete_data_mysql(con):
        id = raw_input('enter a id to delete:')
        cur = con.cursor()
        cur.execute("DELETE FROM student WHERE Id = %s" % (id))
        print "Delete a row"