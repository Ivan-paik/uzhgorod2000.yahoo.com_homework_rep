from app import app, db
from flask import abort, request, redirect, render_template, session, json, jsonify, url_for


from models import Users, Books, Purchases


@app.get('/')
def home():
    return render_template('home.html', title='Users random list', login_name=session.get('login_name'), )


@app.route('/users')  # output format - JSON
def user_list():
    filters = request.args
    if filters.get('size'):
        users_query = db.session.query(Users).limit(int(filters.get('size')))
    else:
        users_query = db.session.query(Users).all()

    users_list = [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'age': user.age}
                  for user in users_query]
    users_json = app.response_class(
        response=json.dumps(users_list),
        mimetype='application/json'
    )
    return users_json, 200



@app.get('/users/<int:user_id>')  # output format - JSON
def user_details(user_id):
    filters = request.values
    count_user = db.session.query(Users).filter(Users.id == user_id).count()
    if count_user == 0:
        users_json = []
        return users_json, 404
    else:
        users_query = db.session.query(Users).filter(Users.id == user_id)
        users_list = [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'age': user.age}
                      for user in users_query]
        users_json = app.response_class(
            response=json.dumps(users_list),
            mimetype='application/json'
        )
        return users_json, 200

@app.route('/users', methods=['POST'])  #add user with JSON format {"first_name": "Fill","last_name": "Zil","age": "11"}
def add_user():
    data = request.get_json()
    if 'first_name' not in data or 'last_name' not in data or 'age' not in data:
        return jsonify({'message': 'Some date is required'}), 400
    new_user = Users(first_name=data['first_name'], last_name=data['last_name'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201


@app.route('/books', methods=['GET', 'POST'])
def books_list():
    if request.method == 'POST':  # add book via HTTP POST request with "application/x-www-form-urlencoded"
        try:
            title = request.form.get('title')
            author = request.form.get('author')
            year = request.form.get('year')
            price = request.form.get('price')

            if not title or not author or not year or not price:
                return jsonify({'message': 'some field is required'}), 400

            new_book = Books(title=title, author=author, year=year, price=price)
            db.session.add(new_book)
            db.session.commit()
            return jsonify({'message': 'Book created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    else:   # GET output format - HTML
        filters = request.args
        if filters.get('size'):
            query = db.select(Books).order_by(Books.id.desc()).limit(int(filters.get('size')))
            books = db.session.execute(query).scalars()
            contex = {
                'title': 'Books list order by descending id',
                'book_list': books,
                'login_name': session.get('login_name'),
            }
        else:
            query = db.select(Books)
            books = db.session.execute(query).scalars()
            contex = {
                'title': 'Books list order by id',
                'book_list': books,
                'login_name': session.get('login_name'),
            }
        return render_template('books/books.html', **contex), 200


@app.get('/books/<int:book_id>')  # output format - HTML
def books_details(book_id):
    filters = request.values
    count_book = db.session.query(Books).filter(Books.id == book_id).count()
    if count_book == 0:
        contex = {
            'title': 'Books list',
            'count_book': count_book,
            'book_id': book_id,
            'login_name': session.get('login_name'),
        }
        return render_template('books/books_id.html', **contex), 404
    else:
        query = db.select(Books).filter(Books.id == book_id)
        books = db.session.execute(query).scalars()
        contex = {
            'title': 'Books list',
            'count_book': count_book,
            'books_list': books,
            'login_name': session.get('login_name'),
        }
        return render_template('books/books_id.html', **contex), 200


@app.route('/purchases')  # output format - HTML
def purchases():
    filters = request.args
    if filters.get('size'):
        query = db.select(Purchases.id, Purchases.book_id, Purchases.user_id, Books.title, Books.author,
            Users.first_name, Users.last_name)\
            .join(Users, Purchases.user_id == Users.id)\
            .join(Books, Purchases.book_id == Books.id)\
            .limit(int(filters.get('size')))
    else:
        query = db.select(Purchases.id, Purchases.book_id, Purchases.user_id, Books.title, Books.author,
                    Users.first_name, Users.last_name)\
                    .join(Users, Purchases.user_id == Users.id)\
                    .join(Books, Purchases.book_id == Books.id)

    purchases = db.session.execute(query)
    contex = {
        'title': 'Purchases list',
        'purchases_list': purchases,
        'login_name': session.get('login_name'),
    }
    return render_template('purchases/purchases.html', **contex), 200


@app.get('/purchases/<int:purchase_id>')  # output format - HTML
def purchase_details(purchase_id):
    filters = request.values
    count_purchases = db.session.query(Purchases).filter(Purchases.id == purchase_id).count()
    if count_purchases == 0:
        contex = {
            'title': 'Purchases list',
            'count_purchases': count_purchases,
            'purchase_id': purchase_id,
            'login_name': session.get('login_name'),
        }
        return render_template('purchases/purchases_id.html', **contex), 404
    else:
        query = db.select(Purchases.id, Purchases.book_id, Purchases.user_id, Books.title, Books.author,
            Users.first_name, Users.last_name)\
            .filter(Purchases.id == purchase_id) \
            .join(Users, Purchases.user_id == Users.id)\
            .join(Books, Purchases.book_id == Books.id)
        purchases = db.session.execute(query)

        contex = {
            'title': 'Books list',
            'count_purchases': count_purchases,
            'purchases_list': purchases,
            'login_name': session.get('login_name'),
        }
        return render_template('purchases/purchases_id.html', **contex), 200


@app.route('/purchases', methods=['POST'])  #add purchase with JSON format {"user_id": "2","book_id": "3", "date": "01.01.2023"}
def add_purchase():
    data = request.get_json()
    if 'user_id' not in data or 'book_id' not in data or 'date' not in data:
        return jsonify({'message': 'Some date is required'}), 400
    if db.session.query(Users).filter(Users.id == data['user_id']).count() == 0:
        return jsonify({'message': 'user_id is not found'}), 400
    if db.session.query(Books).filter(Books.id == data['book_id']).count() == 0:
        return jsonify({'message': 'book_id is not found'}), 400

    new_purchase = Purchases(user_id=data['user_id'], book_id=data['book_id'], date=data['date'])
    db.session.add(new_purchase)
    db.session.commit()
    return jsonify({'message': 'New purchase created successfully'}), 201


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
