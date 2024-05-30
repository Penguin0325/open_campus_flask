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