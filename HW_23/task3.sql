SELECT users.id, users.first_name, users.last_name, books.title
        FROM users
        JOIN purchase on users.id = purchase.user_id
        JOIN books on purchase.book_id = books.id
        ORDER BY users.id;
