import csv
import os

"""
file_handler.py - Handles reading and writing of quiz results to a csv file.

Provides functions to save a player's name and score after completing the quiz, and to load all previous results from the csv file.
"""

results_file = "quiz_results.csv"

def save_result(player_name, score, filepath=results_file):
    """
    Appends a player's name and score to the results csv file.
    Creates the file with a header row.

    Arguments:
        player_name (str): The validated name of the player.
        score (int): The number of correct matches made by the player.
        filepath (str): Path to the csv file. Defaults to results.csv.

    Raises:
        IOError: If the file cannot be written to.
    """
    try:
        file_exists = os.path.isfile(filepath)
        with open(filepath, 'a', newline='') as csvfile:
            fieldnames = ['name', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({'name': player_name, 'score': score})
    except IOError as e:
        raise IOError(f"Could not save result to file: {e}")
