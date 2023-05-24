---- 1. запит, який для кожного user порахує суму всіх покупок.
---- Результат має бути представлений у форматі:
---- users.id, users.first_name, users.last_name, total_purchases

-- SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases
--         FROM users
--         INNER JOIN purchase on users.id = purchase.user_id
--         JOIN books on purchase.book_id = books.id
--         GROUP BY users.id;


---- 2. запит, який виведе кількість покупок книжок для кожного user.
---- Результат має бути представлений у форматі: user.id, purchases_count

-- SELECT users.id, COUNT(purchase.id) AS purchases_count
--         FROM users
--         INNER JOIN purchase on users.id = purchase.user_id
--         GROUP BY users.id;


---- 3. запит, який виведе кількість покупок книжок для автора Rowling.
---- Результат має бути представлений у форматі: amount

-- SELECT count(b.id) AS amount
--         FROM purchase AS p
--         JOIN books AS b on p.user_id = b.id
--         WHERE author = "Rowling"
--         GROUP BY b.author;


---- 4. запит, який виведе загальні суми продажів для кожного автора та кількість покупок.

-- SELECT b.author, sum(b.price), count(b.id) AS amount
--         FROM purchase AS p
--         JOIN books AS b on p.user_id = b.id
--         GROUP BY b.author;


---- 5. запит, який виведе всі назви книжок із кількістю їх продажів в порядку спадання кількості продажів.

-- SELECT b.title, count(b.id) AS amount
--         FROM purchase AS p
--         JOIN books AS b on p.user_id = b.id
--         GROUP BY b.title
--         ORDER BY amount DESC;
