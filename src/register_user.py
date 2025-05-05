"""
Ryan Kennedy, Gabriel Walder
Cmdr. Schenk
Cloud Computing
7th Period
May 5, 2025
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import bcrypt

from user_record import UserRecord
from task_record import TaskRecord
from database import Database

class RegisterUser:

    def __init__(self, root, db):
        self.frame = tk.Frame(root);
        self.db = db

    def init_resources(self):
        # name
        tk.Label(self.frame, text="Name:").pack()
        self.name_ent = tk.Entry(self.frame)
        self.name_ent.pack()

        # username
        tk.Label(self.frame, text="Username:").pack()
        self.username_ent = tk.Entry(self.frame)
        self.username_ent.pack()

        # password
        tk.Label(self.frame, text="Password:").pack()
        self.password_ent = tk.Entry(self.frame)
        self.password_ent.pack()

        # buttons
        tk.Button(self.frame, text="Register", command=self.register_user).pack()
        tk.Button(self.frame, text="Goto User Login", command=self.goto_login_user).pack()

    def register_user(self):
        record = UserRecord()
        password = self.password_ent.get()
        hashed_password = bcrypt.hashpw(password.encode(), b'$2b$12$zm4/D56Ntli/hWPKnmLSgu')
        record.fill(-1, self.name_ent.get(), self.username_ent.get(), str(hashed_password))
        self.db.users_insert(record)

        self.goto_login_user()

    def goto_login_user(self):
        self.frame.pack_forget()
        self.show_map["LoginUser"]()

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()

    def assign_show_map(self, show_map):
        self.show_map = show_map

