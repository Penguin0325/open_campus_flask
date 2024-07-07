from testapp import app
from flask import render_template

@app.route('/')
def index():
    
    return 'Hello World'

events = [
    {
        'title': 'event1',
        'date': '2021-10-15'
    },
    {
        'title': 'event2',
        'date': '2024-06-20'
    }
]
@app.route('/test')
def test():
    return render_template('test.html',events=events)

@app.route('/hints')
def hints():
    return render_template('hints.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/character')
def character():
    return render_template('character.html')

@app.route('/story1')
def story1():
    return render_template('story1.html')

@app.route('/anser1')
def anser1():
    return render_template('mystery1anser.html')

@app.route('/anser2')
def anser2():
    return render_template('mystery2anser.html')

@app.route('/anser3')
def anser3():
    return render_template('mystery3anser.html')

@app.route('/middlestory')
def middlestory():
    return render_template('middlestory.html')

@app.route('/afterentering')
def afterentering():
    return render_template('afterentering.html')

@app.route('/inputchatbot1')
def inputchatbot1():
    return render_template('inputchatbot1.html')

@app.route('/inputchatbot2')
def inputchatbot2():
    return render_template('inputchatbot2.html')

@app.route('/story9')
def story9():
    return render_template('story9.html')

@app.route('/endstory1')
def endstory1():
    return render_template('endstory1.html')

@app.route('/endstory2')
def endstory2():
    return render_template('endstory2.html')

@app.route('/endstory3')
def endstory3():
    return render_template('endstory3.html')