import pytest
from management.user_management import UserManager


@pytest.fixture
def user_manager(tmp_path):
    """
    Pytest fixture to create a UserManager instance with a temporary JSON file.
    """
    # Setup: Create a temporary directory and JSON file
    tmp_dir = tmp_path / "data"
    tmp_dir.mkdir()
    filename = tmp_dir / "test_users.json"

    # Create a UserManager instance
    manager = UserManager(str(filename))

    yield manager  # Provide the UserManager instance to the test function

    # Teardown: Delete the temporary JSON file
    filename.unlink()


def test_add_user(user_manager):
    """
    Test adding a new user to UserManager.
    """
    # Arrange
    name = "Test User"

    # Act
    save_status = user_manager.add_user(name)

    # Assert
    assert save_status == "saved"
    assert len(user_manager.users) == 1
    assert (
        user_manager.users[0].name == name
    )  # Assuming UserManager maintains a list of User objects


def test_update_user(user_manager):
    """
    Test updating an existing user in UserManager.
    """
    # Arrange
    initial_name = "Initial Name"
    new_name = "Updated Name"
    user_manager.add_user(initial_name)

    # Act
    update_status = user_manager.update_user(user_manager.users[0].user_id, new_name)

    # Assert
    assert update_status is True
    assert user_manager.users[0].name == new_name


def test_delete_user(user_manager):
    """
    Test deleting an existing user from UserManager.
    """
    # Arrange
    name = "Test User"
    user_manager.add_user(name)

    # Act
    delete_status = user_manager.delete_user(user_manager.users[0].user_id)

    # Assert
    assert delete_status is True
    assert len(user_manager.users) == 0


def test_search_users(user_manager):
    """
    Test searching for users in UserManager.
    """
    # Arrange
    user_manager.add_user("John Doe")
    user_manager.add_user("Jane Smith")

    # Act
    results = user_manager.search_users(name="John Doe")

    # Assert
    assert len(results) == 1
    assert results[0].name == "John Doe"
