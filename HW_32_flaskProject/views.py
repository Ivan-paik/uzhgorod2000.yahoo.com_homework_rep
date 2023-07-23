from app import app
from flask import abort, request, redirect
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
    return '''
    </br>
    <h1 style="text-align: center;"><a href="/login">Login</a></h1>
    <h1 style="text-align: center;"><a href="/users">Users</a></h1>
    <h1 style="text-align: center;"><a href="/books">Books</a></h1>
    <h1 style="text-align: center;"><a href="/params">Params</a></h1>
    '''

##  Basic task 1 was here
# @app.get('/users')
# def user_list():
#     i = randint(0, len(users)) # Total number of users to show. Zero too.
#     if i > 0:
#         users_random_list = sample(users, k=i)
#         users_render = ''.join([
#             f"{user['user_name']} "
#             for user in users_random_list
#         ])
#     else:
#         users_render = 'Bingo! Zero users to show'
#     response = f'''
#     <h2>Random users list</h2>
#     <h1> {users_render}</h1>
#     '''
#     return response, 200


@app.route('/users')
def user_list():
    filters = request.args
    if filters.get('count') == None or int(filters.get('count')) == 0:
        users_random_list = sample(users, k=randint(1, len(users))) # Random number of users to show. Minimum one)
    else:
        if int(filters.get('count')) > len(users):
            return (f'There are not so many users')
        else:
            users_random_list = sample(users, k=int(filters.get('count')))

    users_render = ''.join([
        f"{user['user_name']}</br>"
        for user in users_random_list
    ])
    response = f'''
           <h1>Random user list</h1>
           <ul>
           {users_render}
           </ul>
           '''
    return (f'{response}')


##  Basic task 1 was here
# @app.get('/books')
# def book_list():
#     books_random_list = sample(books, k=randint(1, len(books))) # Total number of books to show. Minimum one.
#     books_render = ''.join([
#         f"<li>{book['title']}</li>"
#         for book in books_random_list
#     ])
#     response = f'''
#     <h1>Random books list</h1>
#     <ul>
#     {books_render}
#     </ul>
#     '''
#     return response, 200


@app.route('/books')
def books_list():
    filters = request.args
    if filters.get('count') == None or int(filters.get('count')) == 0:
        books_random_list = sample(books, k=randint(1, len(books)))  # Total number of books to show. Minimum one)
    else:
        if int(filters.get('count')) > len(books):
            return (f'There are not so many books')
        else:
            books_random_list = sample(books, k=int(filters.get('count')))

    books_render = ''.join([
        f"<li>{book['title']}</li>"
        for book in books_random_list
    ])
    response = f'''
           <h1>Random books list</h1>
           <ul>
           {books_render}
           </ul>
           '''
    return (f'{response}')


@app.get('/users/<int:user_id>')
def user_details(user_id):
    if user_id % 2 == 0:
        response = f"{user_id}"
    else:
        abort(404, 'Not Found')
    return response, 200


@app.get('/books/<string:book_title>')
def book_details(book_title):
    response = f"{book_title.capitalize()}"
    return response, 200


@app.route('/params')
def params_detail():
    filters = request.args
    response_to_grid = ''
    for item in filters:
        response_to_grid += f'''<tr>
          <td>{item}</td>
          <td>{filters.get(item)}</td>
        </tr>'''
    response = f'''
    <table width=20%>
    <tbody>
    <td>parameter</td>
    <td>value</td>
    {response_to_grid}
    </tbody>
    </table>
    '''
    return (f'{response}')

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
            return redirect('/users')
        else:
            abort(400, 'Missed data')
    else:
        return f'''
        <form method="POST" action="/login">
            <label for="login">Login:</label>
            <input type="login" name="login" id="login"><br><br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password"><br><br>
            <input type="submit" value="submit">
        </form>
        '''


@app.errorhandler(404)
def not_found_error(error):
    return '<h1><span style="color: #ff0000;">Page not found</span></h1>', 404


@app.errorhandler(500)
def internal_server_error (error):
    return '<h1><span style="color: #ff0000;">Internal server error</span></h1>', 505
