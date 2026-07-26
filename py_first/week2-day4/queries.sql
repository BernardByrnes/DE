SELECT *
FROM students;

SELECT name, course
FROM students;

SELECT *
FROM students
WHERE course = 'Python';

SELECT *
FROM students
ORDER BY grade DESC;

SELECT *
FROM students
ORDER BY grade DESC
LIMIT 3;
