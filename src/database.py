import random

class Database():

    def __init__(self):
        self.records = [[1, "Ryan K", 18, "Male"], [3, "Chris C", 18, "Male"], [20, "John Wick", 60, "Male"]]

    def get_all_records(self):
        return self.records

    def update(self, record):
        for i in range(0, len(self.records)):
            if (self.records[i][0] == record[0]):
                self.records[i] = record
                break

    def insert(self, record):
        self.records.append([int(random.random() * 1000), record[1], record[2], record[3]])

    def delete(self, id):
        for i in range(0, len(self.records)):
            if (self.records[i][0] == id):
                del self.records[i]
                break



