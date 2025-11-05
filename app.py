from flask import Flask, render_template, request
app = Flask(__name__)

def mulp():
    fine=50*50
    return fine

@app.route('/')
def home():
    return '<h1> Welcome to my page,first attempt on making a web site:D o/</h1>'

@app.route('/career')
def career():
    career= ["Security","Cleaner", "Organiser", "Cashier","Pitcher","Delivery staff"]
    return render_template("career.html",career=career)
    

@app.route('/town')
def town():
    town= ["Douglasville","Statesboro", "Savannah", "Atlanta"]
    return render_template("town.html",town=town)

@app.route("/add")
def add ():
    a = 3
    b = 4
    c = 5
    total = a + b + c
    return "The sum of the numbers is: " + str(total)

@app.route("/div")
def div ():
    a = 284
    b = 4
    to = a/b
    #return "The division of the two numbers is: " + str(total)
    return render_template("division.html",total=to)

@app.route("/multiply")
def multiply():
    a = 284
    b = 4
    total = a*b
    #return "The multiplication of the two numbers is: " + str(total)
    return render_template("multiply.html",total=total)
    
@app.route("/task")
def task():
    taskavailable = request.args.get("available", "true").lower() == "true"
    if taskavailable:
        todo = ["cleaning", "gathering", "client support", "data manipulations", "cloud support", "marketing", "fumigation"]
        tar= mulp()
        return render_template("tasks.html", todo=todo,tar=tar)
    else:
        return render_template("nojob.html")
          





























































































if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)