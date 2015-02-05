from flask import Flask
#name when you are using just 1 file not package
#port 5000 ex. http://localhost:5000/hello2
app = Flask(__name__)
@app.route('/hello')
def hello():
    return "<h1> Hello Flask! </h1>"

#@app.route('/hello2')
@app.route('/hello2/<name>')
def hello2(name = "Flask"):
    return "<h1> Hello %s number2 </h1>" %name



if __name__ == '__main__':
    app.debug = True
    app.run()
