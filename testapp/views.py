from testapp import app
from flask import render_template

@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
    }
    return render_template('testapp/index.html', my_dict=my_dict)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/story1')
def test():
    return render_template('story1.html')

@app.route('/story2')
def test():
    return render_template('story2.html')

@app.route('/story3')
def test():
    return render_template('story3.html')

@app.route('/story4')
def test():
    return render_template('story4.html')

@app.route('/story5')
def test():
    return render_template('story5.html')

@app.route('/story6')
def test():
    return render_template('story6.html')

@app.route('/story7')
def test():
    return render_template('story7.html')

@app.route('/story8')
def test():
    return render_template('story8.html')

@app.route('/story9')
def test():
    return render_template('story9.html')