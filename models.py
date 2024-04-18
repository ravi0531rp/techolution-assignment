class Book:
    """A class representing a book."""

    def __init__(self, title, author, isbn, checked_out=False):
        """
        Initializes a Book object with the provided attributes.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            checked_out (bool, optional): Indicates whether the book is checked out or not. Defaults to False.
        """
        if not title or title == "":
            print("Error: Title cannot be empty")
            return
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = checked_out

    def to_dict(self):
        """
        Converts the Book object to a dictionary.

        Returns:
            dict: A dictionary representation of the Book object.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "checked_out": self.checked_out,
        }

    def __repr__(self):
        """
        Returns a string representation of the Book object.

        Returns:
            str: A string representation of the Book object.
        """
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', checked_out={self.checked_out})"


class User:
    """A class representing a user."""

    def __init__(self, name, user_id):
        """
        Initializes a User object with the provided attributes.

        Args:
            name (str): The name of the user.
            user_id (str): The unique identifier of the user.
        """
        if not name or name == "":
            print("Error: Name cannot be empty")
            return
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        """
        Converts the User object to a dictionary.

        Returns:
            dict: A dictionary representation of the User object.
        """
        return {"name": self.name, "user_id": self.user_id}

    def __repr__(self):
        """
        Returns a string representation of the User object.

        Returns:
            str: A string representation of the User object.
        """
        return str(self.to_dict())


class Checkout:
    """A class representing a checkout record."""

    def __init__(self, user_id, isbn, checked_out=True):
        """
        Initializes a Checkout object with the provided attributes.

        Args:
            user_id (str): The ID of the user who checked out the book.
            isbn (str): The ISBN of the book that was checked out.
            checked_out (bool, optional): Indicates whether the book is checked out. Defaults to True.
        """
        self.user_id = user_id
        self.isbn = isbn
        self.checked_out = checked_out

    def to_dict(self):
        """
        Converts the Checkout object to a dictionary.

        Returns:
            dict: A dictionary representation of the Checkout object.
        """
        return {
            "user_id": self.user_id,
            "isbn": self.isbn,
            "checked_out": self.checked_out,
        }

    def __repr__(self):
        """
        Returns a string representation of the Checkout object.

        Returns:
            str: A string representation of the Checkout object.
        """
        return f"Checkout(user_id='{self.user_id}', isbn='{self.isbn}', checked_out={self.checked_out})"
