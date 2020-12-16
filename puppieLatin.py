from flask import Flask
app =Flask(__name__)

@app.route('/')
def index():
    return"<h1>Hello User! Go To/puppy/name to see your name in puppy latin</h1>"



    #Dynamic Routing Happens here

@app.route("/puppy/<name>")
def puppy(name):
    name
    if(name[-1]=="y"):
        #indexing and concatination according to rules of puplatin
        name=name[:-1]+"iful"
    else:
        name=name+"y"
    return "<h1>name in puppy latin is .{}</h1>".format(name)

# # DEBUG: mode is ON

if __name__=='__main__':
    app.run(debug=True)
