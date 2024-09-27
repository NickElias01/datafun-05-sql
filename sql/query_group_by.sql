-- Group books by author and count how many books each author has
SELECT authors.first, authors.last, COUNT(books.book_id) AS total_books
FROM authors
INNER JOIN books ON authors.author_id = books.author_id
GROUP BY authors.author_id;
