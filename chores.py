import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from config import CHORES
import datetime

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
weekday = datetime.datetime.today().strftime("%A")

#@ask.launch
#def new_lookup():
#    welcome_msg = render_template('welcome', day=weekday)
#    return question(welcome_msg)

@ask.intent("TurnIntent", convert={'chore': str})
def whose_turn(chore):
    msg = render_template('turn', name=CHORES[chore][weekday], chore=chore) 
    return statement(msg)

@ask.intent("ListIntent")
def list_chores():
    chore_list = []
    for chore in CHORES.keys():
        chore_list.append((chore, CHORES[chore][weekday]))
    msg = render_template('list', day=weekday, chores=chore_list)
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
