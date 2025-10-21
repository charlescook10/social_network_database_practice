from lib.post import Post

class PostRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all posts
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])
            posts.append(item)
        return posts

    # Find a single post by the id
    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])

    # Create a new post
    def create(self, post):
        rows = self._connection.execute('INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s) RETURNING id;', [
                                post.title, post.content, post.views, post.user_id])
        post_id = rows[0]["id"]
        return post_id

    # Delete a post by their id
    def delete(self, post_id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [post_id])
        return None
