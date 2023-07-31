from app import app
from flask import abort, request, redirect, render_template, session, url_for
from random import randint, sample


users = [
    {
        'user_id': 1,
        'user_name': 'Bill',
    },
    {
        'user_id': 2,
        'user_name': 'Will',
    },
    {
        'user_id': 3,
        'user_name': 'John',
    },
    {
        'user_id': 4,
        'user_name': 'Shrek',
    },
    {
        'user_id': 5,
        'user_name': 'Tom',
    },
    {
        'user_id': 6,
        'user_name': 'Jim',
    }
]


books = [
    {
        'book_id': 1,
        'title': 'Kobzar',
    },
    {
        'book_id': 2,
        'title': 'Eneida',
    },
    {
        'book_id': 3,
        'title': 'Zahar Berkut',
    },
    {
        'book_id': 4,
        'title': 'Lisova pisnya',
    },
    {
        'book_id': 5,
        'title': 'Zavoyuvannya mizhplanetnih prostoriv',
    },
    {
        'book_id': 6,
        'title': 'Zhmenyaky',
    }
]


@app.get('/')
def home():
    return render_template('home.html', title='Users random list')


@app.route('/users')
def user_list():
    filters = request.args
    if filters.get('count') == None or int(filters.get('count')) == 0:  # count not specified
        users_random_list = sample(users, k=randint(1, len(users)))  # Random number of users to show. Minimum one)
    elif int(filters.get('count')) > len(users):
        users_random_list = [
        {
            'user_name': 'There are not so many users'  # User name as message to showing
        }]
    else:
            users_random_list = sample(users, k=int(filters.get('count')))  # counter below users number

    return render_template('users/users.html', title='Users random list', users_list=users_random_list, login_name=session.get('login_name')), 200


@app.route('/books')
def books_list():
    filters = request.args
    if filters.get('count') == None or int(filters.get('count')) == 0:  # count not specified
        books_random_list = sample(books, k=randint(1, len(books)))  # Random number of books to show. Minimum one.
    elif int(filters.get('count')) > len(books):  # There are not so many books
        books_random_list = [
        {
            'title': 'There are not so many books'  # Book title as message to showing
        }]
    else:
        books_random_list = sample(books, k=int(filters.get('count')))  # counter below books number

    contex = {
        'title': 'Books random list',  # HTML page title
        'books_random_list': books_random_list,
        'login_name': session.get('login_name'),
    }
    return render_template('books/books.html', **contex), 200


@app.get('/users/<int:user_id>')
def user_details(user_id):
    if user_id % 2 == 0:
        contex = {
            'title': 'User_id',
            'user_id': user_id,
            'login_name': session.get('login_name'),
        }
        return render_template('users/users_id.html', **contex), 200
    else:
        return render_template('users/users_id.html', title='User not found', user_id='Not found', login_name=session.get('login_name')), 404


@app.get('/books/<string:book_title>')
def book_details(book_title):
    return render_template('books/books_title.html', book_title=book_title, login_name=session.get('login_name')), 200


@app.route('/params')
def params_detail():
    return render_template('params/params.html', params_list=request.args, login_name=session.get('login_name')), 200


def rules_for_password(checked_password):
    capitalize = False
    digit = False
    for symbol in checked_password:
        if symbol.isnumeric():
            capitalize = True
        if symbol.isupper():
            digit = True
        print(symbol,capitalize,digit)
    return(capitalize * digit)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_name = request.form['login']
        password = request.form['password']
        if len(login_name) >= 5 and len(password) >= 8 and rules_for_password(password):
            session['login_name'] = login_name
            return redirect('/users')
        else:
            # return render_template('login/login.html'), 400
            abort(400, 'Missed data')  ## or new temolate ??
    else:
        return render_template('login/login.html'), 200


@app.route('/logout', methods=['POST'])
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return render_template('login/login.html'), 200


@app.errorhandler(404)
def not_found_error(error):
    return '<h1><span style="color: #ff0000;">Page not found</span></h1>', 404


@app.errorhandler(500)
def internal_server_error (error):
    return '<h1><span style="color: #ff0000;">Internal server error</span></h1>', 505
