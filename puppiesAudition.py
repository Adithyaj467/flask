from flask import Flask
from flask import render_template
from flask import request
app =Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup_form')
def signup_form():
    return render_template('signup_form.html')



@app.route('/thankyou', methods=['GET', 'POST'])
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html',first=first,last=last)




if __name__=="__main__":
    app.run(debug=True)
