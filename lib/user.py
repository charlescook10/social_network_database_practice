class User:
    def __init__(self, id, email, username):
        self.id = id
        self.email = email
        self.username = username

    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.username})"
    
    def __eq__(self, value):
        return self.__dict__ == value.__dict__