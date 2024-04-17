# models.py

class Book:
    def __init__(self, title, author, isbn):
        if not title or title == "":
            print("Error: Title cannot be empty")
            return
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "checked_out": self.checked_out
        }

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', checked_out={self.checked_out})"

class User:
    def __init__(self, name, user_id):
        if not name or name == "":
            print("Error: Name cannot be empty")
            return
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id
        }

class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn
        self.checked_out = True

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "isbn": self.isbn,
            "checked_out": self.checked_out
        }