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
from gui_states import GUIStates

class TaskBrowser:

    def __init__(self, root, db):
        self.frame = tk.Frame(root);
        self.db = db

    def init_resources(self):
        tk.Label(self.frame, text="Task Browser").pack()

        self.feedback_lbl = tk.Label(self.frame, text="")
        self.feedback_lbl.pack()

        tk.Button(self.frame, text="Goto User Info", command=self.goto_user_info).pack()
        tk.Button(self.frame, text="Logout", command=self.logout).pack()

    def show(self, id):
        self.user = self.db.users_get_record_by_id(id)
        self.frame.pack()

    def logout(self):
        self.goto_login()

    def goto_login(self):
        self.hide()
        self.show_map[GUIStates.LOGIN_USER]()

    def goto_user_info(self):
        self.hide()
        self.show_map[GUIStates.USER_INFO](self.user.id)

    def hide(self):
        self.frame.pack_forget()

    def assign_show_map(self, show_map):
        self.show_map = show_map
