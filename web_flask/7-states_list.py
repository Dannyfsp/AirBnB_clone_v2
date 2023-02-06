#!/usr/bin/python3
'''
A simple Flask web application
'''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
'''The Flask application instance'''
app.url_map.strict_slashes = False


@app.route('/states_list')
def display_states():
    '''Render state_list html page to display States created'''
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    '''Method to remove current SQLAlchemy Session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
