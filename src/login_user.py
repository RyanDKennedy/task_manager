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

from user_record import UserRecord
from task_record import TaskRecord
from database import Database

class LoginUser:

    def __init__(self, root, db):
        self.frame = tk.Frame(root)
        self.db = db

    def init_resources(self):
        self.username_lbl = tk.Label(self.frame, text="Username:").pack()
        self.password_lbl = tk.Label(self.frame, text="Password:").pack()
        self.username_ent = tk.Entry(self.frame).pack()
        self.password_ent = tk.Entry(self.frame).pack()
        tk.Button(self.frame, text="Register", command=self.goto_register_user).pack()

    def goto_register_user(self):
        self.hide()
        self.show_map["RegisterUser"]()

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()

    def assign_show_map(self, show_map):
        self.show_map = show_map
