from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    
   
    return "welcome home"

@app.route('/homepage')
def homepage():
    name="Mrs Akinfolaju"
    email="peju@yahoo.com"
    return render_template('homepage.html', name=name,email=email)


@app.route('/about')
def about():
    return "Welcome to about us page!"

@app.route("/services")
def services():
    return "Welcome to our services page!"

@app.route("/maths")
def maths ():
    a = 5
    b = 10
    c = a+b
    return render_template("maths.html", maths_result=c)

@app.route("/multiply")
def multiply ():
    a = 14
    b = 15
    c = 20
    d= a*b*c
    return render_template("multiply.html", multiply_result=d)

@app.route("/division")
def division ():
    a = 100
    b = 15
    c= a/b
    return "Hurray!, you are correct, this is the result" + str(c)

#Create another route page that would be called contact us, email address
#Create another route page that will add three numbers together 
#Create another page called task, the number are 91, 81 and 71, subtract 50 form whatever you get
#The output should be yes i got it, this is my result



@app.route("/contact")
def contact ():
    email="feyithonia@gmail.com"
    phone="080966753"
    return "Our Contact details are " + email + " , " + phone

@app.route("/add")
def add ():
    a = 3
    b = 4
    c = 5
    total = a + b + c
    return "The sum of the numbers is: " + str(total)

@app.route("/task")
def task ():
    a = 91
    b = 81
    c = 71
    total = a + b + c - 50
    return "Yes, I got it, this is my result: " + str(total)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)