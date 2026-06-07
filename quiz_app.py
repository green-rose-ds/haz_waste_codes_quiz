import tkinter as tk
from tkinter import messagebox, ttk
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
root.option_add('*TCombobox*Listbox.font', ('Arial', 11))
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

# Welcome title 
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

# Quiz opening description
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
    Handles the Let's Go button click on the welcome screen.
    Validates the player name entry using QuizLogic. 
    Displays an error messagebox if the entered name is triggers validate_name from quiz_logic, or switches to the tutorial screen if the name is accepted.
    """
    is_valid, result = quiz.set_player_name(name_entry.get())
    if not is_valid:
        messagebox.showerror("Invalid Name", result)
    else:
        show_tutorial()

lets_go_button = tk.Button(
    welcome_frame,
    text="Let's Go! 🚀",
    font=('Arial', 16, 'bold'),
    bg='#FFE500',
    fg='#000000',
    activebackground="#ffffff",
    relief='groove',
    padx=8,
    pady=3,
    cursor='hand2',
    command=on_lets_go)
lets_go_button.grid(row=5, column=0, columnspan=2, pady=(20, 0))

lets_go_button.bind('<Enter>', on_hover)
lets_go_button.bind('<Leave>', on_leave)
lets_go_button.bind('<ButtonPress-1>', on_press)

# ============================================================
# TUTORIAL SCREEN
# ============================================================

tutorial_frame = tk.Frame(root, bg='#002B5A', padx=60, pady=30, width=800)

def show_tutorial():
    """
    Switches from the welcome screen to the tutorial screen.
    Hides the welcome screen, updates the player name in the title, and displays the tutorial screen.
    """
    welcome_frame.pack_forget()

    # Update title with the validated player's name
    tutorial_title.config(text=f"Hello {quiz.player_name} 👋, after a quick tutorial you're ready to go!")
    tutorial_frame.pack(expand=True, fill='both', anchor='center')

# Tutorial title
tutorial_title = tk.Label(
    tutorial_frame,
    text="",
    font=('Arial', 22, 'bold'),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=800,
    justify='left')
tutorial_title.grid(row=0, column=0, columnspan=3, sticky='w', pady=(0, 8))

# Tutorial instructions
tutorial_instruction = tk.Label(
    tutorial_frame,
    text="I've connected the last 2 HP codes as an example for you below! On the next screen you will be shown 1-14 of the HP codes on the left, with the randomly sorted definitions on the right.\n\n"
         "You will first click on the HP code on the left, and then select the definition you think matches it for a line to be drawn between them. "
         "Once you have matched all of the HP codes to a description you will be able to submit them and see your score.\n\n"
         "If you need to brush up on your classifications knowledge first, please visit:",
    font=('Arial', 14),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=800,
    justify='left')
tutorial_instruction.grid(row=1, column=0, columnspan=3, sticky='w', pady=(0, 2))

# Link to external calssification guidance
guidance_link = tk.Label(
    tutorial_frame,
    text="GOV.UK Waste Classification Technical Guidance",
    font=('Arial', 14, 'underline'),
    fg='#FFE500',
    bg='#002B5A',
    cursor='hand2')
guidance_link.grid(row=2, column=0, columnspan=3, sticky='w', pady=(0, 15))

guidance_link.bind('<Button-1>', lambda e: webbrowser.open(
    "https://www.gov.uk/government/publications/classify-different-types-of-waste"))
guidance_link.bind('<Enter>', lambda e: guidance_link.config(fg='#ffffff'))
guidance_link.bind('<Leave>', lambda e: guidance_link.config(fg='#FFE500'))

# Column headers
tk.Label(
    tutorial_frame,
    text="HP Code",
    font=('Arial', 13, 'bold'),
    fg='#FFE500',
    bg='#002B5A').grid(row=3, column=0, sticky='w', pady=(0, 5))

tk.Label(
    tutorial_frame,
    text="Definition",
    font=('Arial', 13, 'bold'),
    fg='#FFE500',
    bg='#002B5A').grid(row=3, column=2, sticky='w', pady=(0, 5))

# Example HP code buttons
for i, (item, answer) in enumerate(tutorial_questions.items()):

    # HP code label
    hp_frame = tk.Frame(tutorial_frame, bg='#FFE500')
    hp_frame.grid(row=4 + i, column=0, sticky='w', pady=5)
    tk.Label(
        hp_frame,
        text=item,
        font=('Arial', 13, 'bold'),
        bg='#ffffff',
        fg='#002B5A',
        width=22,
        pady=8).pack(pady=(0, 3))

    # Line to show connected HP code and definition
    tk.Label(
        tutorial_frame,
        text="──────────",
        font=('Arial', 12),
        fg='#FFE500',
        bg='#002B5A').grid(row=4 + i, column=1, padx=10)

    # Example definition buttons
    tk.Label(
        tutorial_frame,
        text=answer,
        font=('Arial', 12),
        bg='#ffffff',
        fg='#002B5A',
        width=45,
        pady=8,
        wraplength=400,
        justify='left').grid(row=4 + i, column=2, sticky='w', pady=5)

# Buttons on the bottom row
bottom_row = tk.Frame(tutorial_frame, bg='#002B5A')
bottom_row.grid(row=7, column=0, columnspan=3, pady=(20, 0))

# Back to welcome screen button
back_label = tk.Label(
    bottom_row,
    text="< Back to welcome screen",
    font=('Arial', 16),
    fg='#FFE500',
    bg='#002B5A',
    cursor='hand2')
back_label.pack(side='left', padx=(0, 30))
back_label.bind('<Button-1>', lambda e: [
    tutorial_frame.pack_forget(),
    welcome_frame.pack(expand=True, anchor='center')])

# Let's Begin button
def on_begin_hover(e):
    """
    Changes the Lets Begin button colour on hover.
    """
    lets_begin_button.config(bg='#C7BB13')

def on_begin_leave(e):
    """
    Resets the Let's Begin button colour when mouse leaves.
    """
    lets_begin_button.config(bg='#FFE500', fg='#000000')

def on_begin_press(e):
    """
    Changes the Let's Begin button for pressed state.
    """
    lets_begin_button.config(bg='#2F2A02', fg='#ffffff')

def on_lets_begin():
    """
    Handles the Let's Begin button click on the tutorial screen.
    Switches from the tutorial screen to the main quiz screen.
    """
    tutorial_frame.pack_forget()
    show_quiz()

lets_begin_button = tk.Button(
    bottom_row,
    text="Let's Begin! 🚀",
    font=('Arial', 16, 'bold'),
    bg='#FFE500',
    fg='#000000',
    activebackground='#ffffff',
    relief='groove',
    padx=8,
    pady=3,
    cursor='hand2',
    command=on_lets_begin)
lets_begin_button.pack(side='left')

lets_begin_button.bind('<Enter>', on_begin_hover)
lets_begin_button.bind('<Leave>', on_begin_leave)
lets_begin_button.bind('<ButtonPress-1>', on_begin_press)

# ============================================================
# QUIZ SCREEN
# ============================================================

quiz_frame = tk.Frame(root, bg='#002B5A', padx=40, pady=20, width=800)

#ttk styling for the dropdown boxes
style = ttk.Style()
style.theme_use('clam')
style.configure(
    'TCombobox',
    fieldbackground='#ffffff',
    background='#ffffff',
    foreground='#002B5A',
    arrowcolor='#002B5A',
    selectbackground='#ffffff',
    selectforeground='#002B5A')
style.map('TCombobox',
    fieldbackground=[('readonly', '#ffffff')],
    foreground=[('readonly', '#002B5A')],
    selectbackground=[('readonly', '#ffffff')],
    selectforeground=[('readonly', '#002B5A')])

def show_quiz():
    """
    Switches from the tutorial screen to the quiz screen.
    Hides the tutorial frame and displays the quiz frame with all HP code labels and definition dropdowns.
    """
    tutorial_frame.pack_forget()
    quiz_frame.pack(expand=True, fill='both', anchor='center')

# Column headers
tk.Label(
    quiz_frame,
    text="HP Code",
    font=('Arial', 14, 'bold'),
    fg='#ffffff',
    bg='#002B5A').grid(row=0, column=0, sticky='w', pady=(0, 8))

tk.Label(
    quiz_frame,
    text="Definition",
    font=('Arial', 14, 'bold'),
    fg='#ffffff',
    bg='#002B5A').grid(row=0, column=1, sticky='w', padx=(20, 0), pady=(0, 8))

# Dictionary to store dropdown StringVars for each HP code
selected_answers = {}

# HP code labels and dropdowns
for i, item in enumerate(quiz_questions.keys()):

    style_name = f'Combo{i}.TCombobox'
    style.configure(style_name, fieldbackground='#ffffff', foreground='#002B5A')
    style.map(style_name,
    fieldbackground=[('readonly', '#ffffff')],
    foreground=[('readonly', '#002B5A')],
    selectbackground=[('readonly', '#ffffff')],
    selectforeground=[('readonly', '#002B5A')])


    # HP code labels
    hp_frame = tk.Frame(quiz_frame, bg="#080202")
    hp_frame.grid(row=i + 1, column=0, sticky='w', pady=3)
    tk.Label(
        hp_frame,
        text=item,
        font=('Arial', 10, 'bold'),
        bg='#ffffff',
        fg='#002B5A',
        width=26,
        pady=6,
        anchor='center').pack(pady=(0, 3))

    # StringVar to hold the player's selection for this dropdown
    var = tk.StringVar(value="Please select a definition...")
    selected_answers[item] = var

    # Dropdown populated with 1 correct and 5 random wrong answers
    dropdown = ttk.Combobox(
        quiz_frame,
        textvariable=var,
        style=style_name,
        values=quiz.prepare_options_for_definition_dropdown(item),
        state='readonly',
        width=75,
        height=50,
        font=('Arial', 11))
    dropdown.grid(row=i + 1, column=1, sticky='w', padx=(20, 0), pady=6)

# Bottom row for back link and submit button
bottom_row = tk.Frame(quiz_frame, bg='#002B5A')
bottom_row.grid(row=16, column=0, columnspan=2, sticky='ew', pady=(15, 0))

# Back to tutorial link
back_to_tutorial = tk.Label(
    bottom_row,
    text="< Take me back to the tutorial",
    font=('Arial', 11),
    fg='#FFE500',
    bg='#002B5A',
    cursor='hand2',
    justify='center')
back_to_tutorial.pack(side='left')
back_to_tutorial.bind('<Button-1>', lambda e: [
    quiz_frame.pack_forget(),
    tutorial_frame.pack(expand=True, fill='both', anchor='center')])
back_to_tutorial.bind('<Enter>', lambda e: back_to_tutorial.config(fg='#ffffff'))
back_to_tutorial.bind('<Leave>', lambda e: back_to_tutorial.config(fg='#FFE500'))

def on_submit():
    """
    Handles the Submit button click on the quiz screen.
    Calls is_complete to check all dropdowns have been answered, raising a ValueError and displaying an error messagebox if not.
    If complete, records all matches via attempt_match and switches to the results screen.
    """
    try:
        quiz.is_complete(selected_answers)
        for item, var in selected_answers.items():
            quiz.attempt_match(item, var.get())
        show_results()
    except ValueError as e:
        messagebox.showerror("Incomplete Quiz", str(e))

def on_submit_hover(e):
    """
    Changes the Submit button colour on hover.
    """
    submit_button.config(bg='#C7BB13')

def on_submit_leave(e):
    """
    Resets the Submit button colour when mouse leaves.
    """
    submit_button.config(bg='#FFE500', fg='#000000')

def on_submit_press(e):
    """
    Changes the Submit button colour on press.
    """
    submit_button.config(bg='#2F2A02', fg='#ffffff')

# Submit button sits on the right of the bottom row
submit_button = tk.Button(
    bottom_row,
    text="Submit",
    font=('Arial', 14, 'bold'),
    bg='#FFE500',
    fg='#000000',
    activebackground='#C7BB13',
    relief='groove',
    padx=10,
    pady=4,
    cursor='hand2',
    command=on_submit)
submit_button.pack(side='right')

submit_button.bind('<Enter>', on_submit_hover)
submit_button.bind('<Leave>', on_submit_leave)
submit_button.bind('<ButtonPress-1>', on_submit_press)

# ============================================================
# RESULTS SCREEN
# ============================================================

root.mainloop()