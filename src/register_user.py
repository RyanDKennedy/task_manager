"""
Ryan Kennedy, Gabriel Waldner
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

class RegisterUser:

    def __init__(self, root, db):
        self.frame = tk.Frame(root)
        self.db = db

    def init_resources(self):
        style = ttk.Style()
        style.theme_use('clam')  # Try also: 'alt', 'vista', etc.

        # Title Label 
        style.configure("TitleLabel.TLabel", font=("Segoe UI", 20, "bold"))

        # Feedback Label 
        style.configure("FeedbackLabel.TLabel", font=("Segoe UI", 9, "italic"))

        # Field Labels 
        style.configure("FieldLabel.TLabel", font=("Segoe UI", 20), foreground="#444")

        # Field Entry 
        style.configure("Field.TEntry", font=("Segoe UI", 20), padding=10)

        # Action Buttons 
        style.configure("Action.TButton", font=("Segoe UI", 20), padding=10)



        ttk.Label(self.frame, text="User Registration", style="TitleLabel.TLabel").place(x=400, y=30, anchor="center")

        self.feedback_lbl = ttk.Label(self.frame, text="...", style="FeedbackLabel.TLabel")
        self.feedback_lbl.place(x=50, y=30)

        # name
        ttk.Label(self.frame, text="Name:", style="FieldLabel.TLabel").place(x=100, y=125)
        self.name_ent = ttk.Entry(self.frame, style="Field.TEntry")
        self.name_ent.place(x=100, y=175, width=600, height=50)

        # Username label 
        ttk.Label(self.frame, text="Username:", style="FieldLabel.TLabel").place(x=100, y=260)
        self.username_ent = ttk.Entry(self.frame, style="Field.TEntry")
        self.username_ent.place(x=100, y=310, width=600, height=50)  

        # Password 
        ttk.Label(self.frame, text="Password:", style="FieldLabel.TLabel").place(x=100, y=400)  
        self.password_ent = ttk.Entry(self.frame, style="Field.TEntry")
        self.password_ent.place(x=100, y=450, width=600, height=50)  

        # buttons
        ttk.Button(self.frame, text="Register", command=self.register_user, style="Action.TButton").place(x=425, y=600, width=225, height=75)
        ttk.Button(self.frame, text="Goto User Login", command=self.goto_login_user, style="Action.TButton").place(x=125, y=600, width=225, height=75)

    def register_user(self):
        record = UserRecord()
        password = self.password_ent.get()
        hashed_password = bcrypt.hashpw(password.encode(), b'$2b$12$zm4/D56Ntli/hWPKnmLSgu')
        record.fill(-1, self.name_ent.get(), self.username_ent.get(), hashed_password.decode("utf-8"))
        self.db.users_insert(record)

        self.goto_login_user()

    def goto_login_user(self):
        self.frame.place_forget()
        self.show_map[GUIStates.LOGIN_USER]()

    def clear_entries(self):
        self.name_ent.delete(0, "end")
        self.username_ent.delete(0, "end")
        self.password_ent.delete(0, "end")

    def show(self):
        self.clear_entries()
        self.frame.place(x=0,y=0,width=1000,height=1000)

    def hide(self):
        self.frame.place_forget()

    def assign_show_map(self, show_map):
        self.show_map = show_map
