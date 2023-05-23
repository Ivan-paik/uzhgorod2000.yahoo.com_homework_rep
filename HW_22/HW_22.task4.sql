SELECT age, COUNT(age) AS users
FROM users
WHERE age > 30
GROUP BY age
ORDER BY users DESC, age;