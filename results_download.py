import csv
import os

"""
results_downloads.py - Handles reading and writing of quiz results to a csv file.

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

def load_results(filepath= "quiz_results.csv"):
    """
    Reads all previous results from the CSV file.
    Returns an empty list if the file does not exist.

    Arguments:
        filepath (str): Path to the csv file. Defaults to quiz_results.csv.

    Returns:
        list: A list of dictionaries, each with 'name' and 'score' keys.
              Returns an empty list if the file does not exist.

    Raises:
        IOError: If the file exists but cannot be read.
    """
    try:
        if not os.path.isfile(filepath):
            return []
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except IOError as e:
        raise IOError(f"Could not load results from file: {e}")
