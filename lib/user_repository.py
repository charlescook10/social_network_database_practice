from lib.user import User

class UserRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["email"], row["username"])
            users.append(item)
        return users

    # Find a single user by their id
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["email"], row["username"])

    # Create a new user
    def create(self, user):
        rows = self._connection.execute('INSERT INTO users (email, username) VALUES (%s, %s) RETURNING id;', [
                                user.email, user.username])
        user_id = rows[0]["id"]
        return user_id

    # Delete a user by their id
    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        return None

    # Update a user
    def update(self, user):
        self._connection.execute(
            'UPDATE users SET email = %s, username = %s WHERE id = %s', [user.email, user.username, user.id])
        return None
