from flask import Flask
app =Flask(__name__)

@app.route('/')
def index():
    return"<h1>Hello puppy</h1>"

@app.route("/information")
def info():
    return"<h1>puppies are cute</h1>"

    #Dynamic Routing Happens here 

@app.route("/puppy/<name>")
def puppy(name):
    return "<h1>2nd letter is .{}</h1>".format(name[100])

if __name__=='__main__':
    app.run(debug=True)
