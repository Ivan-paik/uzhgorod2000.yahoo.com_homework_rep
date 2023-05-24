SELECT purchase.id, purchase.date, users.first_name, users.last_name
        FROM users
        JOIN purchase on users.id = purchase.user_id;
