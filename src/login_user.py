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
from gui_states import GUIStates

class LoginUser:

    def __init__(self, root, db):
        self.frame = tk.Frame(root)
        self.db = db

    def init_resources(self):
        # username
        tk.Label(self.frame, text="Username:").pack()
        self.username_ent = tk.Entry(self.frame)
        self.username_ent.pack()

        # password
        tk.Label(self.frame, text="Password:").pack()
        self.password_ent = tk.Entry(self.frame)
        self.password_ent.pack()

        # buttons
        tk.Button(self.frame, text="Login", command=self.login).pack()
        tk.Button(self.frame, text="Goto User Register", command=self.goto_register_user).pack()

    def login(self):
        record = UserRecord()
        password = self.password_ent.get()
        hashed_password = bcrypt.hashpw(password.encode(), b'$2b$12$zm4/D56Ntli/hWPKnmLSgu')
        record.fill(-1, "", self.username_ent.get(), hashed_password.decode("utf-8"))

        users = self.db.users_get_all_records()

        user_id = -1

        for user in users:
            if (user.username == record.username and user.hashed_password == record.hashed_password):
                user_id = user.id
                break

        if (user_id == -1):
            print("invalid credentials")
            return

        print("valid crendentials")

    def goto_register_user(self):
        self.hide()
        self.show_map[GUIStates.REGISTER_USER]()

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()

    def assign_show_map(self, show_map):
        self.show_map = show_map
