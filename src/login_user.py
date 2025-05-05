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

class LoginUser:

    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.username_lbl = tk.Label(self.frame, text="Username:").pack()
        self.password_lbl = tk.Label(self.frame, text="Password:").pack()
        self.username_ent = tk.Entry(self.frame).pack()
        self.password_ent = tk.Entry(self.frame).pack()


    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()
