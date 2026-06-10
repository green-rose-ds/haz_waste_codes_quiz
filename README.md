# haz_waste_codes_quiz
A quiz to match up the descriptions of Hazardous Waste codes to their description, built using Tkinter in Python for IFCS Summative 2

## 1. Introduction
My workplace of the Environment Agency (EA) is a non-departmental public body, who are responsible for protecting and improving the environment across England. One of its core functions is waste regulation, which involves ensuring that businesses and organisations handle, classify, and dispose of waste in accordance with legislation.

Hazardous waste classification is governed by the Hazardous Waste Regulations 2005, key to these are the Hazardous Property (HP) codes, these are a standardised set of 16 codes defining the specific properties that make a waste hazardous. The codes and their definitions and their appropriate uses are outlined in the GOV.UK https://www.gov.uk/government/publications/waste-classification-technical-guidance, of which the  managedbasis of my quiz is based on. The correct application of HP codes to waste is very important to how that waste is managed and disposed of, and misclassification can result in hazardous waste being managed inappropriately, posing significant risks to human health and the environment.

For staff working in Waste Regulation, or the waste industry in general, having a sound working knowledge of the HP code framework is beneficial. There is currently no dedicated interactive tool to support this, Typically, written guidance and on-the-job experience  is relied on for understand about HP codes.
The proposed Minimum Viable Product (MVP) is a quiz application built in Python, designed to support developing familiarity with HP codes and their corresponding definitions. Presenting the codes in an interactive format provides an engaging, self-directed learning tool that reinforces understanding in a practical and fun way, supporting teams to maintain sounds knowledge of the codes.

## 2. Design Section
### GUI Design

### Requirements

**Functional Requirements**

| ID  | Requirement Specification                                                                                                                       |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|
| F1  | The GUI will display a name entry screen before the quiz begins                                                                                 |
| F2  | The app logic must validate the player's name, against the below criteria and display an appropriate error message if invalid:                  |
| F2.1|  - Name cannot be blank                                                                                                                         |
| F2.2|  - Name is between 2 and 20 characters                                                                                                          | 
| F2.3|  - Name is made up of correct characters (letters and valid punctuation) only                                                                   |
| F3  | The GUI will display the predefined 16 Hazardous Waste codes, and 16 corresponding descriptions, in two separate columns                        |
| F4  | The app logic must shuffle the descriptions into a random order each time the quiz loads                                                        |
| F5  | The GUI will allow the player to select one Hazardous Waste code in the left column, and one description in the right column, to create a match |
| F6  | The GUI will visually connect the player's matched pairs with a line between them                                                               |
| F7  | The GUI must allow the player to change a match before final submission                                                                         |
| F8  | The app logic must check all 16 matches against the correct Hazardous Waste code descriptions upon submission                                   |
| F9  | The GUI will display the player's results back to them, showing which of their matches were correct and incorrect                               |
| F10 | The GUI will display the player's final score                                                                                                   |
| F11 | The app logic must save the player's name and score to a persistent csv file following completion of the quiz                                   |
| F12 | The app logic must append to the csv and not overwrite it so as to record and preserve all results                                              |


**Non-functional Requirements**

| ID  | Requirement Specification                                                                                                                       |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|
| F1  | The GUI will display a name entry screen before the quiz begins                                                                                 |
| F2  | The app logic must validate the player's name, against the below criteria and display an appropriate error message if invalid:                  |
| F2.1|  - Name cannot be blank                                                                                                                         |
| F2.2|  - Name is between 2 and 20 characters                                                                                                          | 
| F2.3|  - Name is made up of correct characters (letters and valid punctuation) only                                                                   |
| F3  | The GUI will display the predefined 16 Hazardous Waste codes, and 16 corresponding descriptions, in two separate columns                        |
| F4  | The app logic must shuffle the descriptions into a random order each time the quiz loads                                                        |
| F5  | The GUI will allow the player to select one Hazardous Waste code in the left column, and one description in the right column, to create a match |
| F6  | The GUI will visually connect the player's matched pairs with a line between them                                                               |
| F7  | The GUI must allow the player to change a match before final submission                                                                         |
| F8  | The app logic must check all 16 matches against the correct Hazardous Waste code descriptions upon submission                                   |
| F9  | The GUI will display the player's results back to them, showing which of their matches were correct and incorrect                               |
| F10 | The GUI will display the player's final score                                                                                                   |
| F11 | The app logic must save the player's name and score to a persistent csv file following completion of the quiz                                   |
| F12 | The app logic must append to the csv and not overwrite it so as to record and preserve all results                                              |

### Tech Stack Outline
**Languages**
- Python
- Github flavoured Markdown
  
**Libraries**
- Tkinter
- csv
- Pytest
- Random
- webbrowser
- regex
- Pillow
- os
  
**Apps/Tools**
- Figma
- io.draw
- VS Codes
- Github

### Code Design

## 3. Development Section

The application is structured across four Python files: `quiz_dictionary.py` for data, `quiz_logic.py` for game logic, `results_download.py` for csv persistence, and `quiz_app.py` for the GUI. This separation ensures logic remains independently testable.

**Data: `quiz_dictionary.py`**/n
The quiz content is stored in two dictionaries, `quiz_questions` contains the 14 HP codes used in the quiz, and `tutorial_questions` holds the remaining two codes used as static examples on the tutorial screen:

```
quiz_questions = {
    "HP_1 Explosive": "Cause dangerous chemical reactions that can damage surroundings",
    ...}

tutorial_questions = {
    "HP_15": "May show any of the hazardous properties, even if not initially present",
    "HP_POP": "Contains persistent organic pollutants above the concentration limit"}
```

**Logic: `quiz_logic.py`**/n
This file contains the standalone pure function `validate_name` and the `QuizLogic` class. By keeping all logic independent of Tkinter every function is directly testable with Pytest.
The `validate_name` function strips spaces, converts to title case, and applies four validation rules, returning a (bool, str) tuple in all cases so the GUI can display whichever error message is relevant without:
```
def validate_name(name):
    name = name.strip().title()
    if len(name) == 0:
        return False, "Player name cannot be empty"
    if not re.fullmatch(r'[a-zA-Z\s\-]+', name):
        return False, "Player name can only contain letters, hyphens, and spaces"
    return True, name
```
`QuizLogic` manages all session states, within it the `prepare_options_for_definition_dropdown` method generates six answer options per HP code, which includes the correct definition plus five randomly sampled incorrect ones. The `is_complete` method checks whether any dropdowns still hold the default placeholder, raising a ValueError if so. The `get_results_summary` method returns a list of dictionaries containing each item, the player's answer, the correct answer, and a boolean for the results screen to consume.

**Persistence: `results_download.py`**/n
The 'save_result' function appends the player's name and score to a csv file, creating it with a header row first time. The filepath parameter defaults to 'quiz_results.csv' but can be overridden for testing:
```
def save_result(player_name, score, filepath=RESULTS_FILE):
    try:
        file_exists = os.path.isfile(filepath)
        with open(filepath, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'score'])
            if not file_exists:
                writer.writeheader()
            writer.writerow({'name': player_name, 'score': score})
    except IOError as e:
        raise IOError(f"Could not save result to file: {e}")
```

**GUI: `quiz_app.py`**/n
The GUI is structured across four screens consisting of welcome, tutorial, quiz, and results. Each has a `tk.Frame` shown or hidden using `.pack()` and `.pack_forget()`. On the quiz screen, each HP code is displayed alongside a `ttk.Combobox` populated with six options from `prepare_options_for_definition_dropdown`, with each selection stored in a `tk.StringVar` in the `selected_answers` dictionary. On submission, `on_submit` calls `quiz.is_complete(selected_answers)` inside a `try/except` block. If it completes, it records all matches and navigates to the results screen and if not, it displays an error messagebox:
```
def on_submit():
    try:
        quiz.is_complete(selected_answers)
        for item, var in selected_answers.items():
            quiz.attempt_match(item, var.get())
        show_results()
    except ValueError as e:
        messagebox.showerror("Incomplete Quiz", str(e))
```
The results screen is refreshed on each call to `show_results`, ensuring a second attempt always reflects the current session rather than the previous one.

## 4. Testing Section

### 4.1.Testing methodology

Two testing approaches are use, automated unit testing with Pytest for all pure functions with and manual testing for the GUI behaviour and player journey.
Automated unit testing was prioritised for `quiz_logic.py`, `quiz_dictionary.py`, and `results_download.py` because these modules contain pure functions that take defined inputs and return consistent outputs, making them straightforward to test in isolation. Pytest was chosen as the testing framework due to its simple syntax and output. Test-driven development (TDD) was followed where possible, so tests were written before their corresponding functions, ensuring each function was designed as testable from the outset.
Manual testing was used for all GUI behaviour as Tkinter widgets cannot be instantiated in a test environment without a display. This covered navigation between screens, styling, dropdown behaviour, and error handling.

**4.1.1. Manual Testing Outcomes**

**4.1.2. Unit Testing Outcomes**
17 unit tests are written for the testable modules, all of which pass successfully with the final version of the app.

/haz_waste_codes_quiz/main/assets/images/unit_test_outcome.png

Key test cases include validating that:
- `validate_name` correctly rejects empty strings, numeric characters, and names outside the length requirments.
- `prepare_options_for_definition_dropdown` always includes the correct answer, returns exactly 6 options, and contains no duplicates
-  `is_complete` raises a ValueError when unanswered dropdowns are present.
-  Tests for the csv file handler `results_download.py` use Pytest's built-in `tmp_path` to write to a temporary file, keeping the real `quiz_results.csv` unaffected for testing.


## 5. Documentation Section (User and Technical)

### 5.1. Technical Documentation
System requirements: Windows, Mac, or Linux with Python 3.14 installed with a virtual environment activated.

**Starting the application:**
1. Open a terminal and navigate to the project folder haz-waste-codes-quiz
2. Once in the project folder, activate the virtual environment: 
- Windows - `.venv\Scripts\activate`
- Mac/Linux - `source .venv/bin/activate`
   
**Run the application:**
 `python quiz_app.py`

**Installing dependencies:**
- python `-m pip install Pillow`
- python `-m pip install pytest`

**Running tests:**
- python `-m pytest test_quiz_app.py`

### 5.12 User Documentation


## 6. Evaluation Section

