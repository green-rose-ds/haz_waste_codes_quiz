# haz_waste_codes_quiz
A quiz to match up the descriptions of Hazardous Waste codes to their description, built using Tkinter in Python for IFCS Summative 2

## 1. Introduction

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
- re
- Pillow
  
**Apps/Tools**
- Figma
- io.draw
- VS Codes
- Github

### Code Design

## 3. Development Section

## 4. Testing Section


## 5. Documentation Section (User and Technical)


## 6. Evaluation Section

