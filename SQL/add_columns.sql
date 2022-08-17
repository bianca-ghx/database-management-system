INSERT INTO `book`(ISBN, ISBN13, title, author,  pages_no, language_code, avg_rating, rate_count, text_review_count, publisher, publication_date, available_books) 
SELECT ISBN, ISBN13, title, authors, num_pages, language_code, average_rating, ratings_count, text_reviews, publisher, publication_date, available_books
FROM `initial_db`;

INSERT INTO `client`(idClient, name, phone, email)
SELECT idClient, name, phone, email
FROM `initial_client_db`;




