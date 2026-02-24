from datetime import datetime

class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        self.status = "Sent"

    def __str__(self):
        return f"[{self.timestamp}] {self.sender}: {self.content} ({self.status})"


class User:
    def __init__(self, username):
        self.username = username