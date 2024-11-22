class BookOperations:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre, publication_date):
        book = Book(title, author, genre, publication_date)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def borrow_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                if book.borrow():
                    print(f"You have borrowed '{title}'.")
                else:
                    print(f"Sorry, '{title}' is currently not available.")
                return
        print(f"Book '{title}' not found.")

    def return_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                book.return_book()
                print(f"Book '{title}' has been returned.")
                return
        print(f"Book '{title}' not found.")

    def search_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                print(f"Found: {book.get_title()}, Author: {book.get_author()}, Genre: {book.get_genre()}, Available: {'Yes' if book.is_available() else 'No'}")
                return
        print(f"Book '{title}' not found.")

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(f"{book.get_title()} by {book.get_author()} - {'Available' if book.is_available() else 'Borrowed'}")


class Book:
    def __init__(self, title, author, genre, publication_date, availability=True):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = availability

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__availability

    def borrow(self):
        if self.__availability:
            self.__availability = False
            return True
        return False

    def return_book(self):
        self.__availability = True