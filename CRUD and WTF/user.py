from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/thankyou', methods = ['GET', 'POST'])
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html',first=first,last=last)


if __name__=='__main__':
    app.run(debug=True)
