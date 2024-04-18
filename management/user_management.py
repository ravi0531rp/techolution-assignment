from models import User
from storage import load_data, save_data

class UserManager:
    """A class to manage users."""

    def __init__(self, filename):
        """
        Initializes the UserManager with the specified filename.

        Args:
            filename (str): The name of the file to load and save user data.
        """
        self.filename = filename
        # Loading user data from the specified file and creating User objects
        self.users = [User(**user_data) for user_data in load_data(filename)]

    def add_user(self, name):
        """
        Adds a new user to the system.

        Args:
            name (str): The name of the user to be added.

        Returns:
            str: A string indicating whether the user was saved or not.
        """
        if not name:
            print("Error: User name cannot be empty")
            return "not saved"

        # Find the next available user ID
        existing_ids = [int(user.user_id) for user in self.users]
        next_id = max(existing_ids, default=0) + 1

        user_id = str(next_id)
        user = User(name, user_id)
        self.users.append(user)
        # Saving the updated user data to the file
        save_data([user.to_dict() for user in self.users], self.filename)
        return "saved"

    def update_user(self, user_id, new_name=None):
        """
        Updates the name of an existing user.

        Args:
            user_id (str): The ID of the user to be updated.
            new_name (str): The new name of the user.

        Returns:
            bool: True if the user is successfully updated, False otherwise.
        """
        for user in self.users:
            if user.user_id == user_id:
                if new_name:
                    user.name = new_name
                # Saving the updated user data to the file
                save_data([user.to_dict() for user in self.users], self.filename)
                return True
        return False

    def delete_user(self, user_id):
        """
        Deletes a user from the system.

        Args:
            user_id (str): The ID of the user to be deleted.
        """
        self.users = [user for user in self.users if user.user_id != user_id]
        # Saving the updated user data to the file
        save_data([user.to_dict() for user in self.users], self.filename)

    def list_users(self):
        """Lists all the users."""
        for user in self.users:
            print(user)

    def search_users(self, **kwargs):
        """
        Searches for users based on specified criteria.

        Args:
            **kwargs: Arbitrary keyword arguments representing search criteria.

        Returns:
            list: A list of users that match the search criteria.
        """
        results = []
        for user in self.users:
            match = all(
                getattr(user, attr, None) == value for attr, value in kwargs.items()
            )
            if match:
                results.append(user)
        return results
