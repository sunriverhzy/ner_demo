import json
import sys
import requests
import time
from flask import Flask, request, jsonify
from flask import render_template
from flask import current_app

from collections import defaultdict as ddict
from collections import Counter
from collections import OrderedDict

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    return 'Hello Conditional KGs!'

@app.route('/structuring', methods=['GET', 'POST'])
def structuring_text():
    if request.method == 'GET':
        # print(statements_graph)
        # statements = {'stmt 1': {'text': '小男孩在马路边捡到一分钱.', 'fact tuples': [['小男孩', 'NIL', '捡到', '一分钱', 'NIL']], 'condition tuples': [['NIL', 'NIL', '在', '马路边', 'NIL'], ['TNF-α', 'NIL', 'in', 'synovial fluid', 'NIL']], 'unit_indx': [[0, 8, 0, 10, 8, 13, 14, 10, 13, 14], [6, 6], [1, 2, 3, 4, 1, 2, 3, 4, 11, 11]]}}
        # return jsonify({'fact_tuples': '(小男孩, 捡到, 一分钱)', 'cond_tuples': u'(NIL, 在, 马路边)', 'statements_graph': statements_graph})
        return render_template('SciNER_example1.html')
    else:
        return 'Error! in structuring'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/about')
def about():
    return 'The about page'

# pip install flask
# export FLASK_APP=ckg.py
# flask run

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8708)
