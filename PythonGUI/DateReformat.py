# to reformat the date
import pandas as pd
from datetime import datetime

# changing the publicaton_date format in order for it to be imported intro SQL as datetime

# reading books.csv (the Goodreads database we found online) as a Pandas dataframe
bookData = pd.read_csv('books/books.csv', error_bad_lines=False)

# fetching the publication_date column as a list
pub_dates = list(bookData['publication_date'].values)

# creating new list to store the re-formatted dates
pub_dates2 = []

# re-formatting the dates
i = 0
for pub_date in pub_dates:
    try:
        date_oldformat = datetime.strptime(pub_date, '%m/%d/%Y')
        date_newformat = date_oldformat.strftime('%Y-%m-%d')
        pub_dates2.append(str(date_newformat))
        i+=1
    except:
        print(pub_date)
        print(i)

# replacing the old publication_date column with pub_dates2, which contains the re-formatted dates
bookData['publication_date'] = pub_dates2

# saving the Pandas dataframe as books2.csv
bookData.to_csv('books2.csv', index=False)


