# -*- coding : utf-8 -*-

import sys
import db_query 

def crud_mysql(con):
    print "-----------------------"
    print "1.Create"
    print "2.Retrive"
    print "3.Insert"
    print "4.Delete"
    print "5.Update"
    print "6.Exit"
    print "-----------------------"
    user = raw_input("Enter your choice : ")

    if user == "1":
        db_query.create_table_mysql(con)
        crud_mysql(con)
    elif user == "2":
        db_query.retrive_data_mysql(con)
        crud_mysql(con)
    elif user == "3":
        db_query.insert_data_mysql(con)
        crud_mysql(con)
    elif user == "4":
        db_query.delete_data_mysql(con)
        crud_mysql(con)
    elif user == "5":
        db_query.update_data_mysql(con)
        crud_mysql(con)
    elif user == "6":
        exit()

def choice():
    con = db_query.db_con.connection_mysql()
    crud_mysql(con)


choice()