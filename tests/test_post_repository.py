from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new PostRepository

    posts = repository.all() # Get all posts

    # Assert on the results
    assert posts == [
        Post(1, 'Reflection Day 1', 'Today I made a database', 192, 1),
        Post(2, 'Reflection Day 2', 'Today I made a table', 32, 1),
        Post(3, 'Hot Dog Stand Review 1', 'Very nice', 1283, 2),
        Post(4, 'Confession', 'I no longer enjoy hot dogs', 9992, 2),
        Post(5, 'Leaving', 'I am leaving the internet', 1232, 2)
    ]

"""
When we call PostRepository#find
We get a single Post object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(2)
    assert post == Post(2, 'Reflection Day 2', 'Today I made a table', 32, 1)

"""
When we call PostRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post_id = repository.create(Post(None, "New Post", "Hello World", 323, 1))

    post = repository.find(post_id)
    assert post == Post(6, "New Post", "Hello World", 323, 1)

"""
When we call PostRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(5)

    result = repository.all()
    assert result == [
        Post(1, 'Reflection Day 1', 'Today I made a database', 192, 1),
        Post(2, 'Reflection Day 2', 'Today I made a table', 32, 1),
        Post(3, 'Hot Dog Stand Review 1', 'Very nice', 1283, 2),
        Post(4, 'Confession', 'I no longer enjoy hot dogs', 9992, 2)
    ]
