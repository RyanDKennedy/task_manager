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

class UserInfo:

    def __init__(self, root, db):
        self.frame = tk.Frame(root);
        self.db = db
        self.user = UserRecord() # stores the user that we are currently displaying the information of, currently blank but gets set in self.show(...)

    def init_resources(self):
        self.feedback_lbl = tk.Label(self.frame, text="")
        self.feedback_lbl.pack()

        tk.Button(self.frame, text="Logout", command=self.logout).pack()

        tk.Label(self.frame, text="Change Name").pack()

        tk.Label(self.frame, text="Name:").pack()
        self.name_ent = tk.Entry(self.frame)
        self.name_ent.pack()
        tk.Button(self.frame, text="Change Name", command=self.change_name).pack()

        tk.Label(self.frame, text="Username:").pack()
        self.username_ent = tk.Entry(self.frame)
        self.username_ent.pack()

        tk.Label(self.frame, text="Password:").pack()
        self.password_ent = tk.Entry(self.frame)
        self.password_ent.pack()

    def show(self, id):
        self.clear_entries()
        self.user = self.db.users_get_record_by_id(id)
        self.name_ent.insert(0, self.user.name)
        self.username_ent.insert(0, self.user.username)
        self.frame.pack()

    def change_name(self):
        record = UserRecord()
        record.fill(self.user.id, self.name_ent.get(), self.user.username, self.user.hashed_password)
        self.db.users_update(record)
        self.feedback_lbl["text"] = "Successfully Updated Name"

    def clear_entries(self):
        self.name_ent.delete(0, "end")
        self.username_ent.delete(0, "end")
        self.password_ent.delete(0, "end")

    def logout(self):
        self.hide()
        self.show_map[GUIStates.LOGIN_USER]()

    def hide(self):
        self.frame.pack_forget()

    def assign_show_map(self, show_map):
        self.show_map = show_map
