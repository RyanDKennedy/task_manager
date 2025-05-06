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
        self.user = UserRecord()
        self.tasks = []
        self.selected_task = 0 # index into self.tasks

    def init_resources(self):
        tk.Label(self.frame, text="Task Browser").pack()

        self.feedback_lbl = tk.Label(self.frame, text="")
        self.feedback_lbl.pack()

        # gui state change buttons

        tk.Button(self.frame, text="Goto User Info", command=self.goto_user_info).pack()
        tk.Button(self.frame, text="Logout", command=self.logout).pack()

        # entries and their respective labels

        self.task_num_lbl = tk.Label(self.frame)
        self.task_num_lbl.pack()

        tk.Label(self.frame, text="Short Name:").pack()
        self.short_name_ent = tk.Entry(self.frame)
        self.short_name_ent.pack()

        tk.Label(self.frame, text="Description:").pack()
        self.description_ent = tk.Entry(self.frame)
        self.description_ent.pack()

        # CRUD buttons
        tk.Button(self.frame, text="New", command=self.add_record).pack()
        tk.Button(self.frame, text="Update", command=self.update_record).pack()
        tk.Button(self.frame, text="Delete", command=self.delete_record).pack()

        # nav buttons
        tk.Button(self.frame, text="<", command=lambda:self.increment_selected_task(-1)).pack()
        tk.Button(self.frame, text="<<", command=lambda:self.increment_selected_task(-3)).pack()
        tk.Button(self.frame, text="|<", command=lambda:self.increment_selected_task(-1 * self.selected_task)).pack()
        tk.Button(self.frame, text=">", command=lambda:self.increment_selected_task(1)).pack()
        tk.Button(self.frame, text=">>", command=lambda:self.increment_selected_task(3)).pack()
        tk.Button(self.frame, text=">|", command=lambda:self.increment_selected_task(len(self.tasks) - 1 - self.selected_task)).pack()

    def show(self, id):
        self.user = self.db.users_get_record_by_id(id)
        self.selected_task = 0
        self.refresh()

        self.frame.pack()

    def add_record(self):
        task = TaskRecord()
        task.fill(id=-1, user_id=self.user.id, short_name=self.short_name_ent.get(), description=self.description_ent.get())
        self.db.tasks_insert(task)
        self.refresh()

    def update_record(self):
        if (self.selected_task == -1):
            self.feedback_lbl["text"] = "Can't update nonexistent record"
            return

        task = self.tasks[self.selected_task]
        task.short_name = self.short_name_ent.get()
        task.description = self.description_ent.get()
        self.db.tasks_update(task)
        self.refresh()

    def delete_record(self):
        if (self.selected_task == -1):
            self.feedback_lbl["text"] = "Can't delete nonexistent record"
            return

        self.db.tasks_delete(self.tasks[self.selected_task].id)

        self.refresh()

    def refresh(self):
        self.tasks = self.db.tasks_get_all_records_with_user_id(self.user.id)

        self.increment_selected_task(0) # bounds check self.selected_task

        self.display_record()        

    def increment_selected_task(self, amt):
        self.selected_task += amt

        # check if there are no tasks
        if (len(self.tasks) == 0):
            self.selected_task = -1
            return

        # cap to within bounds

        if (self.selected_task >= len(self.tasks)):
            self.selected_task = len(self.tasks) - 1

        if (self.selected_task < 0):
            self.selected_task = 0

        self.display_record()


    def display_record(self):
        self.short_name_ent.delete(0, "end")
        self.description_ent.delete(0, "end")
        
        task = TaskRecord()
        if (self.selected_task == -1):
            task.fill(id = -1, user_id = self.user.id, short_name = "", description = "")
            self.task_num_lbl["text"] = "Task #: {}".format("No Tasks")
        else:
            task = self.tasks[self.selected_task]
            self.task_num_lbl["text"] = "Task #: {}".format(self.selected_task + 1)

        self.short_name_ent.insert(0, task.short_name)
        self.description_ent.insert(0, task.description)

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
