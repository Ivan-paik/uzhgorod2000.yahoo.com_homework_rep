from flask import Flask, request, json
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route('/')
def start_page():
    return (
        '<h1>Start page</h1>'
        '<h2><a href="./hello">Hello (html)</h1>'
        '<h2><a href="./bye">Bye (html)</h1>'
        '<h2><a href="./users">users (JSON from dict)</h2>'
        '<h2><a href="./admins">admins (JSON.dumps)</h2>'
    )

@app.route('/hello')
def hello():
    app.logger.info("GET Hello endpoint")
    return (
        '<h1>Hello, World!</h1>'
    )

@app.route('/bye')
def bye():
    app.logger.info("GET bye endpoint")
    return (
        '<h1>Good bye!</h1>'
    )

users_list = [{"name": "Hottabich", "age": 3732}, {"name": "Genie", "age": 10000}]

@app.route('/users') # dict in JSON
def users():
    app.logger.info("GET users endpoint")
    return users_list

admin_users_list = [{'user_name': 'user1', 'user_pass': '***'}, {'user_name': 'user2', 'user_pass': '???'}]

@app.route('/admins') # json.dumps
def admins():
    response = app.response_class(
        response=json.dumps(admin_users_list),
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
