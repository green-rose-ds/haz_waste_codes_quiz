import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser
from PIL import Image, ImageTk
from quiz_logic import QuizLogic
from quiz_dictionary import quiz_questions, tutorial_questions
from results_download import save_result, load_results

"""
quiz_app.py - Main application file for the Hazardous Property (HP) Codes Quiz.

Builds and manages the Tkinter GUI including the welcome screen, tutorial screen, quiz screen, and results screen. 
Imports quiz logic from quiz_logic.py and data from quiz_dictionary.py.
Imports Pillow for ImageTk to position and size an image embedded in the GUI.
"""

root = tk.Tk()
root.option_add('*TCombobox*Listbox.font', ('Arial', 10))
root.title("Hazardous Property (HP) Codes Quiz")
root.geometry('900x700')
root.resizable(False, False)
root.configure(bg='#002B5A')

quiz = QuizLogic(quiz_questions)

# ============================================================
# WELCOME SCREEN
# ============================================================

welcome_frame = tk.Frame(root, 
                         bg='#002B5A', 
                         padx=60, 
                         pady=30, 
                         width=800)
welcome_frame.pack(expand=True, 
                   anchor='center')

"""
    Handles the player name entry.
    Hosts the player name entry box and Let's Begin button, which triggers validate_name on press.
"""

# Welcome title 
title_label = tk.Label(
    welcome_frame,
    text="Welcome to the Hazardous Property (HP) Codes Quiz!",
    font=('Courier New', 26, 'bold'),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=850,
    justify='left')
title_label.grid(row=0, 
                 column=0, 
                 columnspan=2, 
                 sticky='w', 
                 pady=(0, 8))

# Pulls in HW warning banner image
warning_img = Image.open('images/warning.png')
warning_img = warning_img.resize((325, 105))
warning_image = ImageTk.PhotoImage(warning_img)
warning_label = tk.Label(welcome_frame, 
                         image=warning_image, 
                         bg='#002B5A')
warning_label.image = warning_image
warning_label.grid(row=1, 
                   column=0, 
                   columnspan=2, 
                   pady=(0, 15), 
                   sticky='ew')
warning_label.configure(anchor="center")

# Quiz opening description
description_label = tk.Label(
    welcome_frame,
    text="In this quiz, you will match HP codes for hazardous classified waste to their corresponding definition.\n"
         "The aim is to support understanding of how we classify hazardous waste with codes according to the specific environmental or health risks that it poses.\n\n"
         "Please type your name below for your score to be saved -",
    font=('Courier New', 18),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=800,
    justify='center',
    anchor='center')
description_label.grid(row=2, 
                       column=0, 
                       columnspan=2, 
                       sticky='w', 
                       pady=(8, 15))

# Player name entry row
name_row = tk.Frame(welcome_frame, 
                    bg='#002B5A')
name_row.grid(row=3, 
              column=0, 
              columnspan=2, 
              sticky="w", 
              pady=(0, 10))

name_label = tk.Label(
    name_row,
    text="Player name:",
    font=('Courier New', 18, 'bold'),
    fg='#ffffff',
    bg='#002B5A')
name_label.pack(side="left", 
                pady=(5, 0))

name_entry = tk.Entry(
    name_row,
    font=('Courier New', 18),
    bg='#ffffff',
    fg="#000000",
    relief='sunken',
    width=25)
name_entry.pack(side="left", 
                pady=(2, 0), 
                padx=(10, 0))

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
    font=('Courier New', 14, 'bold'),
    bg='#FFE500',
    fg='#000000',
    activebackground="#ffffff",
    relief='groove',
    padx=8,
    pady=3,
    cursor='hand2',
    command=on_lets_go)
lets_go_button.grid(row=5, 
                    column=0, 
                    columnspan=2, 
                    pady=(20, 0))

lets_go_button.bind('<Enter>', on_hover)
lets_go_button.bind('<Leave>', on_leave)
lets_go_button.bind('<ButtonPress-1>', on_press)

# ============================================================
# TUTORIAL SCREEN
# ============================================================

tutorial_frame = tk.Frame(root, bg='#002B5A', 
                          padx=40, 
                          pady=20, 
                          width=800)

def show_tutorial():
    """
    Switches from the welcome screen to the tutorial screen.
    Hides the welcome screen, updates the title with the validated player name, and displays the tutorial screen.
    """
    welcome_frame.pack_forget()
    tutorial_title.config(
        text=f"Hello {quiz.player_name} 👋, after this quick tutorial you're ready to go!")
    tutorial_frame.pack(expand=True, 
                        fill='both', 
                        anchor='center')

# Tutorial title with updated player name in show_tutorial
tutorial_title = tk.Label(
    tutorial_frame,
    text="",
    font=('Courier New', 18, 'bold'),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=800,
    justify='left')
tutorial_title.grid(row=0, 
                    column=0, 
                    columnspan=2, 
                    sticky='w', 
                    pady=(0, 12))

# First instruction paragraph
tk.Label(
    tutorial_frame,
    text="On the next screen you will be shown 1 to 14 of the HP codes listed on the left. "
         "On the right you will see 14 aligned dropdown boxes.",
    font=('Courier New', 12),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=800,
    justify='left').grid(row=1, 
                         column=0, 
                         columnspan=2, 
                         sticky='w', 
                         pady=(0, 8))

def make_static_dropdown(parent, text, row, has_text=False):
    """
    Creates a static label styled to look like a dropdown box.
    Uses a frame with two labels to keep the arrow consistently
    aligned to the right regardless of text length.

    Args:
        parent: The parent widget to place the dropdown in.
        text (str): The text to display inside the dropdown.
        row (int): The grid row to place the dropdown on.
        has_text (bool): True if showing a pre-filled answer,
                         False for the default placeholder.
    """
    container = tk.Frame(
        parent,
        bg='#ffffff',
        bd=1,
        relief='sunken',
        width=500)
    container.grid(row=row, 
                   column=1, 
                   sticky='ew', 
                   padx=(20, 0), 
                   pady=3, 
                   ipady=6)
    container.grid_propagate(False)

    text_label = tk.Label(
        container,
        text=text,
        font=('Arial', 10),
        bg='#ffffff',
        fg='#002B5A' if has_text else '#808080',
        anchor='w',
        padx=5)
    text_label.pack(side='left', 
                    fill='x', 
                    expand=True)

    arrow_label = tk.Label(
        container,
        text="▼",
        font=('Arial', 10),
        bg='#ffffff',
        fg='#002B5A',
        padx=5)
    arrow_label.pack(side='right')

# Empty dropdowns in first demo section
for i, item in enumerate(tutorial_questions.keys()):
    hp_frame = tk.Frame(tutorial_frame, 
                        bg='#080202')
    hp_frame.grid(row=2 + i, 
                  column=0, 
                  sticky='w', 
                  pady=3)
    tk.Label(
        hp_frame,
        text=item,
        font=('Arial', 10, 'bold'),
        bg='#ffffff',
        fg='#002B5A',
        width=22,
        pady=6,
        anchor='center').pack(pady=(0, 3))
    make_static_dropdown(
        tutorial_frame,
        "Please select a definition...",
        2 + i,
        has_text=False)

# Second instruction paragraph
tk.Label(
    tutorial_frame,
    text="You will need to click to open the dropdown menu, you will be shown 6 options for the corresponding definition of the HP code to choose from.",
    font=('Courier New', 12),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=800,
    justify='left').grid(row=4, 
                         column=0, 
                         columnspan=2, 
                         sticky='w', 
                         pady=(12, 8))

# Open dropdown demo using a Frame with Labels
demo_outer = tk.Frame(tutorial_frame, 
                      bg='#002B5A')
demo_outer.grid(row=5, 
                column=0, 
                columnspan=2, 
                sticky='w', 
                pady=(0, 8))


# Demo section — HP code label
demo_hp_frame = tk.Frame(tutorial_frame, 
                         bg='#080202')
demo_hp_frame.grid(row=5, 
                   column=0, 
                   sticky='nw', 
                   pady=3)
tk.Label(
    demo_hp_frame,
    text=list(tutorial_questions.keys())[0],
    font=('Arial', 10, 'bold'),
    bg='#ffffff',
    fg='#002B5A',
    width=22,
    pady=6,
    anchor='center').pack(pady=(0, 3))

# Example open dropdown list
demo_options_frame = tk.Frame(tutorial_frame, 
                              bg='#ffffff', 
                              bd=1, 
                              relief='solid')
demo_options_frame.grid(row=5, 
                        column=1, 
                        sticky='w', 
                        padx=(20, 0), 
                        pady=3)

demo_options = [
    "Causes allergic reactions, affecting the skin or respiratory system",
    "Easily ignites, inc. liquids with flashpoint below 60°C, flammable gases, or solid waste",
    "Causes skin irritation or damage to the eyes upon contact",
    "Harm specific organs or cause toxic effects when inhaled or absorbed",
    "Causes severe health effects when ingested, inhaled, or through skin contact",
    "May show any of the hazardous properties, even if not initially present"]

for j, option in enumerate(demo_options):
    tk.Label(
        demo_options_frame,
        text=option,
        font=('Arial', 10),
        bg='#ffffff',
        fg='#002B5A',
        width=75,
        anchor='w',
        padx=8,
        pady=4).pack(fill='x')
    if j < len(demo_options) - 1:
        tk.Frame(demo_options_frame, 
                 bg='#e0e0e0', 
                 height=1).pack(fill='x')

# Third instruction paragraph with guidance link
tk.Label(
    tutorial_frame,
    text="I've completed the final 2 HP codes for you below as an example! "
         "If you want to brush up on waste classficiations first, please visit:",
    font=('Courier New', 12),
    fg='#ffffff',
    bg='#002B5A',
    wraplength=800,
    justify='left').grid(row=6, 
                         column=0, 
                         columnspan=2, 
                         sticky='w', 
                         pady=(12, 2))

guidance_link = tk.Label(
    tutorial_frame,
    text="Waste Classification Technical Guidance!",
    font=('Courier New', 12, 'underline'),
    fg='#FFE500',
    bg='#002B5A',
    cursor='hand2')
guidance_link.grid(row=7, column=0, columnspan=2, sticky='w', pady=(0, 8))
guidance_link.bind('<Button-1>', lambda e: webbrowser.open(
    "https://www.gov.uk/government/publications/waste-classification-technical-guidance"))
guidance_link.bind('<Enter>', lambda e: guidance_link.config(fg='#ffffff'))
guidance_link.bind('<Leave>', lambda e: guidance_link.config(fg='#FFE500'))

# Completed dropdowns in example section
for i, (item, answer) in enumerate(tutorial_questions.items()):
    hp_complete_frame = tk.Frame(tutorial_frame, 
                                 bg='#080202')
    hp_complete_frame.grid(row=8 + i, 
                           column=0, 
                           sticky='w', 
                           pady=3)
    tk.Label(
        hp_complete_frame,
        text=item,
        font=('Arial', 10, 'bold'),
        bg='#ffffff',
        fg='#002B5A',
        width=22,
        pady=6,
        anchor='center').pack(pady=(0, 3))
    make_static_dropdown(
        tutorial_frame,
        answer,
        8 + i,
        has_text=True)

# Bottom row
bottom_row = tk.Frame(tutorial_frame, 
                      bg='#002B5A')
bottom_row.grid(row=11, 
                column=0, 
                columnspan=2, 
                sticky='ew', 
                pady=(15, 0))

# Back to welcome screen link
back_to_welcome = tk.Label(
    bottom_row,
    text="< Take me back to the Welcome Screen",
    font=('Courier New', 13),
    fg='#FFE500',
    bg='#002B5A',
    cursor='hand2')
back_to_welcome.pack(side='left')
back_to_welcome.bind('<Button-1>', lambda e: [
    tutorial_frame.pack_forget(),
    welcome_frame.pack(expand=True, anchor='center')])
back_to_welcome.bind('<Enter>', lambda e: back_to_welcome.config(fg='#ffffff'))
back_to_welcome.bind('<Leave>', lambda e: back_to_welcome.config(fg='#FFE500'))

def on_lets_begin():
    """
    Switches from the tutorial screen to the main quiz screen.
    Hides the tutorial frame and calls show_quiz.
    """
    tutorial_frame.pack_forget()
    show_quiz()

def on_begin_hover(e):
    """Changes the Lets Go button colour on hover."""
    lets_begin_button.config(bg='#C7BB13')

def on_begin_leave(e):
    """Resets the Lets Go button colour when mouse leaves."""
    lets_begin_button.config(bg='#FFE500', 
                             fg='#000000')

def on_begin_press(e):
    """Changes the Lets Go button colour on press."""
    lets_begin_button.config(bg='#2F2A02', 
                             fg='#ffffff')

# Lets Go button
lets_begin_button = tk.Button(
    bottom_row,
    text="Lets Go! 🚀",
    font=('Courier New', 13, 'bold'),
    bg='#FFE500',
    fg='#000000',
    activebackground='#C7BB13',
    relief='groove',
    padx=10,
    pady=4,
    cursor='hand2',
    command=on_lets_begin)
lets_begin_button.pack(side='right')

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
    selectforeground='#002B5A',
    padding=(5, 5, 5, 5)),

style.map('TCombobox',
    fieldbackground=[('readonly', '#ffffff')],
    foreground=[('readonly', '#002B5A')],
    selectbackground=[('readonly', '#ffffff')],
    selectforeground=[('readonly', '#002B5A')])

def show_quiz():
    """
    Switches from the tutorial screen to the quiz screen.
    Hides the tutorial screen and displays the quiz screen with all HP code labels and definition dropdowns.
    """
    tutorial_frame.pack_forget()
    quiz_frame.pack(expand=True, 
                    fill='both', 
                    anchor='center')

# Column headers
tk.Label(
    quiz_frame,
    text="HP Code",
    font=('Courier New', 14, 'bold'),
    fg='#ffffff',
    bg='#002B5A').grid(row=0, 
                       column=0, 
                       sticky='w', 
                       pady=(0, 8))

tk.Label(
    quiz_frame,
    text="Definition",
    font=('Courier New', 14, 'bold'),
    fg='#ffffff',
    bg='#002B5A').grid(row=0, 
                       column=1, 
                       sticky='w', 
                       padx=(20, 0), 
                       pady=(0, 8))

# Dictionary to store dropdown StringVars for each HP code
selected_answers = {}

# HP code labels and dropdowns
for i, item in enumerate(quiz_questions.keys()):

    style_name = f'Combo{i}.TCombobox'
    style.configure(style_name, 
                    fieldbackground='#ffffff', 
                    foreground='#002B5A',
                    padding=(5, 5, 5, 5))
    style.map(style_name,
    fieldbackground=[('readonly', '#ffffff')],
    foreground=[('readonly', '#002B5A')],
    selectbackground=[('readonly', '#ffffff')],
    selectforeground=[('readonly', '#002B5A')])


    # HP code labels
    hp_frame = tk.Frame(quiz_frame, 
                        bg="#080202")
    hp_frame.grid(row=i + 1, 
                  column=0, 
                  sticky='w', 
                  pady=3)
    tk.Label(
        hp_frame,
        text=item,
        font=('Arial', 10, 'bold'),
        bg='#ffffff',
        fg='#002B5A',
        width=26,
        pady=5,
        anchor='center').pack(pady=(0, 2))

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
        width=76,
        font=('Arial', 10))
    dropdown.grid(row=i + 1, 
                  column=1, 
                  sticky='w', 
                  padx=(20, 0), 
                  pady=4)

# Bottom row for back link and submit button
bottom_row = tk.Frame(quiz_frame, 
                        bg='#002B5A')
bottom_row.grid(row=16, 
                column=0, 
                columnspan=2, 
                sticky='ew', 
                pady=(10, 0))

# Back to tutorial link
back_to_tutorial = tk.Label(
    bottom_row,
    text="< Take me back to the tutorial",
    font=('Courier New', 13),
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
    submit_button.config(bg='#FFE500', 
                         fg='#000000')

def on_submit_press(e):
    """
    Changes the Submit button colour on press.
    """
    submit_button.config(bg='#2F2A02', 
                         fg='#ffffff')

# Submit button
submit_button = tk.Button(
    bottom_row,
    text="Submit",
    font=('Courier New', 13, 'bold'),
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

results_frame = tk.Frame(root, bg='#002B5A', padx=40, pady=20, width=800)

def show_results():
    """
    Switches from the quiz screen to the results screen.
    Hides the quiz screen, saves the player's result to csv, and displays the results screen with a full breakdown of correct and incorrect answers.
    """
    quiz_frame.pack_forget()

    # Save result to csv
    try:
        save_result(quiz.player_name, quiz.get_score())
    except IOError as e:
        messagebox.showerror("Save Error", str(e))

    # Clear the screen
    for widget in results_frame.winfo_children():
        widget.destroy()

    # Results screen refresh
    build_results_screen()
    results_frame.pack(expand=True, fill='both', anchor='center')

def build_results_screen():
    """
    Builds all widgets for the results screen dynamically.
    Called each time from show_results to ensure the content reflects the current quiz session.
    """
    score = quiz.get_score()
    total = len(quiz_questions)
    summary = quiz.get_results_summary()


    # Score display
    tk.Label(
        results_frame,
        text=f"Well done {quiz.player_name}! You scored {score} out of {total}",
        font=('Courier New', 14, 'bold'),
        fg='#FFE500',
        bg='#002B5A',
        justify='left').pack(anchor='w', 
                             pady=(0, 14))

    # Column headers
    headers_frame = tk.Frame(results_frame, 
                             bg='#002B5A')
    headers_frame.pack(fill='x', pady=(0, 4))

    tk.Label(
        headers_frame,
        text="HP Code",
        font=('Courier New', 10, 'bold'),
        fg='#ffffff',
        bg='#002B5A',
        width=22,
        anchor='w').pack(side='left')

    tk.Label(
        headers_frame,
        text="Your Answer (green=correct, red=incorrect)",
        font=('Courier New', 10, 'bold'),
        fg='#ffffff',
        bg='#002B5A',
        width=40,
        anchor='w').pack(side='left', 
                         padx=(10, 0))

    tk.Label(
        headers_frame,
        text="Correct Answer",
        font=('Courier New', 10, 'bold'),
        fg='#ffffff',
        bg='#002B5A',
        width=38,
        anchor='w').pack(side='left', 
                         padx=(10, 0))

    # Separator line
    tk.Frame(
        results_frame,
        bg="#ffffff",
        height=1).pack(fill='x', 
                       pady=(0, 6))

    # Results rows
    for entry in summary:
        row_frame = tk.Frame(results_frame, 
                             bg='#002B5A')
        row_frame.pack(fill='x', pady=1)

        is_correct = entry['is_correct']
        row_bg = "#B7ECA9" if is_correct else "#DE8F8F"
        result_colour = '#4caf50' if is_correct else '#ff4444'

        # HP code
        hp_frame = tk.Frame(row_frame, 
                            bg='#080202')
        hp_frame.pack(side='left')
        tk.Label(
            hp_frame,
            text=entry['item'],
            font=('Arial', 9, 'bold'),
            bg='#ffffff',
            fg='#002B5A',
            width=25,
            pady=2,
            anchor='center').pack(pady=(0, 2))

        # Player's answer
        tk.Label(
            row_frame,
            text=entry['given_answer'],
            font=('Arial', 9),
            bg=row_bg,
            fg="#000000",
            width=45,
            pady=2,
            wraplength=290,
            justify='left',
            anchor='w',
            padx=5).pack(side='left', 
                         padx=(8, 0))

        # Correct answer
        tk.Label(
            row_frame,
            text=entry['correct_answer'],
            font=('Arial', 9),
            bg='#ffffff',
            fg='#000000',
            width=44,
            pady=2,
            wraplength=290,
            justify='left',
            anchor='w',
            padx=5).pack(side='left', 
                         padx=(10, 0), 
                         expand=True, 
                         fill='both')


    # Bottom row
    bottom_row = tk.Frame(results_frame, bg='#002B5A')
    bottom_row.pack(fill='x', 
                    pady=(12, 0))

    # Play again button
    def on_play_again():
        """
        Resets the quiz and returns the player to the welcome screen.
        Clears matched pairs and rebuilds the quiz frame for a fresh session.
        """
        quiz.matched_pairs = {}
        results_frame.pack_forget()
        welcome_frame.pack(expand=True, 
                           anchor='center')

    play_again_button = tk.Button(
        bottom_row,
        text="Play Again",
        font=('Courier New', 11, 'bold'),
        bg='#FFE500',
        fg='#120606',
        activebackground='#C7BB13',
        relief='groove',
        padx=10,
        pady=8,
        cursor='hand2',
        command=on_play_again)
    play_again_button.pack(side='right')
    play_again_button.bind(
        '<Enter>', lambda e: play_again_button.config(bg='#C7BB13'))
    play_again_button.bind(
        '<Leave>', lambda e: play_again_button.config(bg='#FFE500', 
                                                      fg='#000000'))
    play_again_button.bind(
        '<ButtonPress-1>', lambda e: play_again_button.config(
            bg='#2F2A02', fg='#ffffff'))

root.mainloop()