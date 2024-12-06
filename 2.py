import uuid
from datetime import datetime
class Book:
    def __init__(self, title, author) -> None:
        self.id_ = str(uuid.uuid4())
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author} ID: {self.id_}"