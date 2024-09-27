-- Filter books published after 1950
SELECT * FROM books WHERE year_published > 1950;

-- Filter authors whose last name starts with 'T'
SELECT * FROM authors WHERE last LIKE 'T%';
