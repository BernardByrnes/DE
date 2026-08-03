SELECT *
FROM teachers;

SELECT name, subject
FROM teachers
WHERE subject = "optics";

SELECT *
FROM teachers
ORDER BY students DESC
LIMIT 3;