from flask import Flask, render_template, request, session, redirect
from random import randint

app = Flask(__name__)

# encrypts every new session dictionary
app.secret_key = "sadfuih7832hn3498f3un$nu3un4#$34rvdfv"

@app.route('/')
def index():
    return render_template('greatNG.html')

@app.route('/gametime', methods=['post'])
def gametime():
    print (session)
    session['user_pick'] = int(request.form['user_pick'])
    if 'comp_choice' not in session:
        session['comp_choice'] = randint(1, 100)
    print("Computer choice: {}".format(session['comp_choice']))
    print("User choice: {}".format(request.form['user_pick']))
    result = "testing"
    user = int(request.form['user_pick'])
    if session['comp_choice'] < user:
        session['result'] = "Too High!"
        session['r-style'] = "result-style2"

        print(session['result'])
    elif session['comp_choice'] > user:
        session['result'] = "Too Low!"
        session['r-style'] = "result-style2"

        print(session['result'])
    else:
        session['result'] = "Perfection!"
        session['r-style'] = "result-style1"

        print(session['result'])

    return redirect('/')

@app.route('/reset', methods=['post'])
def reset():
    session.pop('comp_choice')

    return redirect('/')




app.run(debug=True)