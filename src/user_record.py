"""
Ryan Kennedy, Gabriel Walder
Cmdr. Schenk
Cloud Computing
7th Period
May 5, 2025
"""


# CREATE TABLE users (
#        id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
#        name TEXT NOT NULL,
#        username TEXT NOT NULL,
#        hashed_password TEXT NOT NULL,
# );

class UserRecord:

    def __init__(self):
        self.id = -1
        self.name = "blank"
        self.username = "blank"
        self.hashed_password = "blank"

    def fill(self, id, name, username, hashed_password):
        self.id = id
        self.name = name
        self.username = username
        self.hashed_password = hashed_password
