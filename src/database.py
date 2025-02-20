import mysql.connector
import random

class Database():

    def __init__(self):
        self.table_name = "test"
        self.conn = mysql.connector.connect(host = "192.168.0.100", user = "student", passwd = "jchs", database = "RyanKennedyAndGabrielWaldner")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def get_all_records(self):
        self.cursor.execute("SELECT * FROM {};".format(self.table_name));
        return self.cursor.fetchall();

    def update(self, record):
        self.cursor.execute("UPDATE {} SET name='{}', age={}, gender='{}' WHERE id={};".format(self.table_name, record[1], record[2], record[3], record[0]))

    def insert(self, record):
        self.cursor.execute("INSERT INTO {} (name, age, gender) VALUES('{}', {}, '{}');".format(self.table_name, record[1], record[2], record[3]))

    def delete(self, id):
        self.cursor.execute("DELETE FROM {} WHERE id={};".format(self.table_name, id))



