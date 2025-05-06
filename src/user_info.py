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

        # change name

        tk.Label(self.frame, text="Change Name").pack()

        tk.Label(self.frame, text="Name:").pack()
        self.name_ent = tk.Entry(self.frame)
        self.name_ent.pack()

        tk.Button(self.frame, text="Change Name", command=self.change_name).pack()

        # change credentials

        tk.Label(self.frame, text="New Username:").pack()
        self.username_ent = tk.Entry(self.frame)
        self.username_ent.pack()

        tk.Label(self.frame, text="New Password:").pack()
        self.password_ent = tk.Entry(self.frame)
        self.password_ent.pack()

        tk.Label(self.frame, text="Old Password:").pack()
        self.old_password_ent = tk.Entry(self.frame)
        self.old_password_ent.pack()

        tk.Button(self.frame, text="Change Credentials", command=self.change_credentials).pack()

    def show(self, id):
        self.clear_entries()
        self.user = self.db.users_get_record_by_id(id)
        self.name_ent.insert(0, self.user.name)
        self.username_ent.insert(0, self.user.username)
        self.frame.pack()

    def change_credentials(self):
        old_password = self.old_password_ent.get()
        hashed_old_password = bcrypt.hashpw(old_password.encode(), b'$2b$12$zm4/D56Ntli/hWPKnmLSgu').decode("utf-8")

        if (hashed_old_password != self.user.hashed_password):
            self.feedback_lbl["text"] = "Failed to change credentials. Old password is incorrect."
            return

        password = self.password_ent.get()
        hashed_password = bcrypt.hashpw(password.encode(), b'$2b$12$zm4/D56Ntli/hWPKnmLSgu').decode("utf-8")

        record = UserRecord()
        record.fill(id=self.user.id, name=self.name_ent.get(), username=self.username_ent.get(), hashed_password=hashed_password)
        self.db.users_update(record)
        self.user = self.db.users_get_record_by_id(self.user.id)
        self.update_entries()
        self.feedback_lbl["text"] = "Successfully Updated Credentials"

    def change_name(self):
        record = UserRecord()
        record.fill(id=self.user.id, name=self.name_ent.get(), username=self.user.username, hashed_password=self.user.hashed_password)
        self.db.users_update(record)
        self.feedback_lbl["text"] = "Successfully Updated Name"

        self.user = self.db.users_get_record_by_id(self.user.id)
        self.update_entries()

    def update_entries(self):
        self.clear_entries()
        self.name_ent.insert(0, self.user.name)
        self.username_ent.insert(0, self.user.username)
        

    def clear_entries(self):
        self.name_ent.delete(0, "end")
        self.username_ent.delete(0, "end")
        self.password_ent.delete(0, "end")
        self.old_password_ent.delete(0, "end")

    def logout(self):
        self.hide()
        self.show_map[GUIStates.LOGIN_USER]()

    def hide(self):
        self.frame.pack_forget()

    def assign_show_map(self, show_map):
        self.show_map = show_map
