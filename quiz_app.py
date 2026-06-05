import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from quiz_logic import QuizLogic
from quiz_dictionary import quiz_questions, tutorial_questions

"""
quiz_app.py - Main application file for the Hazardous Property (HP) Codes Quiz.

Builds and manages the Tkinter GUI including the welcome screen, tutorial screen, quiz screen, and results screen. 
Imports quiz logic from quiz_logic.py and data from quiz_dictionary.py.
Imports Pillow for ImageTk to position and size an image embedded in the GUI.
"""

root = tk.Tk()
root.title("Hazardous Property (HP) Codes Quiz")
root.geometry('900x700')
root.resizable(False, False)
root.configure(bg='#002B5A')

quiz = QuizLogic(quiz_questions)

# ============================================================
# WELCOME SCREEN
# ============================================================

welcome_frame = tk.Frame(root, bg='#002B5A', padx=60, pady=30, width=800)
welcome_frame.pack(expand=True, anchor='center')

# Title
title_label = tk.Label(
    welcome_frame,
    text="Welcome to the Hazardous Property (HP) Codes Quiz!",
    font=('Arial', 26, 'bold'),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=850,
    justify='left')
title_label.grid(row=0, column=0, columnspan=2, sticky='w', pady=(0, 8))

# Pulls in HW warning banner image
warning_img = Image.open('images/warning.png')
warning_img = warning_img.resize((325, 105))
warning_image = ImageTk.PhotoImage(warning_img)
warning_label = tk.Label(welcome_frame, image=warning_image, bg='#002B5A')
warning_label.image = warning_image
warning_label.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky="ew")
warning_label.configure(anchor="center")

# Quiz Opening Description
description_label = tk.Label(
    welcome_frame,
    text="In this quiz, you will match HP codes for hazardous classified waste to their corresponding definition.\n"
         "The aim is to support understanding of how we classify hazardous waste with codes according to the specific environmental or health risks that it poses.\n\n"
         "Please type your name below for your score to be saved -",
    font=('Arial', 20),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=700,
    justify='center',
    anchor='center')
description_label.grid(row=2, column=0, columnspan=2, sticky='w', pady=(8, 15))

# Player name entry row
name_row = tk.Frame(welcome_frame, bg='#002B5A')
name_row.grid(row=3, column=0, columnspan=2, sticky="w", pady=(0, 10))

name_label = tk.Label(
    name_row,
    text="Player name:",
    font=('Arial', 20, 'bold'),
    fg='#ffffff',
    bg='#002B5A')
name_label.pack(side="left", pady=(5, 0))

name_entry = tk.Entry(
    name_row,
    font=('Arial', 20),
    bg='#ffffff',
    fg="#000000",
    relief='sunken',
    width=25)
name_entry.pack(side="left", pady=(2, 0), padx=(10, 0))

# Lets Go button
def on_hover(e):
    """
    Changes the Lets Go button colour when the mouse hovers over it.
    """
    lets_go_button.config(bg="#C7BB13")

def on_leave(e):
    """
    Resets the Lets Go button colour when the mouse leaves it.
    """
    lets_go_button.config(bg='#FFE500',
                          fg='#000000')

def on_press(e):
    """
    Changes the Lets Go button colour for a pressed state.
    """
    lets_go_button.config(bg='#2F2A02',
                          fg='#ffffff')

def on_lets_go():
    """
    Handles the Lets Go button click on the welcome screen.
    Validates the player name entry using QuizLogic. 
    Displays an error messagebox if the entered name is triggers validate_name from quiz_logic, or switches to the tutorial screen if the name is accepted.
    """
    is_valid, result = quiz.set_player_name(name_entry.get())
    if not is_valid:
        messagebox.showerror("Invalid Name", result)
    else:
        # switch to tutorial frame here when built
        print(f"Name accepted: {quiz.player_name}")

lets_go_button = tk.Button(
    welcome_frame,
    text="Lets Go! 🚀",
    font=('Arial', 20, 'bold'),
    bg='#FFE500',
    fg='#000000',
    activebackground="#ffffff",
    relief='groove',
    padx=20,
    pady=8,
    cursor='hand2',
    command=on_lets_go)
lets_go_button.grid(row=5, column=0, columnspan=2, pady=(20, 0))

lets_go_button.bind('<Enter>', on_hover)
lets_go_button.bind('<Leave>', on_leave)
lets_go_button.bind('<ButtonPress-1>', on_press)

# ============================================================
# TUTORIAL SCREEN
# ============================================================

# ============================================================
# QUIZ SCREEN
# ============================================================

# ============================================================
# RESULTS SCREEN
# ============================================================

root.mainloop()