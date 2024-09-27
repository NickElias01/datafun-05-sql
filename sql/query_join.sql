-- Inner join authors with books to see which author wrote which book
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;

-- Left join to get all authors, even those without books
SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON authors.author_id = books.author_id;
