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

class UserInfo:

    def __init__(self, root, db):
        self.frame = tk.Frame(root);
        self.db = db

    def init_resources(self):
        pass

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()

    def assign_show_map(self, show_map):
        self.show_map = show_map
