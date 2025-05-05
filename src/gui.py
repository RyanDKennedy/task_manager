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

class GUI():

    def __init__(self):

        # tkinter init
        self.root = tk.Tk()
        self.root.geometry("1000x1000")

        # db init
        self.db = Database()



        self.root.mainloop()



