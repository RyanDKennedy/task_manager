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
        self.register_user = RegisterUser(self.root, self.db)

        # where you can login to the user
        self.login_user = LoginUser(self.root, self.db)

        # where you can update/delete your user
        self.user_info = UserInfo(self.root, self.db)

        # where you can view/CRUD on the logged in user's tasks
        self.task_browser = TaskBrowser(self.root, self.db)

        # a map that stores the functions to show the different states so that a button in one state can change to another state
        show_map = {
            "RegisterUser" : self.register_user.show,
            "LoginUser" : self.login_user.show,
            "UserInfo" : self.user_info.show,
            "TaskBrowser" : self.task_browser.show
        }
        self.register_user.assign_show_map(show_map)
        self.login_user.assign_show_map(show_map)
        self.user_info.assign_show_map(show_map)
        self.task_browser.assign_show_map(show_map)

        # this is the actual init because now inside the states the self.show_map is valid
        self.register_user.init_resources()
        self.login_user.init_resources()
        self.user_info.init_resources()
        self.task_browser.init_resources()


    def run(self):
        self.login_user.show()
        self.root.mainloop()



