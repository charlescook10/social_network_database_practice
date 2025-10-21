from lib.user import User

"""
User constructs with an id, name and genre
"""
def test_user_constructs():
    user = User(1, "Test@user.com", "Test User")
    assert user.id == 1
    assert user.email == "Test@user.com"
    assert user.username == "Test User"

"""
We can format users to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "Test@user.com", "Test User")
    assert str(user) == "User(1, Test@user.com, Test User)"
    # Try commenting out the `__repr__` method in lib/user.py
    # And see what happens when you run this test again.

"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Test@user.com", "Test User")
    user2 = User(1, "Test@user.com", "Test User")
    assert user1 == user2
    # Try commenting out the `__eq__` method in lib/user.py
    # And see what happens when you run this test again.
