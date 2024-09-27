-- Count the number of books in the database
SELECT COUNT(*) FROM books;

-- Find the average publication year of the books
SELECT AVG(year_published) FROM books;

-- Sum up the number of years in which books were published
SELECT SUM(year_published) FROM books;
