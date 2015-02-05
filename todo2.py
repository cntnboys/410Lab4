from flask import Flask, request, url_for, redirect
import sqlite3

dbFile = 'db1.db'
conn = None

#function for giving you the connection
def get_conn():
    global conn
    if conn is None:
        conn = sqlite3.connect(dbFile)
        #return object connect
        #name and value
        conn.row_factory = sqlite3.Row
    return conn

#close connection
def close_conn():
    global conn
    if conn != None:
        conn.close()
        conn = None
    
#Query the db
def query_db(query, args=(), one=False):
    cur = get_conn().cursor()
    cur.execute(query, args)
    result = cur.fetchall()
    cur.close()
    return result

def add_task(category):
    tasks = query_db('insert into tasks(category) values(?)', [category], one=True)
    #commit to database
    get_conn().commit()

def print_tasks():
    tasks = query_db('select * from tasks')
    for task in tasks:
        print ("Task(category): %s" %task['category'])
        
    print("%d tasks in total" %len(tasks))
        

if __name__ == '__main__':
    query_db('delete from tasks')
    print_tasks()
    add_task("Cmput410")
    add_task("shopping")
    add_task("coding")
    print_tasks()
