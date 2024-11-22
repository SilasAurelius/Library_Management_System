class UserOperations:
    def __init__(self):
        self.users = []

    def add_user(self, user_name, library_id):
        user = User(user_name, library_id)
        self.users.append(user)
        print(f"User '{user_name}' added successfully!")

    def view_user(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                print(f"User: {user.get_user_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {', '.join(user.get_borrowed_books()) or 'None'}")
                return
        print(f"User with ID '{library_id}' not found.")

    def display_all_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(f"User: {user.get_user_name()}, Library ID: {user.get_library_id()}")


class User:
    def __init__(self, user_name, library_id):
        self.__user_name = user_name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_user_name(self):
        return self.__user_name

    def get_library_id(self):
        return self.__library_id

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def get_borrowed_books(self):
        return self.__borrowed_books