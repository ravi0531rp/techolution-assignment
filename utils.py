def main_menu():
    print("\nLibrary Management System")
    print("1. Book Management")
    print("2. User Management")
    print("3. Checkout Management")
    print("4. Exit")
    choice = input("Enter choice: ")
    return choice


def book_menu():
    print("\nBook Management")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. List Books")
    print("5. Search Books")
    print("6. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice


def user_menu():
    print("\nUser Management")
    print("1. Add User")
    print("2. Update User")
    print("3. Delete User")
    print("4. List Users")
    print("5. Search Users")
    print("6. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice


def checkout_menu():
    print("\nCheckout Management")
    print("1. Checkout Book")
    print("2. Checkin Book")
    print("3. List Checkouts")
    print("4. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice
