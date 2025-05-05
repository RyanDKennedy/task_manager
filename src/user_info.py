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

class UserInfo:

    def __init__(self, root):
        self.frame = tk.Frame(root);

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()
