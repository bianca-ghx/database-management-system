use booksdb;

Create table book(
idBook INT AUTO_INCREMENT PRIMARY KEY, 
ISBN VARCHAR(10) NOT NULL, 
ISBN13 VARCHAR(13) NOT NULL, 
title VARCHAR(400) NOT NULL, 
author VARCHAR(800) NOT NULL, 
pages_no INT, 
language_code VARCHAR(15),
avg_rating FLOAT, 
rate_count INT, 
text_review_count INT, 
publisher VARCHAR(100), 
publication_date DATE, 
available_books TINYINT
);

Create table client(
idClient VARCHAR(20) PRIMARY KEY NOT NULL, 
name VARCHAR(100) NOT NULL, 
phone VARCHAR(20) NOT NULL, 
email VARCHAR(200)
);

Create table loan(
idLoan VARCHAR(36) PRIMARY KEY NOT NULL, 
start_date DATE NOT NULL, 
return_date DATE NOT NULL, 
client_idClient VARCHAR(20), 
CONSTRAINT client_idClient FOREIGN KEY (client_idClient) REFERENCES client(idClient) ON DELETE CASCADE ON UPDATE CASCADE
);

Create table loan_has_book(
loan_idLoan VARCHAR(36),
book_idBook INT,
PRIMARY KEY(loan_idLoan, book_idBook),
CONSTRAINT loan_idLoan FOREIGN KEY(loan_idLoan) REFERENCES loan(idLoan) ON DELETE CASCADE ON UPDATE CASCADE, 
CONSTRAINT book_idBook FOREIGN KEY(book_idBook) REFERENCES book(idBook) ON DELETE CASCADE ON UPDATE CASCADE
);

# view the tables initial_client_db
select * from book;
select * from loan;
select * from client;
select * from loan_has_book;