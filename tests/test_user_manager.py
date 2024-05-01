import pytest
from management.user_manager import UserManager


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

    name = "Test User"

    save_status = user_manager.add_user(name)

    assert save_status == "saved"
    assert len(user_manager.users) == 1
    assert (
        user_manager.users[0].name == name
    )  


def test_update_user(user_manager):
    """
    Test updating an existing user in UserManager.
    """
    initial_name = "Initial Name"
    new_name = "Updated Name"
    user_manager.add_user(initial_name)

    update_status = user_manager.update_user(user_manager.users[0].user_id, new_name)

    assert update_status is True
    assert user_manager.users[0].name == new_name


def test_delete_user(user_manager):
    """
    Test deleting an existing user from UserManager.
    """
    name = "Test User"
    user_manager.add_user(name)

    delete_status = user_manager.delete_user(user_manager.users[0].user_id)

    assert delete_status is True
    assert len(user_manager.users) == 0


def test_search_users(user_manager):
    """
    Test searching for users in UserManager.
    """
    user_manager.add_user("John Doe")
    user_manager.add_user("Jane Smith")

    results = user_manager.search_users(name="John Doe")

    assert len(results) == 1
    assert results[0].name == "John Doe"
