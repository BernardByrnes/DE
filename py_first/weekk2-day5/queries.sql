SELECT *
FROM students;

SELECT name, course
FROM students;

SELECT *
FROM students
WHERE course = 'Python';

SELECT name, course, grade
FROM students
ORDER BY grade DESC;

SELECT name, course, grade
FROM students
ORDER BY grade DESC
LIMIT 3;
