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

from register_user import RegisterUser
from login_user import LoginUser
from user_info import UserInfo
from task_browser import TaskBrowser

class GUI():

    def __init__(self):

        # tkinter init
        self.root = tk.Tk()
        self.root.geometry("1000x1000")

        # db init
        self.db = Database()

        # where you can create a new user
        self.register_user = RegisterUser(self.root)

        # where you can login to the user
        self.login_user = LoginUser(self.root)

        # where you can update/delete your user
        self.user_info = UserInfo(self.root)

        # where you can view/CRUD on the logged in user's tasks
        self.task_browser = TaskBrowser(self.root)


    def run(self):
        self.login_user.show()
        self.root.mainloop()



