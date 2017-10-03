# coding=utf-8
"""
@author: beyourself
@time: 2017/10/3 13:19
"""

from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/todo/api/v1.0/tasks', methods=['GET', 'POST'])
def get_tasks():
    if request.method == 'GET':
        return jsonify({'tasks': tasks})
    elif request.method == 'POST':
        if not request.json or 'title' not in request.json:
            abort(404)
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ''),
            'done': False
        }
        tasks.append(task)
        return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [t for t in tasks if t['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


