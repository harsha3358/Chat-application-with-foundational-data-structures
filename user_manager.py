from models import User

class UserManager:
    def __init__(self):
        self.users = []  # ARRAY
        self.online_users = set()  # HASHSET

    def register(self, username):
        self.users.append(User(username))
        print("User registered.")

    def login(self, username):
        for user in self.users:
            if user.username == username:
                self.online_users.add(username)
                print("Login successful.")
                return True
        print("User not found.")
        return False

    def is_online(self, username):
        return username in self.online_users