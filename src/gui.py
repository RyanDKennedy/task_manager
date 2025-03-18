import tkinter as tk
from tkinter import ttk

from database import Database
from author_record import AuthorRecord
from book_record import BookRecord

class GUI():

    def __init__(self):

        self.root = tk.Tk()

        self.db = Database()

        self.authors_records = self.db.authors_get_all_records()
        self.authors_selected_record_index = 0

        self.books_records = self.db.books_get_all_records()
        self.books_selected_record_index = 0

        self.feedback_lbl = ttk.Label(self.root, text="")
        self.feedback_lbl.pack()

        self.authors_create_gui_elements()
        self.books_create_gui_elements()

        self.refresh_display()

        self.root.mainloop()


    def authors_create_gui_elements(self):
        
        # record display
        self.authors_id_lbl = ttk.Label(self.root, text="ID:")
        self.authors_id_dpy = ttk.Label(self.root, text="")
        self.authors_id_lbl.pack()
        self.authors_id_dpy.pack()

        self.authors_name_lbl = ttk.Label(self.root, text="Name:")
        self.authors_name_ent = ttk.Entry(self.root)
        self.authors_name_lbl.pack()
        self.authors_name_ent.pack()
        
        self.authors_birth_year_lbl = ttk.Label(self.root, text="Birth Year:")
        self.authors_birth_year_ent = ttk.Entry(self.root)
        self.authors_birth_year_lbl.pack()
        self.authors_birth_year_ent.pack()


        # navigation buttons
        
        self.authors_back_all_btn = ttk.Button(self.root, text="|<", command=lambda: self.authors_increment_selected_record_index(-self.authors_selected_record_index))
        self.authors_back_all_btn.pack()

        self.authors_back_5_btn = ttk.Button(self.root, text="<<", command=lambda: self.authors_increment_selected_record_index(-5))
        self.authors_back_5_btn.pack()

        self.authors_back_1_btn = ttk.Button(self.root, text="<", command=lambda: self.authors_increment_selected_record_index(-1))
        self.authors_back_1_btn.pack()

        self.authors_next_1_btn = ttk.Button(self.root, text=">", command=lambda: self.authors_increment_selected_record_index(1))
        self.authors_next_1_btn.pack()

        self.authors_next_5_btn = ttk.Button(self.root, text=">>", command=lambda: self.authors_increment_selected_record_index(5))
        self.authors_next_5_btn.pack()

        self.authors_next_all_btn = ttk.Button(self.root, text=">|", command=lambda: self.authors_increment_selected_record_index(len(self.authors_records) - self.authors_selected_record_index))
        self.authors_next_all_btn.pack()

        # CRUD

        self.authors_insert_btn = ttk.Button(self.root, text="Insert", command=self.authors_insert_record)
        self.authors_insert_btn.pack()

        self.authors_update_btn = ttk.Button(self.root, text="Update", command=self.authors_update_current_record)
        self.authors_update_btn.pack()

        self.authors_delete_btn = ttk.Button(self.root, text="Delete", command=self.authors_delete_current_record)
        self.authors_delete_btn.pack()


    def authors_increment_selected_record_index(self, amt):
        self.authors_selected_record_index += amt

        if (self.authors_selected_record_index >= len(self.authors_records)):
            self.authors_selected_record_index = len(self.authors_records) - 1

        if (self.authors_selected_record_index < 0):
            self.authors_selected_record_index = 0

        self.refresh_display()

    def authors_display_record_at_index(self, index):
        if (len(self.authors_records) == 0):
            blank = AuthorRecord()
            blank.fill(-1, "No Records", 0)
            self.authors_display_record(blank)
            return

        if (index < len(self.authors_records) and index >= 0):
            self.authors_display_record(self.authors_records[index])
        else:
            self.feedback_lbl["text"] = "ERROR: Tried to display index out of bounds."

    def authors_display_record(self, record):
        self.authors_id_dpy["text"] = str(record.id)
        self.authors_name_ent.delete(0, "end")
        self.authors_name_ent.insert(0, record.name)
        self.authors_birth_year_ent.delete(0, "end")
        self.authors_birth_year_ent.insert(0, str(record.birth_year))

    def authors_insert_record(self):
        rec = AuthorRecord()
        rec.fill(-1, self.authors_name_ent.get(), int(self.authors_birth_year_ent.get()))
        self.db.authors_insert(rec)
        self.authors_records = self.db.authors_get_all_records()
        self.refresh_display()

    def authors_delete_current_record(self):
        current_record = self.authors_records[self.authors_selected_record_index]
        self.db.authors_delete(current_record.id)
        self.authors_records = self.db.authors_get_all_records()
        self.books_records = self.db.books_get_all_records()
        self.refresh_display()

    def authors_update_current_record(self):
        rec = AuthorRecord()
        rec.fill(self.authors_records[self.authors_selected_record_index].id, self.authors_name_ent.get(), int(self.authors_birth_year_ent.get()))
        self.db.authors_update(rec)
        self.authors_records = self.db.authors_get_all_records()
        self.refresh_display()

    # ==== Books Stuff ====

    def books_create_gui_elements(self):
        
        # record display
        self.books_id_lbl = ttk.Label(self.root, text="ID:")
        self.books_id_dpy = ttk.Label(self.root, text="")
        self.books_id_lbl.pack()
        self.books_id_dpy.pack()

        self.books_name_lbl = ttk.Label(self.root, text="Name:")
        self.books_name_ent = ttk.Entry(self.root)
        self.books_name_lbl.pack()
        self.books_name_ent.pack()

        self.books_year_released_lbl = ttk.Label(self.root, text="Year Released:")
        self.books_year_released_ent = ttk.Entry(self.root)
        self.books_year_released_lbl.pack()
        self.books_year_released_ent.pack()

        self.books_page_amt_lbl = ttk.Label(self.root, text="Page Amount:")
        self.books_page_amt_ent = ttk.Entry(self.root)
        self.books_page_amt_lbl.pack()
        self.books_page_amt_ent.pack()

        self.books_price_lbl = ttk.Label(self.root, text="Price:")
        self.books_price_ent = ttk.Entry(self.root)
        self.books_price_lbl.pack()
        self.books_price_ent.pack()

        self.books_author_lbl = ttk.Label(self.root, text="Author:")
        self.books_author_val = tk.StringVar()
        self.books_author_cbx = ttk.Combobox(self.root, textvariable=self.books_author_val)
        self.books_author_cbx["values"] = [""]
        self.books_author_cbx["state"] = "readonly"
        self.books_author_val.set("")
        self.books_author_lbl.pack()
        self.books_author_cbx.pack()
        

        # navigation buttons
        
        self.books_back_all_btn = ttk.Button(self.root, text="|<", command=lambda: self.books_increment_selected_record_index(-self.books_selected_record_index))
        self.books_back_all_btn.pack()

        self.books_back_5_btn = ttk.Button(self.root, text="<<", command=lambda: self.books_increment_selected_record_index(-5))
        self.books_back_5_btn.pack()

        self.books_back_1_btn = ttk.Button(self.root, text="<", command=lambda: self.books_increment_selected_record_index(-1))
        self.books_back_1_btn.pack()

        self.books_next_1_btn = ttk.Button(self.root, text=">", command=lambda: self.books_increment_selected_record_index(1))
        self.books_next_1_btn.pack()

        self.books_next_5_btn = ttk.Button(self.root, text=">>", command=lambda: self.books_increment_selected_record_index(5))
        self.books_next_5_btn.pack()

        self.books_next_all_btn = ttk.Button(self.root, text=">|", command=lambda: self.books_increment_selected_record_index(len(self.books_records) - self.books_selected_record_index))
        self.books_next_all_btn.pack()

        # CRUD

        self.books_insert_btn = ttk.Button(self.root, text="Insert", command=self.books_insert_record)
        self.books_insert_btn.pack()

        self.books_update_btn = ttk.Button(self.root, text="Update", command=self.books_update_current_record)
        self.books_update_btn.pack()

        self.books_delete_btn = ttk.Button(self.root, text="Delete", command=self.books_delete_current_record)
        self.books_delete_btn.pack()


    def books_increment_selected_record_index(self, amt):
        self.books_selected_record_index += amt

        if (self.books_selected_record_index >= len(self.books_records)):
            self.books_selected_record_index = len(self.books_records) - 1

        if (self.books_selected_record_index < 0):
            self.books_selected_record_index = 0

        self.refresh_display()

    def books_display_record_at_index(self, index):
        if (len(self.books_records) == 0):
            blank = BookRecord()
            blank.fill(-1, "No Records", 0, 0, 0, -1)
            self.books_display_record(blank, "No Records")
            return

        if (index < len(self.books_records) and index >= 0):
            self.books_display_record(self.books_records[index], self.books_format_cbx_value(self.books_records[index].author_id))
        else:
            self.feedback_lbl["text"] = "ERROR: Tried to display index out of bounds."

    def books_display_record(self, record, cbx_value):
        self.books_id_dpy["text"] = str(record.id)
        self.books_name_ent.delete(0, "end")
        self.books_name_ent.insert(0, record.name)
        self.books_year_released_ent.delete(0, "end")
        self.books_year_released_ent.insert(0, str(record.year_released))
        self.books_page_amt_ent.delete(0, "end")
        self.books_page_amt_ent.insert(0, str(record.page_amt))
        self.books_price_ent.delete(0, "end")
        self.books_price_ent.insert(0, str(record.price))
        self.books_author_val.set(cbx_value)

    def books_format_cbx_value(self, id):
        for author in self.authors_records:
            if (author.id == id):
                return "{} - {}".format(str(id), author.name)        

        return "{} is not a valid id".format(str(id))

    def books_get_author_id_from_cbx_value(self, text):
        arr = text.split(" ")
        return int(arr[0])

    def books_insert_record(self):
        rec = BookRecord()
        rec.fill(-1, self.books_name_ent.get(), int(self.books_year_released_ent.get()), int(self.books_page_amt_ent.get()), float(self.books_price_ent.get()), self.books_get_author_id_from_cbx_value(self.books_author_val.get()))
        self.db.books_insert(rec)
        self.books_records = self.db.books_get_all_records()
        self.refresh_display()

    def books_delete_current_record(self):
        current_record = self.books_records[self.books_selected_record_index]
        self.db.books_delete(current_record.id)
        self.books_records = self.db.books_get_all_records()
        self.refresh_display()

    def books_update_current_record(self):
        rec = BookRecord()
        rec.fill(self.books_records[self.books_selected_record_index].id, self.books_name_ent.get(), int(self.books_year_released_ent.get()), int(self.books_page_amt_ent.get()), float(self.books_price_ent.get()), self.books_get_author_id_from_cbx_value(self.books_author_val.get()))
        self.db.books_update(rec)
        self.books_records = self.db.books_get_all_records()
        self.refresh_display()

    def refresh_display(self):

        if (self.authors_selected_record_index >= len(self.authors_records)):
            self.authors_selected_record_index = len(self.authors_records) - 1

        if (self.authors_selected_record_index < 0):
            self.authors_selected_record_index = 0

        if (self.books_selected_record_index >= len(self.books_records)):
            self.books_selected_record_index = len(self.books_records) - 1

        if (self.books_selected_record_index < 0):
            self.books_selected_record_index = 0

        author_arr = []
        for author in self.authors_records:
            author_arr.append("{} - {}".format(author.id, author.name))

        self.books_author_cbx["values"] = author_arr

        self.authors_display_record_at_index(self.authors_selected_record_index)
        self.books_display_record_at_index(self.books_selected_record_index)
