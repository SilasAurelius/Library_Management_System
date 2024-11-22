class AuthorOperations:
    def __init__(self):
        self.authors = []

    def add_author(self, name, biography):
        author = Author(name, biography)
        self.authors.append(author)
        print(f"Author '{name}' added successfully!")

    def view_author(self, name):
        for author in self.authors:
            if author.get_name() == name:
                print(f"Author: {author.get_name()}, Biography: {author.get_biography()}")
                return
        print(f"Author '{name}' not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors available.")
        for author in self.authors:
            print(f"Author: {author.get_name()}")

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography