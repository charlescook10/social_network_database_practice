# Posts Model and Repository Classes Design Recipe

## 1. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: posts

# Model class
# (in lib/post.py)
class Post


# Repository class
# (in lib/post_repository.py)
class PostRepository

```

## 2. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: posts

# Model class
# (in lib/post.py)

class Post:
    def __init__(self, id, title, content, views, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.views = views
        self.user_id = user_id
```

## 3. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: posts

# Repository class
# (in lib/post_repository.py)

class PostRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, content, views, user_id FROM posts;

        # Returns an array of Post objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, title, content, views, user_id FROM posts WHERE id = $1;

        # Returns a single Post object.

        # Creates a new record
        # One argument: post(Post object)
    def create(post)
        # Executes the SQL query:
        # INSERT INTO posts (title, email, content, views, user_id) VALUES ($1, $2, $3, $4, $5);

        # Returns id of new post

        # Deletes a single record by its ID
        # One argument: the id (number)
    def delete(id)
        # Executes the SQL query:
        # DELETE FROM posts WHERE id = $1;

        # Returns None

```

## 4. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all posts

repo = PostRepository()

posts = repo.all()

len(posts) # =>  2

posts[0].id # =>  1
posts[0].title # =>  'Random'
posts[0].content # =>  'Bla bla bla'
posts[0].views # =>  '182'
posts[0].user_id # =>  '1'

posts[1].id # =>  2
posts[1].title # =>  'Test'
posts[1].content # =>  'Test Test'
posts[1].views # =>  '112'
posts[1].user_id # =>  '2'

# 2
# Get a single post

repo = PostRepository()

post = repo.find(1)

post.id # =>  1
post.title # =>  'Test'
post.content # =>  'Test Test'
post.views # =>  '112'
post.user_id # =>  '2'

# 3
# Create a new post

repo = PostRepository()

new_post = Post(None, "Test Title", "Test Content", 112, 1)

post_id = repo.create(new_post)

post = repo.find(post_id)

post.id # =>  3
posts.title # =>  'Test Title'
posts.content # =>  'Test Content'
posts.views # =>  '112'
posts.user_id # =>  '1'

# 4
# Delete a post

repo = PostRepository()

posts = repo.all()

len(posts) # =>  2

repo.delete(2)

posts = repo.all()

len(posts) # =>  1

```

Encode this example as a test.


## 5. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._