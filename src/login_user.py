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

class LoginUser:

    def __init__(self, root, db):
        self.frame = tk.Frame(root)
        self.db = db

    def init_resources(self):
        style = ttk.Style()
        style.theme_use('clam')  # Try also: 'alt', 'vista', etc.

        # Title Label 
        style.configure("TitleLabel.TLabel", font=("Segoe UI", 20, "bold"))

        # Field Labels 
        style.configure("FieldLabel.TLabel", font=("Segoe UI", 20), foreground="#444")

        # Field Entry 
        style.configure("Field.TEntry", font=("Segoe UI", 20), padding=10)

        # Action Buttons 
        style.configure("Action.TButton", font=("Segoe UI", 20), padding=10)



        ttk.Label(self.frame, text="User Login", style="TitleLabel.TLabel").place(x=400, y=30, anchor="center")

        # Username label 
        ttk.Label(self.frame, text="Username:", style="FieldLabel.TLabel").place(x=100, y=150)
        self.username_ent = ttk.Entry(self.frame, style="Field.TEntry")
        self.username_ent.place(x=100, y=200, width=600, height=50)  

        # Password 
        ttk.Label(self.frame, text="Password:", style="FieldLabel.TLabel").place(x=100, y=375)  
        self.password_ent = ttk.Entry(self.frame, style="Field.TEntry")
        self.password_ent.place(x=100, y=425, width=600, height=50)  

        #Buttonss
        ttk.Button(self.frame, text="Login", command=self.login).place(x=425, y=600, width=225, height=75)
        ttk.Button(self.frame, text="Register", command=self.goto_register_user).place(x=125, y=600, width=225, height=75)

    def login(self):
        record = UserRecord()
        password = self.password_ent.get()
        hashed_password = bcrypt.hashpw(password.encode(), b'$2b$12$zm4/D56Ntli/hWPKnmLSgu')
        record.fill(-1, "", self.username_ent.get(), hashed_password.decode("utf-8"))

        matched_users = self.db.users_get_records_with_username_and_hashed_password(record.username, record.hashed_password)

        if (len(matched_users) == 0):
            tk.messagebox.showerror("Failed to Login", "Invalid Login Credentials");
            return

        self.hide()
        self.show_map[GUIStates.USER_INFO](matched_users[0].id)

    def goto_register_user(self):
        self.hide()
        self.show_map[GUIStates.REGISTER_USER]()

    def clear_entries(self):
        self.username_ent.delete(0, "end")
        self.password_ent.delete(0, "end")

    def show(self):
        self.clear_entries()
        self.frame.place(x=0,y=0,width=1000,height=1000)

    def hide(self):
        self.frame.place_forget()

    def assign_show_map(self, show_map):
        self.show_map = show_map
