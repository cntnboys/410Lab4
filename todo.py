from flask import Flask, request, url_for, redirect, sqlite3
#name when you are using just 1 file not package
#port 5000 ex. http://localhost:5000/hello2
app = Flask(__name__)
tasks = []
@app.route('/')
def welcome():
    return "<h1> Welcome to the Flask Lab! </h1>"

@app.route('/task1', methods = ['GET', 'POST'])
def task():
    
    #Post
    if request.method == 'POST':
        #do something
        category = request.form['category']
        tasks.append({'category':category})
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
            </tr>
            
            </tbody>
            
        '''
            
        for task in tasks:
            resp = resp + "<tr><td>%s</td></tr>" %(task['category'])
            
        return resp
        
    

if __name__ == '__main__':
    app.debug = True
    app.run()
