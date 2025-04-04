"""
Ryan Kennedy, Gabriel Walder
Cmdr. Schenk
Cloud Computing
7th Period
March 18, 2025
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from database import Database
from author_record import AuthorRecord
from book_record import BookRecord

class GUI():

    def __init__(self):

        # tkinter init
        self.root = tk.Tk()
        self.root.geometry("1000x1000")

        # db init
        self.db = Database()

        # get the records and set navigation defaults
        self.authors_records = self.db.authors_get_all_records()
        self.authors_selected_record_index = 0
        self.books_records = self.db.books_get_all_records()
        self.books_selected_record_index = 0

        # create canvas for display
        self.canvas = tk.Canvas(self.root, width=1000, height=1000)
        self.canvas.pack()

        # create label for user feedback
        self.feedback_lbl = ttk.Label(self.root, text="", font=("Helvetica", 14))
        self.feedback_lbl.place(x=500, y=10, anchor="center")

        # create the actual gui
        self.authors_create_gui_elements()
        self.books_create_gui_elements()

        # refreshes the display so the correct things show
        self.refresh_display()

        self.root.mainloop()


    def authors_create_gui_elements(self):

        # title

        self.authors_display_lbl = ttk.Label(self.root, text="Authors:", font=("Helvetica", 18))
        self.authors_display_lbl.place(x=500,y=35)
        self.canvas.create_rectangle(300, 75, 800, 375, outline="black", width=3)

        # record display

        self.authors_id_lbl = ttk.Label(self.root, text="ID:", font=("Helvetica", 14))
        self.authors_id_dpy = ttk.Label(self.root, text="", font=("Helvetica", 14))
        self.authors_id_lbl.place(x=475,y=130)
        self.authors_id_dpy.place(x=525,y=130)

        self.authors_name_lbl = ttk.Label(self.root, text="Name:", font=("Helvetica", 14))
        self.authors_name_ent = ttk.Entry(self.root, width=20 )
        self.authors_name_lbl.place(x=460, y=160)
        self.authors_name_ent.place(x=540, y=160)
        
        self.authors_birth_year_lbl = ttk.Label(self.root, text="Birth Year:")
        self.authors_birth_year_ent = ttk.Entry(self.root, width=20 )
        self.authors_birth_year_lbl.place(x=460, y=190)
        self.authors_birth_year_ent.place(x=540, y=190)

        # navigation buttons

        self.authors_back_all_btn = ttk.Button(self.root, text="|<", command=lambda: self.authors_increment_selected_record_index(-self.authors_selected_record_index))
        self.authors_back_all_btn.place(x=340, y=220)

        self.authors_back_5_btn = ttk.Button(self.root, text="<<", command=lambda: self.authors_increment_selected_record_index(-5))
        self.authors_back_5_btn.place(x=410, y=220)

        self.authors_back_1_btn = ttk.Button(self.root, text="<", command=lambda: self.authors_increment_selected_record_index(-1))
        self.authors_back_1_btn.place(x=480, y=220)

        self.authors_next_1_btn = ttk.Button(self.root, text=">", command=lambda: self.authors_increment_selected_record_index(1))
        self.authors_next_1_btn.place(x=550, y=220)

        self.authors_next_5_btn = ttk.Button(self.root, text=">>", command=lambda: self.authors_increment_selected_record_index(5))
        self.authors_next_5_btn.place(x=620, y=220)

        self.authors_next_all_btn = ttk.Button(self.root, text=">|", command=lambda: self.authors_increment_selected_record_index(len(self.authors_records) - self.authors_selected_record_index))
        self.authors_next_all_btn.place(x=690, y=220)

        # CRUD

        self.authors_insert_btn = ttk.Button(self.root, text="Insert", command=self.authors_insert_record)
        self.authors_insert_btn.place(x=430, y=250)

        self.authors_update_btn = ttk.Button(self.root, text="Update", command=self.authors_update_current_record)
        self.authors_update_btn.place(x=500, y=250)

        self.authors_delete_btn = ttk.Button(self.root, text="Delete", command=self.authors_delete_current_record)
        self.authors_delete_btn.place(x=570,y=250)


    def authors_increment_selected_record_index(self, amt):
        self.authors_selected_record_index += amt

        if (self.authors_selected_record_index >= len(self.authors_records)):
            self.authors_selected_record_index = len(self.authors_records) - 1

        if (self.authors_selected_record_index < 0):
            self.authors_selected_record_index = 0

        self.refresh_display()

    def authors_display_record_at_index(self, index):
        # display blank record if there are no records
        if (len(self.authors_records) == 0):
            blank = AuthorRecord()
            blank.fill(-1, "No Records", 0)
            self.authors_display_record(blank)
            return

        # check for index out of range
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
        # don't insert if input isn't valid
        if (self.authors_validate_input() == False):
            return

        rec = AuthorRecord()
        rec.fill(-1, self.authors_name_ent.get(), int(self.authors_birth_year_ent.get()))

        result = messagebox.askquestion("Author Insert Confirmation", "Are you sure that you would like to insert this author?\n\n"+rec.to_string())
        if (result != "yes"):
            return

        self.db.authors_insert(rec)
        self.authors_records = self.db.authors_get_all_records()
        self.refresh_display()

    def authors_delete_current_record(self):
        # if there are no authors then you can't delete an author so return
        if (len(self.authors_records) == 0):
            self.feedback_lbl["text"] = "You cannot delete an author that doesn't exist."
            return

        current_record = self.authors_records[self.authors_selected_record_index]

        result = messagebox.askquestion("Author Delete Confirmation", "Are you sure that you would like to delete this author, and all the books associated with them?\n\n"+current_record.to_string())
        if (result != "yes"):
            return

        self.db.authors_delete(current_record.id)
        self.authors_records = self.db.authors_get_all_records()
        self.books_records = self.db.books_get_all_records()
        self.refresh_display()

    def authors_update_current_record(self):
        # don't update if input is not valid
        if (self.authors_validate_input() == False):
            return

        # you cannot update if there are no records
        if (len(self.authors_records) == 0):
            self.feedback_lbl["text"] = "You cannot update an author that doesn't exist."
            return

        rec = AuthorRecord()
        rec.fill(self.authors_records[self.authors_selected_record_index].id, self.authors_name_ent.get(), int(self.authors_birth_year_ent.get()))

        result = messagebox.askquestion("Author Update Confirmation", "Are you sure that you would like to update this author?\n\nBefore:\n"+self.authors_records[self.authors_selected_record_index].to_string()+"\n\nAfter:\n"+rec.to_string())
        if (result != "yes"):
            return

        self.db.authors_update(rec)
        self.authors_records = self.db.authors_get_all_records()
        self.refresh_display()

    def authors_validate_input(self):
        name_text = self.authors_name_ent.get()
        birth_year_text = self.authors_birth_year_ent.get()
        
        # check for semicolons or quotes to prevent sql injection
        if (self.is_character_in_string(name_text, '\'') or self.is_character_in_string(name_text, ';') or self.is_character_in_string(birth_year_text, '\'') or self.is_character_in_string(birth_year_text, ';')):
            self.feedback_lbl["text"] = "You cannot have ' or ; in your inputs."
            return False

        # see if birth_year_text is a valid integer
        try:
            birth_year_num = int(birth_year_text)
        except:
            self.feedback_lbl["text"] = "Birth year has to be a valid number."
            return False

        return True

    # ==== Books Stuff ====

    def books_create_gui_elements(self):

        # title

        self.books_display_lbl = ttk.Label(self.root, text="Books:", font=("Helvetica", 18))
        self.books_display_lbl.place(x=500,y=540)
        self.canvas.create_rectangle(300, 575, 800, 875, outline="black", width=3)

        # record display

        self.books_id_lbl = ttk.Label(self.root, text="ID:", font=("Helvetica", 14))
        self.books_id_dpy = ttk.Label(self.root, text="", font=("Helvetica", 14))
        self.books_id_lbl.place(x=475,y=590)
        self.books_id_dpy.place(x=525,y=590)

        self.books_name_lbl = ttk.Label(self.root, text="Name:", font=("Helvetica", 14))
        self.books_name_ent = ttk.Entry(self.root, width=20 )
        self.books_name_lbl.place(x=460, y=620)
        self.books_name_ent.place(x=540, y=620)

        self.books_year_released_lbl = ttk.Label(self.root, text="Published Year:", font=("Helvetica", 14))
        self.books_year_released_ent = ttk.Entry(self.root, width=20 )
        self.books_year_released_lbl.place(x=430, y=650)
        self.books_year_released_ent.place(x=580, y=650)

        self.books_page_amt_lbl = ttk.Label(self.root, text="# of Pages:", font=("Helvetica", 14))
        self.books_page_amt_ent = ttk.Entry(self.root, width=20 )
        self.books_page_amt_lbl.place(x=430, y=680)
        self.books_page_amt_ent.place(x=580, y=680)

        self.books_price_lbl = ttk.Label(self.root, text="Price:", font=("Helvetica", 14))
        self.books_price_ent = ttk.Entry(self.root, width=20 )
        self.books_price_lbl.place(x=460, y=710)
        self.books_price_ent.place(x=540, y=710)

        self.books_author_lbl = ttk.Label(self.root, text="Author:", font=("Helvetica", 14))
        self.books_author_val = tk.StringVar()
        self.books_author_cbx = ttk.Combobox(self.root, textvariable=self.books_author_val)
        self.books_author_cbx["values"] = [""]
        self.books_author_cbx["state"] = "readonly"
        self.books_author_val.set("")
        self.books_author_lbl.place(x=460, y=740)
        self.books_author_cbx.place(x=540, y=740)
        
        # navigation buttons
        
        self.books_back_all_btn = ttk.Button(self.root, text="|<", command=lambda: self.books_increment_selected_record_index(-self.books_selected_record_index))
        self.books_back_all_btn.place(x=340, y=770)

        self.books_back_5_btn = ttk.Button(self.root, text="<<", command=lambda: self.books_increment_selected_record_index(-5))
        self.books_back_5_btn.place(x=410, y=770)

        self.books_back_1_btn = ttk.Button(self.root, text="<", command=lambda: self.books_increment_selected_record_index(-1))
        self.books_back_1_btn.place(x=480, y=770)

        self.books_next_1_btn = ttk.Button(self.root, text=">", command=lambda: self.books_increment_selected_record_index(1))
        self.books_next_1_btn.place(x=550, y=770)

        self.books_next_5_btn = ttk.Button(self.root, text=">>", command=lambda: self.books_increment_selected_record_index(5))
        self.books_next_5_btn.place(x=620, y=770)

        self.books_next_all_btn = ttk.Button(self.root, text=">|", command=lambda: self.books_increment_selected_record_index(len(self.books_records) - self.books_selected_record_index))
        self.books_next_all_btn.place(x=690, y=770)

        # CRUD

        self.books_insert_btn = ttk.Button(self.root, text="Insert", command=self.books_insert_record)
        self.books_insert_btn.place(x=430, y=800)

        self.books_update_btn = ttk.Button(self.root, text="Update", command=self.books_update_current_record)
        self.books_update_btn.place(x=500, y=800)

        self.books_delete_btn = ttk.Button(self.root, text="Delete", command=self.books_delete_current_record)
        self.books_delete_btn.place(x=570, y=800)

    def books_increment_selected_record_index(self, amt):
        self.books_selected_record_index += amt

        if (self.books_selected_record_index >= len(self.books_records)):
            self.books_selected_record_index = len(self.books_records) - 1

        if (self.books_selected_record_index < 0):
            self.books_selected_record_index = 0

        self.refresh_display()

    def books_display_record_at_index(self, index):
        # if there are no records then display empty record
        if (len(self.books_records) == 0):
            blank = BookRecord()
            blank.fill(-1, "No Records", 0, 0, 0, -1)
            self.books_display_record(blank, "-1 - No Records")
            return

        # check for index out of bounds
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

    # format data into the format which the combobox displays
    def books_format_cbx_value(self, id):
        for author in self.authors_records:
            if (author.id == id):
                return "{} - {}".format(str(id), author.name)        

        return "{} is not a valid id".format(str(id))

    # take the combobox display and decode the data from it
    def books_get_author_id_from_cbx_value(self, text):
        arr = text.split(" ")
        return int(arr[0])

    def books_insert_record(self):
        # return if the input is not valid
        if (self.books_validate_input() == False):
            return

        # make sure the author_id is a valid id / not the nonexistent record id
        author_id = self.books_get_author_id_from_cbx_value(self.books_author_val.get())
        if (author_id == -1):
            self.feedback_lbl["text"] = "You must have a valid author selected."
            return

        rec = BookRecord()
        rec.fill(-1, self.books_name_ent.get(), int(self.books_year_released_ent.get()), int(self.books_page_amt_ent.get()), float(self.books_price_ent.get()), author_id)

        result = messagebox.askquestion("Book Insert Confirmation", "Are you sure that you would like to insert this book?\n\n"+rec.to_string())
        if (result != "yes"):
            return

        self.db.books_insert(rec)
        self.books_records = self.db.books_get_all_records()
        self.refresh_display()
        
    def books_delete_current_record(self):
        # if there are no books then you can't delete a book
        if (len(self.books_records) == 0):
            self.feedback_lbl["text"] = "You cannot delete a book that doesn't exist."
            return

        current_record = self.books_records[self.books_selected_record_index]

        result = messagebox.askquestion("Book Delete Confirmation", "Are you sure that you would like to delete this book?\n\n"+current_record.to_string())
        if (result != "yes"):
            return

        self.db.books_delete(current_record.id)
        self.books_records = self.db.books_get_all_records()
        self.refresh_display()

    def books_update_current_record(self):
        # return if input is not valid
        if (self.books_validate_input() == False):
            return

        # you cannot update a book if there are no books
        if (len(self.books_records) == 0):
            self.feedback_lbl["text"] = "You cannot update a book that doesn't exist."
            return

        rec = BookRecord()
        rec.fill(self.books_records[self.books_selected_record_index].id, self.books_name_ent.get(), int(self.books_year_released_ent.get()), int(self.books_page_amt_ent.get()), float(self.books_price_ent.get()), self.books_get_author_id_from_cbx_value(self.books_author_val.get()))

        result = messagebox.askquestion("Book Update Confirmation", "Are you sure that you would like to update this book?\n\nBefore:\n"+self.books_records[self.books_selected_record_index].to_string()+"\n\nAfter:\n"+rec.to_string())
        if (result != "yes"):
            return

        self.db.books_update(rec)
        self.books_records = self.db.books_get_all_records()
        self.refresh_display()
            
    def books_validate_input(self):
        name_text = self.books_name_ent.get()
        year_released_text = self.books_year_released_ent.get()
        page_amt_text = self.books_page_amt_ent.get()
        price_text = self.books_price_ent.get()
        
        # make sure none of the inputs contain ' or ; to prevent sql injections
        if (self.is_character_in_string(name_text, '\'') or self.is_character_in_string(name_text, ';') or
            self.is_character_in_string(year_released_text, '\'') or self.is_character_in_string(year_released_text, ';') or
            self.is_character_in_string(page_amt_text, '\'') or self.is_character_in_string(page_amt_text, ';') or
            self.is_character_in_string(price_text, '\'') or self.is_character_in_string(price_text, ';')):

            self.feedback_lbl["text"] = "You cannot have ' or ; in your inputs."
            return False

        # make sure that all inputs correctly convert to int or float
        try:
            year_released = int(year_released_text)
            page_amt = int(page_amt_text)
            price = float(price_text)
        except:
            self.feedback_lbl["text"] = "Your inputs (year released, page amount, price) aren't valid numbers."
            return False

        return True

        

    def refresh_display(self):

        # cap indexes between their valid ranges

        if (self.authors_selected_record_index >= len(self.authors_records)):
            self.authors_selected_record_index = len(self.authors_records) - 1

        if (self.authors_selected_record_index < 0):
            self.authors_selected_record_index = 0

        if (self.books_selected_record_index >= len(self.books_records)):
            self.books_selected_record_index = len(self.books_records) - 1

        if (self.books_selected_record_index < 0):
            self.books_selected_record_index = 0

        # update the combobox options

        author_arr = []
        for author in self.authors_records:
            author_arr.append("{} - {}".format(author.id, author.name))

        self.books_author_cbx["values"] = author_arr

        # display the current record
        self.authors_display_record_at_index(self.authors_selected_record_index)
        self.books_display_record_at_index(self.books_selected_record_index)

    # function that sees if a character is in a string
    def is_character_in_string(self, string, character):
        for c in string:
            if (c == character):
                return True
        return False
