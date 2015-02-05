from flask import Flask, request, url_for, redirect
import sqlite3
app= Flask(__name__)
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

@app.teardown_appcontext
#close connection
def close_conn(exeption):
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

def add_task(category,priority,description):
    tasks = query_db('insert into tasks(category,priority,description) values(?,?,?)', [category,priority,description])
    #commit to database
    get_conn().commit()
    
    
    
    
@app.route('/')
def welcome():
    return "<h1> Welcome to the Flask Lab! </h1>"
    
@app.route('/task', methods = ['GET', 'POST'])
def task():
        
    #Post
    if request.method == 'POST':
        #do something
        category = request.form['category']
        priority = request.form['priority']
        description = request.form['description']
        add_task(category,priority,description)
            
        #return redirect('/task1')
        return redirect(url_for('task'))
            
    #GET
    if request.method == 'GET':
        resp = '''
        <form action ="" method = post>
        <div> Category: <input type=text name=category </input> </div> </br>
        <div> Priority: <input type=text name=priority </input> </div> </br> 
        <div> Description: <input type=text name=description </input> </div> </br>
        <div> <input type = "submit" value= Add </input> </div>
            
        </form>
        
        '''
            
        #show table
        resp = resp + '''
        <table border="1" cellpadding="3">
        <tbody>
        
        <tr>
        <th> Category </th>
        <th> Priority </th>
        <th> Description </th>
        </tr>
                
    
        '''
                
        for task in query_db('select * from tasks'):
            resp = resp + "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(task['category'],task['priority'],task['description'])
            
        resp = resp + "</body></table>"
            
        return resp
    
        

if __name__ == '__main__':
    app.debug = True
    app.run()
