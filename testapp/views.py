from testapp import app
from flask import render_template

@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
    }
    return render_template('testapp/index.html', my_dict=my_dict)

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

@app.route('/story1')
def story1():
    return render_template('story1.html')

@app.route('/anser1')
def anser1():
    return render_template('mystery1anser')

@app.route('/anser2')
def anser2():
    return render_template('mystery2anser')

@app.route('/anser3')
def anser3():
    return render_template('mystery3anser')

@app.route('/story5')
def story5():
    return render_template('story5.html')

@app.route('/story6')
def story6():
    return render_template('story6.html')

@app.route('/story7')
def story7():
    return render_template('story7.html')

@app.route('/story8')
def story8():
    return render_template('story8.html')

@app.route('/story9')
def story9():
    return render_template('story9.html')
