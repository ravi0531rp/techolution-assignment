from storage import save_data, load_data
from models import User

class UserManager:
    def __init__(self, filename):
        self.filename = filename
        self.users = [User(**user_data) for user_data in load_data(filename)]
    
    def add_user(self, name):
        if not name:
            print("Error: User name cannot be empty")
            return "not saved"
        
        # Find the next available user ID
        existing_ids = [int(user.user_id) for user in self.users]
        next_id = max(existing_ids, default=0) + 1
        
        user_id = str(next_id)
        user = User(name, user_id)
        self.users.append(user)
        save_data([user.to_dict() for user in self.users], self.filename)
        return "saved"
    
    def update_user(self, user_id, new_name=None):
        for user in self.users:
            if user.user_id == user_id:
                if new_name:
                    user.name = new_name
                save_data([user.to_dict() for user in self.users], self.filename)
                return True
        return False
    
    def delete_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]
        save_data([user.to_dict() for user in self.users], self.filename)
    
    def list_users(self):
        for user in self.users:
            print(user)
    
    def search_users(self, **kwargs):
        results = []
        for user in self.users:
            match = all(getattr(user, attr, None) == value for attr, value in kwargs.items())
            if match:
                results.append(user)
        return results
