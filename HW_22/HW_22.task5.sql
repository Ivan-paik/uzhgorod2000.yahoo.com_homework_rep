SELECT age, COUNT(age) AS users
FROM users
WHERE age > 30
GROUP BY age
HAVING users > 1
ORDER BY users DESC, age;