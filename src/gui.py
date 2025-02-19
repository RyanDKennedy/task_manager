import tkinter as tk
from tkinter import ttk

from database import Database

class GUI():

    def __init__(self):

        self.root = tk.Tk()
        self.create_gui_elements()

        self.db = Database()
        self.records = self.db.get_all_records()
        self.selected_record_index = 0

        # 0 if normal operation, 1 if ready for inserting record
        self.inserting_record = 0

        self.refresh_display()

        self.root.mainloop()


    def create_gui_elements(self):
        # feedback
        self.feedback_lbl = ttk.Label(self.root, text="")
        self.feedback_lbl.pack()
        
        # record display
        
        self.id_lbl = ttk.Label(self.root, text="ID:")
        self.id_dpy = ttk.Label(self.root, text="")
        self.id_lbl.pack()
        self.id_dpy.pack()

        self.name_lbl = ttk.Label(self.root, text="Name:")
        self.name_ent = ttk.Entry(self.root)
        self.name_lbl.pack()
        self.name_ent.pack()

        self.age_lbl = ttk.Label(self.root, text="Age:")
        self.age_ent = ttk.Entry(self.root)
        self.age_lbl.pack()
        self.age_ent.pack()

        self.gender_lbl = ttk.Label(self.root, text="Gender:")
        self.gender_val = tk.StringVar()
        self.gender_cbx = ttk.Combobox(self.root, textvariable=self.gender_val)
        self.gender_cbx["values"] = ["Male", "Female"]
        self.gender_cbx["state"] = "readonly"
        self.gender_val.set("Male")
        self.gender_lbl.pack()
        self.gender_cbx.pack()

        # navigation buttons
        
        self.back_all_btn = ttk.Button(self.root, text="|<", command=lambda: self.increment_selected_record_index(-self.selected_record_index))
        self.back_all_btn.pack()

        self.back_5_btn = ttk.Button(self.root, text="<<", command=lambda: self.increment_selected_record_index(-5))
        self.back_5_btn.pack()

        self.back_1_btn = ttk.Button(self.root, text="<", command=lambda: self.increment_selected_record_index(-1))
        self.back_1_btn.pack()

        self.next_1_btn = ttk.Button(self.root, text=">", command=lambda: self.increment_selected_record_index(1))
        self.next_1_btn.pack()

        self.next_5_btn = ttk.Button(self.root, text=">>", command=lambda: self.increment_selected_record_index(5))
        self.next_5_btn.pack()

        self.next_all_btn = ttk.Button(self.root, text=">|", command=lambda: self.increment_selected_record_index(len(self.records) - self.selected_record_index))
        self.next_all_btn.pack()

        # CRUD

        self.insert_btn = ttk.Button(self.root, text="Start Insert", command=self.start_insert_record)
        self.insert_btn.pack()

        self.update_btn = ttk.Button(self.root, text="Update", command=self.update_current_record)
        self.update_btn.pack()

        self.delete_btn = ttk.Button(self.root, text="Delete", command=self.delete_current_record)
        self.delete_btn.pack()

    def delete_current_record(self):
        if (len(self.records) > 0):
            id = self.records[self.selected_record_index][0]
            self.db.delete(id)
            self.records = self.db.get_all_records()
            self.refresh_display()
            
    def update_current_record(self):
        if (len(self.records) > 0):
            record = [self.records[self.selected_record_index][0], self.name_ent.get(), self.age_ent.get(), self.gender_val.get()]
            self.db.update(record)
            self.records = self.db.get_all_records()
            self.refresh_display()

    def start_insert_record(self):
        self.inserting_record = 1
        self.insert_btn["text"] = "Insert"
        self.insert_btn["command"] = self.insert_record
        self.refresh_display()

    def insert_record(self):
        self.inserting_record = 0
        self.insert_btn["text"] = "Start Insert"
        self.insert_btn["command"] = self.start_insert_record

        record = [-1, self.name_ent.get(), self.age_ent.get(), self.gender_val.get()]
        self.db.insert(record)
        self.records = self.db.get_all_records()

        self.refresh_display()

    # val = 1 = show buttons, val = 0 = hide buttons
    def hide_show_nav_buttons(self, val):
        if (val == 0):
            self.back_all_btn["state"] = "disabled"
            self.back_5_btn["state"] = "disabled"
            self.back_1_btn["state"] = "disabled"
            self.next_all_btn["state"] = "disabled"
            self.next_5_btn["state"] = "disabled"
            self.next_1_btn["state"] = "disabled"
        elif (val == 1):
            self.back_all_btn["state"] = "normal"
            self.back_5_btn["state"] = "normal"
            self.back_1_btn["state"] = "normal"
            self.next_all_btn["state"] = "normal"
            self.next_5_btn["state"] = "normal"
            self.next_1_btn["state"] = "normal"            

    def increment_selected_record_index(self, amt):
        self.selected_record_index += amt
        self.refresh_display()

    def refresh_display(self):

        # if the user is currently inserting a record
        if (self.inserting_record == 1):
            self.display_record([-1, "", "", "Male"])
            self.hide_show_nav_buttons(0)
            self.update_btn["state"] = "disabled"
            self.delete_btn["state"] = "disabled"
            return


        # if the user is currently not inserting a record
        self.hide_show_nav_buttons(1)
        self.update_btn["state"] = "normal"
        self.delete_btn["state"] = "normal"

        # updates record display and makes sure the selected_record_index is within bounds
        if (len(self.records) == 0):
            self.selected_record_index = 0
            self.display_record([-1, "No Records", "No Records", "No Records"])
        else:
            # setting an upper and lower limit for self.selected_record_index to prevent index out of bounds
            if (self.selected_record_index >= len(self.records)):
                self.selected_record_index = len(self.records) - 1
            if (self.selected_record_index < 0):
                self.selected_record_index = 0

            self.display_record_at_index(self.selected_record_index)
        

    def display_record_at_index(self, index):
        if (index < len(self.records)):
            self.display_record(self.records[index])
        else:
            self.feedback_lbl["text"] = "ERROR: Tried to display index beyond bounds."


    def display_record(self, record):
        self.id_dpy["text"] = record[0]

        self.name_ent.delete(0, "end")
        self.name_ent.insert(0, record[1])

        self.age_ent.delete(0, "end")
        self.age_ent.insert(0, record[2])

        self.gender_val.set(record[3])
