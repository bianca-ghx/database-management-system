# importing QtDesigner generated files
from MenuWindow import Ui_MenuWindow
from AddBookWindow import Ui_AddBookWindow
from DeleteBookWindow import Ui_DeleteBookWindow
from ViewAllBooksWindow import Ui_ViewAllBooksWindow
from LendBookWindow import Ui_LendBookWindow
from ReceiveWindow import Ui_ReceiveWindow

# PyQt libraries
from PyQt5 import QtGui, QtWidgets, QtCore

from qt_material import apply_stylesheet

# other libraries
import sys
import re
import uuid

# MySQL
from mysql.connector import connect, Error

def catch_exceptions(t, val, tb):
   QtWidgets.QMessageBox.critical(None,
                                  "An exception was raised",
                                  "Exception type: {}".format(t))
   old_hook(t, val, tb)

old_hook = sys.excepthook
sys.excepthook = catch_exceptions

# adding functionality to Main Menu window
class Menu(QtWidgets.QMainWindow, Ui_MenuWindow):

   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.setupUi(self)
       self.setWindowTitle("X Library")
       self.menuPage()

   def menuPage(self):
       self.pushButton1.clicked.connect(self.AddBookPage)
       self.pushButton2.clicked.connect(self.DeleteBookPage)
       self.pushButton3.clicked.connect(self.ViewAllBooksPage)
       self.pushButton4.clicked.connect(self.LendBookPage)
       self.pushButton5.clicked.connect(self.ReceiveBookPage)
       self.show()

    # when Add Book button is pressed, MenuWindow closes and AddBookWindow opens
   def AddBookPage(self):
        self.close()
        self.addBookWindow = AddBook()
        self.addBookWindow.show()

   # when Delete Book button is pressed, MenuWindow closes and DeleteBookWindow opens
   def DeleteBookPage(self):
        self.close()
        self.deleteBookWindow = DeleteBook()
        self.deleteBookWindow.show()

   # when View Book List button is pressed, MenuWindow closes and ViewAllBooksWindow opens
   def ViewAllBooksPage(self):
       self.close()
       self.viewallBooksWindow = ViewAllBooks()
       self.viewallBooksWindow.show()

   # when Lend Books button is pressed, MenuWindow closes and LendBookWindow opens
   def LendBookPage(self):
       self.close()
       self.lendBookWindow = LendBook()
       self.lendBookWindow.show()

   # when Receive Returend Books button is pressed, MenuWindow closes and ReceiveWindow opens
   def ReceiveBookPage(self):
       self.close()
       self.receiveBookWindow = ReceiveBook()
       self.receiveBookWindow.show()

# adding functionality to AddBook window
class AddBook(QtWidgets.QMainWindow, Ui_AddBookWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Add Book")


        # Set date in dateEdit as current date
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # Preview Entry button
        self.pushButton1.clicked.connect(self.pushButton1clicked)
        # Add Book button
        self.pushButton2.clicked.connect(self.pushButton2clicked)
        # Reset button
        self.pushButton3.clicked.connect(self.pushButton3clicked)
        # Back button
        self.pushButton4.clicked.connect(self.menuPage)

        self.result = 0

        # auto-generate BookID = BookID_lastbook + 1
        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                get_last_record = f"SELECT idBook FROM book ORDER BY idBook DESC LIMIT 1"
                with connection.cursor() as cursor:
                    cursor.execute(get_last_record)
                    self.result = cursor.fetchall()
                    self.result = re.sub("[^0-9]", "", str(self.result[0]))
        except Error as e:
                print(e)

        BookID = int(self.result) + 1
        # add auto-generated to BookID lineEdit
        self.lineEdit1.setText(str(BookID))

    # Preview Entry
    def pushButton1clicked(self):

        self.listWidget.clear()

        # all the lineEdits are read
        BookID = int(self.result) + 1
        Title = self.lineEdit2.text()
        Author = self.lineEdit3.text()
        NumPages = self.lineEdit4.text()
        ISBN = self.lineEdit5.text()
        ISBN13 = self.lineEdit6.text()
        LangCode = self.lineEdit7.text()
        Publisher = self.lineEdit8.text()
        PubDate = self.dateEdit.date().toPyDate()
        AvgRating = self.lineEdit9.text()
        RatingsCount = self.lineEdit10.text()
        TextReviews = self.lineEdit11.text()
        AvailableBooks = self.lineEdit12.text()

        # the content of the previously read lineEdits is added to listWidget
        self.listWidget.addItem(f"Book ID: {BookID}")
        self.listWidget.addItem(f"Title: {Title} ")
        self.listWidget.addItem(f"Author: {Author}")
        self.listWidget.addItem(f"Num. of Pages: {NumPages}")
        self.listWidget.addItem(f"ISBN: {ISBN}")
        self.listWidget.addItem(f"ISBN13: {ISBN13}")
        self.listWidget.addItem(f"Language Code: {LangCode}")
        self.listWidget.addItem(f"Publisher: {Publisher}")
        self.listWidget.addItem(f"Publication Date: {PubDate}")
        self.listWidget.addItem(f"Average Rating: {AvgRating} ")
        self.listWidget.addItem(f"Ratings Count: {RatingsCount}")
        self.listWidget.addItem(f"Text Reviews Count: {TextReviews}")
        self.listWidget.addItem(f"Available Books: {AvailableBooks}")

    # Add Book
    def pushButton2clicked(self):

        # lineEdits are read and their values are stored into local variables
        BookID = self.lineEdit1.text()
        Title = self.lineEdit2.text()
        Author = self.lineEdit3.text()
        NumPages = self.lineEdit4.text()
        ISBN = self.lineEdit5.text()
        ISBN13 = self.lineEdit6.text()
        LangCode = self.lineEdit7.text()
        Publisher = self.lineEdit8.text()
        PubDate = self.dateEdit.date().toPyDate()
        AvgRating = self.lineEdit9.text()
        RatingsCount = self.lineEdit10.text()
        TextReviews = self.lineEdit11.text()
        AvailableBooks = self.lineEdit12.text()

        # checking that the data was introduced correctly, else. show error dialog
        if BookID == '' or Title == '' or Author == '' or ISBN == '' or len(ISBN) != 10 or ISBN13 == '' or len(ISBN13) !=13 or AvailableBooks == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('All required fields must be completed (correctly)')
            msg.setWindowTitle("Error")
            msg.exec_()

        # if the user leaves a non-required field empty
        # this is seen as an empty string: ''
        # however, this cannot easily be added into MySQL
        # so it is converted to None
        if NumPages == '':
            NumPages = None
        if LangCode == '':
            LangCode = None
        if Publisher == '':
            Publisher = None
        if AvgRating == '':
            AvgRating = None
        if RatingsCount == '':
            RatingsCount = None
        if TextReviews == '':
            TextReviews = None

        # inserting book entry into MySQL table
        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                # command for inserting book entry into book table
                insert_book = f"INSERT INTO book VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                with connection.cursor() as cursor:
                    # defining the values to be inserted into MySQL, which were read from the editFields and pre-processed
                    book_values = (
                    BookID, ISBN, ISBN13, Title, Author, NumPages, LangCode, AvgRating, RatingsCount, TextReviews, Publisher,
                    PubDate, AvailableBooks)
                    cursor.execute(insert_book, book_values)
                    connection.commit()
                    # # Used for debugging, to see if book was introduced correctly
                    # select_book = "SELECT * FROM book"
                    # cursor.execute(select_book)
                    # result = cursor.fetchall()
                    # for row in result:
                    #     print(row)
        except Error as e:
            print(e)

    # Reset
    def pushButton3clicked(self):

        # clearing listWidget
        self.listWidget.clear()

        # auto-generate BookID = BookID_lastbook + 1
        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                get_last_record = f"SELECT idBook FROM book ORDER BY idBook DESC LIMIT 1"
                with connection.cursor() as cursor:
                    cursor.execute(get_last_record)
                    self.result = cursor.fetchall()
                    self.result = re.sub("[^0-9]", "", str(self.result[0]))
        except Error as e:
            print(e)

        # adding auto-generated BookID to the corresponding lineEdit
        BookID = int(self.result) + 1
        self.lineEdit1.setText(str(BookID))
        # clearing all the other lineEdits
        self.lineEdit2.clear()
        self.lineEdit3.clear()
        self.lineEdit4.clear()
        self.lineEdit5.clear()
        self.lineEdit6.clear()
        self.lineEdit7.clear()
        self.lineEdit8.clear()
        self.lineEdit9.clear()
        self.lineEdit10.clear()
        self.lineEdit11.clear()
        self.lineEdit12.clear()

    # Back
    def menuPage(self):
        self.close()
        self.menuWindow = Menu()
        self.menuWindow.show()

# adding functionality to DeleteBook window
class DeleteBook(QtWidgets.QMainWindow, Ui_DeleteBookWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Delete Book")

        # Find Book button
        self.pushButton1.clicked.connect(self.pushButton1clicked)
        # Delete Slected Book button
        self.pushButton2.clicked.connect(self.pushButton2clicked)
        # Reset button
        self.pushButton3.clicked.connect(self.pushButton3clicked)
        # Back button
        self.pushButton4.clicked.connect(self.menuPage)

        # declaring class variables
        self.selection_results = []

    # Find Book
    def pushButton1clicked(self):

        self.selection_results = []
        self.listWidget.clear()

        # lineEdits are read and their values are stored into local variables
        BookID = self.lineEdit1.text()
        Title = self.lineEdit2.text()
        ISBN = self.lineEdit3.text()
        ISBN13 = self.lineEdit4.text()
        LangCode = self.lineEdit5.text()
        Publisher = self.lineEdit6.text()

        # construct command for selecting Books
        select_book = "SELECT * FROM book WHERE "

        numChecked = 0

        if self.checkBox1.isChecked():
            select_book += f"idBook={BookID} "
            numChecked += 1

        if self.checkBox2.isChecked() and numChecked == 0:
            select_book += f"title='{Title}' "
            numChecked += 1
        elif self.checkBox2.isChecked() and numChecked > 0:
            select_book += f"and title='{Title}' "

        if self.checkBox3.isChecked() and numChecked == 0:
            select_book += f"ISBN='{ISBN}' "
            numChecked += 1
        elif self.checkBox3.isChecked() and numChecked > 0:
            select_book += f"and ISBN='{ISBN}' "

        if self.checkBox4.isChecked() and numChecked == 0:
            select_book += f"ISBN13='{ISBN13}' "
            numChecked += 1
        elif self.checkBox4.isChecked() and numChecked > 0:
            select_book += f"and ISBN13='{ISBN13}' "

        if self.checkBox5.isChecked() and numChecked == 0:
            select_book += f"language_code='{LangCode}' "
            numChecked += 1
        elif self.checkBox5.isChecked() and numChecked > 0:
            select_book += f"and language_code='{LangCode}' "

        if self.checkBox6.isChecked() and numChecked == 0:
            select_book += f"publisher='{Publisher}' "
            numChecked += 1
        elif self.checkBox6.isChecked() and numChecked > 0:
            select_book += f"and publisher='{Publisher}' "

        # check if completion was correct and if not, show error dialog
        if self.checkBox1.isChecked() == False and self.checkBox2.isChecked() == False and self.checkBox3.isChecked() == False and self.checkBox4.isChecked() == False and self.checkBox5.isChecked() == False and self.checkBox6.isChecked() == False:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('At least one check box must be selected!')
            msg.setWindowTitle("Error")
            msg.exec_()

        if self.lineEdit1.text() == '' and self.lineEdit2.text() == '' and self.lineEdit3.text() == '' and self.lineEdit4.text() == '' and self.lineEdit5.text() == '' and self.lineEdit6.text() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('At least one line edit must be completed')
            msg.setWindowTitle("Error")
            msg.exec_()

        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                with connection.cursor() as cursor:
                    # execute previously constructed command
                    cursor.execute(select_book)
                    # show results in listWidget
                    # append results to selection_results list
                    for row in cursor.fetchall():
                        row = list(row)
                        row[11] = str(row[11])
                        self.selection_results.append(row)
                        self.listWidget.addItem(f"{row}")
        except Error as e:
            print(e)

    # Delete Selected Book
    def pushButton2clicked(self):

        # find BookID for selected book, which is then used to delete the book from the database
        selected_index = [selected_index.row() for selected_index in self.listWidget.selectedIndexes()]
        selected_index= selected_index[0]
        selected_book = self.selection_results[selected_index]
        selected_book_ID = selected_book[0]

        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                # command for deleting the book
                delete_book = f"DELETE FROM book WHERE idBook = {selected_book_ID}"
                with connection.cursor() as cursor:
                    # execute command and show message that deletion was successful
                    cursor.execute(delete_book)
                    connection.commit()
                    self.listWidget.addItem("Selected Book was deleted.")
        except Error as e:
            print(e)

    # Reset
    def pushButton3clicked(self):

        # clear listWidget
        self.listWidget.clear()

        # uncheck all checkboxes
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.checkBox4.setChecked(False)
        self.checkBox5.setChecked(False)
        self.checkBox6.setChecked(False)

        # clear all linEdits
        self.lineEdit1.clear()
        self.lineEdit2.clear()
        self.lineEdit3.clear()
        self.lineEdit4.clear()
        self.lineEdit5.clear()
        self.lineEdit6.clear()

    # Back
    def menuPage(self):
        self.close()
        self.menuWindow = Menu()
        self.menuWindow.show()

# adding functionality to ViewAllBooks window
class ViewAllBooks(QtWidgets.QMainWindow, Ui_ViewAllBooksWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("View All Books")

        # Back button
        self.pushButton.clicked.connect(self.menuPage)

        # Row count
        self.tableWidget.rowCount()

        # Column count
        self.tableWidget.setColumnCount(12)

        # Add column names
        column_names = ["Book ID", "ISBN", "ISBN13", "Title", "Author", "Num. Pages", "Lang Code",  "Avg Rating", "Rate Count", "Text Rev", "Publisher", "Pub Date", "Av Books"]
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        # Create list to store all the books in the database
        all_books = []

        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                # command selecting all books from the database
                select_books= "SELECT * FROM book"
                # add all books from book table to tableWidget
                with connection.cursor() as cursor:
                    cursor.execute(select_books)
                    for row in cursor.fetchall():
                        all_books.append(list(row))
                        self.addTableRow(self.tableWidget, list(row))
        except Error as e:
            print(e)

        # resizing columns to contend in otder to see all data
        self.tableWidget.resizeColumnsToContents()

    # function which is called to add data row by row in table
    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row + 1)
        col = 0
        for item in row_data:
            cell = QtWidgets.QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

    # Back
    def menuPage(self):
            self.close()
            self.menuWindow = Menu()
            self.menuWindow.show()

# adding functionality to LendBook window
class LendBook(QtWidgets.QMainWindow, Ui_LendBookWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Lend Book")

        # set date in dateEdit1 (current_date) ad the current date
        # and date in dateEdit2 (return_date) as current date + 30 days
        self.dateEdit1.setDateTime(QtCore.QDateTime.currentDateTime())
        current_date = QtCore.QDateTime.currentDateTime()
        return_date = current_date.addDays(30)
        self.dateEdit2.setDateTime(return_date)

        # Find Book button
        self.pushButton1.clicked.connect(self.pushButton1clicked)
        # Find Client button
        self.pushButton2.clicked.connect(self.pushButton2clicked)
        # Add Client button
        self.pushButton3.clicked.connect(self.pushButton3clicked)
        # Select Book button
        self.pushButton4.clicked.connect(self.pushButton4clicked)
        # Select Another Book button
        self.pushButton5.clicked.connect(self.pushButton5clicked)
        # Delete Selected Book button
        self.pushButton6.clicked.connect(self.pushButton6clicked)
        # Generate Order button
        self.pushButton7.clicked.connect(self.pushButton7clicked)
        # Back button
        self.pushButton8.clicked.connect(self.menuPage)

        # declaring class variables
        self.selection_results = []

    # Find Book
    def pushButton1clicked(self):

        self.listWidget1.clear()

        # lineEdits are read and their values are stored into local variables
        BookID = self.lineEdit1.text()
        Title = self.lineEdit2.text()
        ISBN = self.lineEdit3.text()
        ISBN13 = self.lineEdit4.text()
        LangCode = self.lineEdit5.text()
        Publisher = self.lineEdit6.text()

        self.selection_results = []

        # construct select book command
        select_book = "SELECT * FROM book WHERE "

        numChecked = 0

        if self.checkBox1.isChecked():
            select_book += f"idBook={BookID} "
            numChecked += 1

        if self.checkBox2.isChecked() and numChecked == 0:
            select_book += f"title='{Title}' "
            numChecked += 1
        elif self.checkBox2.isChecked() and numChecked > 0:
            select_book += f"and title='{Title}' "

        if self.checkBox3.isChecked() and numChecked == 0:
            select_book += f"ISBN='{ISBN}' "
            numChecked += 1
        elif self.checkBox3.isChecked() and numChecked > 0:
            select_book += f"and ISBN='{ISBN}' "

        if self.checkBox4.isChecked() and numChecked == 0:
            select_book += f"ISBN13='{ISBN13}' "
            numChecked += 1
        elif self.checkBox4.isChecked() and numChecked > 0:
            select_book += f"and ISBN13='{ISBN13}' "

        if self.checkBox5.isChecked() and numChecked == 0:
            select_book += f"language_code='{LangCode}' "
            numChecked += 1
        elif self.checkBox5.isChecked() and numChecked > 0:
            select_book += f"and language_code='{LangCode}' "

        if self.checkBox6.isChecked() and numChecked == 0:
            select_book += f"publisher='{Publisher}' "
            numChecked += 1
        elif self.checkBox6.isChecked() and numChecked > 0:
            select_book += f"and publisher='{Publisher}' "

        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                with connection.cursor() as cursor:
                    # execute command constructed previously
                    cursor.execute(select_book)
                    # add results to listWidget and append them to selection_results
                    for row in cursor.fetchall():
                        row = list(row)
                        row[11] = str(row[11])
                        self.selection_results.append(row)
                        self.listWidget1.addItem(f"{row}")
        except Error as e:
            print(e)

    # Find Client
    def pushButton2clicked(self):

        # read introduced ClientID from lineEdit7
        ClientID = self.lineEdit7.text()

        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                # command for finding client by ID
                select_client = f"SELECT * FROM client WHERE idClient = {ClientID}"
                with connection.cursor() as cursor:
                    cursor.execute(select_client)
                    self.client_result = cursor.fetchall()
                    # if client is not in client database, show "Client not in DB." message in lineEdit8
                    if not self.client_result:
                        self.lineEdit8.setText("Client not in DB.")
                    # else fetch the client's name, phone number and email from database
                    else:
                        self.lineEdit9.setText(self.client_result[0][1])
                        self.lineEdit10.setText(self.client_result[0][2])
                        self.lineEdit11.setText(self.client_result[0][3])
        except Error as e:
            print(e)

    # Add Client
    # used only in the case where the client found by the introduced ID is not in database
    def pushButton3clicked(self):

        # read lineEdits and store their values intro variables
        ClientID = self.lineEdit7.text()
        Name = self.lineEdit9.text()
        Phone = self.lineEdit10.text()
        Email = self.lineEdit11.text()

        # add new client to database
        if not self.client_result:
            try:
                with connect(
                        host="localhost",
                        user="Biank",
                        password="Parola123",
                        database="booksdb"
                ) as connection:
                    # command for adding new client entry
                    insert_client = f"INSERT INTO client VALUES(%s, %s, %s, %s)"
                    with connection.cursor() as cursor:
                        # defining the values for the new client entry, which were read from the lineEdits
                        client_values = (ClientID, Name, Phone, Email)
                        # adding new client
                        cursor.execute(insert_client, client_values)
                        connection.commit()
                        # # used for debugging purposes, to see if the client was introduced into the database correctly
                        # select_client_query = "SELECT * FROM client"
                        # cursor.execute(select_client_query)
                        # result = cursor.fetchall()
                        # for row in result:
                        #     print(row)
            except Error as e:
                print(e)
        # if the user tries to re-enter a client that is already in the database, the error dialog is shown
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Client is already in database')
            msg.setWindowTitle("Error")
            msg.exec_()

    # Select Book
    def pushButton4clicked(self):

        # find BookID for selected book, which is then used to delete the book from the database
        selected_index = [selected_index.row() for selected_index in self.listWidget1.selectedIndexes()]
        selected_index = selected_index[0]
        selected_book = self.selection_results[selected_index]
        selected_book_ID = selected_book[0]

        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                # command used to find book by its ID
                select_book = f"SELECT * FROM book WHERE idBook = {selected_book_ID}"
                with connection.cursor() as cursor:
                    cursor.execute(select_book)
                    # find books and add them to listWidget
                    for row in cursor.fetchall():
                        row = list(row)
                        row[11] = str(row[11])
                        self.listWidget2.addItem(f"{row}")
        except Error as e:
            print(e)

    # Select Another Book
    def pushButton5clicked(self):

        # clear listWidget
        self.listWidget1.clear()

        # uncheck all check boxes
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.checkBox4.setChecked(False)
        self.checkBox5.setChecked(False)
        self.checkBox6.setChecked(False)

        # clear all lineEdits
        self.lineEdit1.clear()
        self.lineEdit2.clear()
        self.lineEdit3.clear()
        self.lineEdit4.clear()
        self.lineEdit5.clear()
        self.lineEdit6.clear()

    # Delete Selected Book
    def pushButton6clicked(self):
        selected_items = self.listWidget2.selectedItems()
        for item in selected_items:
            self.listWidget2.takeItem(self.listWidget2.row(item))

    # Generate Order
    def pushButton7clicked(self):

        # read dateEdits and editFields and store them into variables
        start_date = self.dateEdit1.date().toPyDate()
        return_date = self.dateEdit2.date().toPyDate()
        clientID = self.lineEdit7.text()
        # generate loan ID using uuid module
        loanID = str(uuid.uuid1())
        # add loan ID to lineEdit
        self.lineEdit12.setText(loanID)

        # get all items in listWidget2 (all selected books)
        itemsTextList = [str(self.listWidget2.item(i).text()) for i in range(self.listWidget2.count())]

        # adding new loan entry to loan table
        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                # command for inserting loan entry into database
                insert_loan = f"INSERT INTO loan VALUES(%s, %s, %s, %s)"
                with connection.cursor() as cursor:
                    # defining the values for the new loan entry, which were read from the lineEdits
                    loan_values = (loanID, start_date, return_date, clientID)
                    cursor.execute(insert_loan, loan_values)
                    connection.commit()
        except Error as e:
            print(e)

        # adding entry into loan_has_book table
        # decrementing available_books for the book that lend
        for item in itemsTextList:
            item = item.split(',')
            # if the number of available books is 0 the user gets an error message
            # because it means that the book is not available anymore
            if item[12] == 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText(f"{item[3]} can't be added because it's not available anymore")
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                try:
                    with connect(
                            host="localhost",
                            user="Biank",
                            password="Parola123",
                            database="booksdb"
                    ) as connection:
                        bookID = re.sub("[^0-9]", "", item[0])
                        num_avbooks = re.sub("[^0-9]", "", item[12])
                        # command for decrementing the number of available books
                        update_avbooks = f"UPDATE book SET available_books = {int(num_avbooks) - 1} WHERE idBook = {bookID}"
                        # command for inserting loanID and bookID into loan has book
                        insert_loanhasbook = f"INSERT INTO loan_has_book VALUES(%s, %s)"
                        with connection.cursor() as cursor:
                            # defining the values to be inserted into loan_had_book
                            # which were read forthe lineEdits
                            loanhasbook_values = (loanID, bookID)
                            cursor.execute(insert_loanhasbook, loanhasbook_values)
                            connection.commit()
                            cursor.execute(update_avbooks)
                            connection.commit()
                except Error as e:
                    print(e)

    # Back
    def menuPage(self):
        self.close()
        self.menuWindow = Menu()
        self.menuWindow.show()

# adding functionality to ReceiveBook window
class ReceiveBook(QtWidgets.QMainWindow, Ui_ReceiveWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Receive Returned Book")

        # Return Selected Book button
        self.pushButton1.clicked.connect(self.pushButton1clicked)
        # Back button
        self.pushButton2.clicked.connect(self.menuPage)

        self.selection_results = []

        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                # command that shows return date, client's name, client's phone no., loan ID and all books from order
                table = """select l.return_date, c.name, c.phone, l.idLoan, group_concat(lhb.book_idBook)
                from loan as l 
                LEFT JOIN client AS c
                on l.client_idClient = c.idClient
                INNER JOIN loan_has_book as lhb
                on l.idLoan = lhb.loan_idLoan
                where l.return_date > CAST(CURRENT_TIMESTAMP AS DATE)
                GROUP BY idLoan 
                ORDER BY l.return_date ASC;  """
                with connection.cursor() as cursor:
                    # execute command
                    cursor.execute(table)
                    result = cursor.fetchall()
                    # add results in listWidget and append them to selection results
                    for row in result:
                        row = list(row)
                        row[0] = str(row[0])
                        self.selection_results.append(row)
                        self.listWidget.addItem(str(row))

        except Error as e:
            print(e)

    def pushButton1clicked(self):

        # find BookID and LoanID for selected order
        selected_index = [selected_index.row() for selected_index in self.listWidget.selectedIndexes()]
        selected_index = selected_index[0]
        selected_order= self.selection_results[selected_index]
        LoanID = selected_order[3]
        BookID = selected_order[4].split(',')

        # delete loan entry for the order that is returned
        # and increment available_books for the returned books
        try:
            with connect(
                    host="localhost",
                    user="Biank",
                    password="Parola123",
                    database="booksdb"
            ) as connection:
                # command for deleting the selected order
                delete_loan = f"DELETE FROM loan WHERE idLoan = '{LoanID}'"
                with connection.cursor() as cursor:
                    cursor.execute(delete_loan)
                    connection.commit()
                    for ID in BookID:
                        # command for incrementing available_books
                        update_avbooks = f"UPDATE book SET available_books = available_books + 1 WHERE idBook = {ID}"
                        cursor.execute(update_avbooks)
                        connection.commit()
        except Error as e:
            print(e)

    # Back
    def menuPage(self):
        self.close()
        self.menuWindow = Menu()
        self.menuWindow.show()

if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   window = Menu()
   # setup stylesheet
   apply_stylesheet(app, theme='dark_lightgreen.xml')
   window.show()
   app.exec_()