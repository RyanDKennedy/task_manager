"""
Ryan Kennedy, Gabriel Walder
Cmdr. Schenk
Cloud Computing
7th Period
March 18, 2025
"""

# CREATE TABLE books (
#     id integer auto_increment unique not null,
#     name text not null,
#     year_released integer,
#     page_amt integer,
#     price float,
#     author_id integer not null,
#     PRIMARY KEY (id),
#     FOREIGN KEY (author_id) REFERENCES authors(id)
# );

class BookRecord:

    def __init__(self):
        self.id = -1
        self.name = "None"
        self.year_released = 0
        self.page_amt = 0
        self.price = 0
        self.author_id = 0

    def fill(self, id, name, year_released, page_amt, price, author_id):
        self.id = id
        self.name = name
        self.year_released = year_released
        self.page_amt = page_amt
        self.price = price
        self.author_id = author_id
