from book_operations import BookOperations
from user_operations import UserOperations
from author_operations import AuthorOperations

def main():
    book_ops = BookOperations()
    user_ops = UserOperations()
    author_ops = AuthorOperations()

    while True:
        print("Welcome to the Library Management System!\n")
        try:
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            user_choice = input("Select an option: ")
        except ValueError:
            print("Please select an option (1 - 4)")

        if user_choice == '1':
            print("Book Operations")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            book_choice = input("Select an option: ")

            if book_choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                genre = input("Enter book genre: ")
                pub_date = input("Enter publication date: ")
                book_ops.add_book(title, author, genre, pub_date)

            elif book_choice == '2':
                title = input("Enter book title to borrow: ")
                book_ops.borrow_book(title)

            elif book_choice == '3':
                title = input("Enter book title to return: ")
                book_ops.return_book(title)

            elif book_choice == '4':
                title = input("Enter book title to search: ")
                book_ops.search_book(title)

            elif book_choice == '5':
                book_ops.display_all_books()

        elif user_choice == '2':
            print("\nUser Operations:\n")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            user_choice = input("Select an option: ")

            if user_choice == '1':
                user_name = input("Enter user name: ")
                library_id = input("Enter library ID: ")
                user_ops.add_user(user_name, library_id)

            elif user_choice == '2':
                library_id = input("Enter library ID to view: ")
                user_ops.view_user(library_id)

            elif user_choice == '3':
                user_ops.display_all_users()

        elif user_choice == '3':
            print("\nAuthor Operations:\n")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            author_choice = input("Select an option: ")

            if author_choice == '1':
                name = input("Enter author name: ")
                bio = input("Enter biography: ")
                author_ops.add_author(name, bio)

            elif author_choice == '2':
                name = input("Enter author name to view: ")
                author_ops.view_author(name)

            elif author_choice == '3':
                author_ops.display_all_authors()

        elif user_choice == '4':
            print("Exiting application.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()