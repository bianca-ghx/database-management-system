use booksdb;

insert into loan_has_book(loan_idLoan, book_idBook)
values
('2410c007-03ec-4f5f-bb52-4aeb0338a990','1'),
('2d93ec20-ef84-4074-b99a-d6d8535c999b','2'),
('331c6f82-f892-40f0-b2bd-eeb25d179c73','3'),
('3d56c12c-328e-4c7e-8230-bf6a9aeb056e','4'),
('6c8a9231-2c23-4cbd-9cc5-01a709c7bb61','5'),
('740eff8f-2776-4e86-8fe2-3d8bfc6ef061','6'),
('863748ca-842b-4e94-8574-05da5af16c74','7'),
('01bc9137-8cb4-4bca-b781-c11f8143556a','7'),
('0a0aeab2-8ef9-4b41-b616-c4107507ae5a','7'),
('32fb1c87-243c-418c-b028-2de82efb8fcf','8'),
('36c9d578-e551-4639-b043-1edc4069b2ef','9'),
('4738ee3c-ad4e-4091-b88f-f24d130f2961','9'),
('59128dcc-52c4-4049-a082-0b08fe344ba5','10'),
('6c5fa962-2932-449d-a1d6-8e7fbb0d0843','12'),
('81201fde-facd-4d8b-8189-e3cafd15b354','12'),
('b9ff3641-b292-4a67-bb3f-547da47f1374','12'),
('ba282de6-50c4-47af-99f1-f4fee3429b08','12'),
('c2707c17-0e9b-49f3-9c67-a4c3c1ff4c11','12'),

('e1b2ce7f-fb72-49b4-96eb-17d8d408f9ca','420'),
('e1b2ce7f-fb72-49b4-96eb-17d8d408f9ca','69'),
('e1b2ce7f-fb72-49b4-96eb-17d8d408f9ca','558'),
('e1b2ce7f-fb72-49b4-96eb-17d8d408f9ca','627'),
('e1b2ce7f-fb72-49b4-96eb-17d8d408f9ca','489'),

('ead6d46b-3645-4071-a8aa-e1a40623c574','351'),
('ead6d46b-3645-4071-a8aa-e1a40623c574','282');

select * from loan_has_book