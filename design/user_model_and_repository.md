# Users Model and Repository Classes Design Recipe

## 1. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: users

# Model class
# (in lib/user.py)
class User


# Repository class
# (in lib/user_repository.py)
class UserRepository

```

## 2. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: users

# Model class
# (in lib/user.py)

class User:
    def __init__(self, id, email, username):
        self.id = id
        self.email = email
        self.username = username
```

## 3. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: users

# Repository class
# (in lib/user_repository.py)

class UserRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, email, username FROM users;

        # Returns an array of User objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, email, username FROM users WHERE id = $1;

        # Returns a single User object.

        # Creates a new record
        # One argument: user(User object)
    def create(user)
        # Executes the SQL query:
        # INSERT INTO users (email, username) VALUES ($1, $2);

        # Returns None

        # Deletes a single record by its ID
        # One argument: the id (number)
    def delete(id)
        # Executes the SQL query:
        # DELETE FROM users WHERE id = $1;

        # Returns None

```

## 4. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all users

repo = UserRepository()

users = repo.all()

len(users) # =>  2

users[0].id # =>  1
users[0].email # =>  'David@email.com'
users[0].username # =>  'David12'

users[1].id # =>  2
users[1].email # =>  'Anna@email.com'
users[1].username # =>  'annaSmell'

# 2
# Get a single user

repo = UserRepository()

user = repo.find(1)

user.id # =>  1
user.email # =>  'David@email.com'
user.username # =>  'David12'

# 3
# Create a new user

repo = UserRepository()

new_user = User(3, "sid@email.com", "sidTheSloth")

repo.create(new_user)

user = repo.find(3)

user.id # =>  3
user.email # =>  'sid@email.com'
user.username # =>  'sidTheSloth'

# 4
# Delete a user

repo = UserRepository()

users = repo.all()

len(users) # =>  2

user = repo.delete(2)

users = repo.all()

len(users) # =>  1

```

Encode this example as a test.


## 5. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._