"""
    Frequently used functions for the AskMate project.
    by StormCoders
"""


import csv
import random
import constants


def ID_generator():
    """
        Generates an ID for the questions and answers.
        The ID is unique in the database.
    """
    generated_q_ids = []
    generated_a_ids = []



def open_question_file(filepath):
    """
        Opens the question.csv file,
        reads it content as rows.
    """
    filepath = QUESTION_FILE
    decode = ENCODE_QUESTION_FIELDS

    with open(filepath, 'r') as workfile:
        reader = csv.DictReader(filepath, fieldnames=QUESTION_FIELDS, delimiter(','))
        row["0"] = int(row["0"])
        for field in decode:
            row[4][5] = base64.b64decode(row[field]).decode()
        table = [item.strip("\n").split(';') for item in row]
        return table


def open_answer_file(filepath):
    """
        Opens the answer.csv file,
        reads it content as rows.
    """
    filepath = ANSWERS_FILE
    decode = ENCODE_ANSWER_FIELDS

    with open(filepath, 'r') as workfile:
        row = workfile.readlines()
        row["0"] = int(row["0"])
        row[4:5] = base64.b64decode(row[field]).decode()
        table = [item.strip("\n").split(';') for item in row]
        return table


def write_question_to_file(table, filepath):
    """
        Saves question to the specified file.
        Write the data as rows.
    """
    filepath = QUESTION_FILE

    with open(answers, 'w') as workfile:
        for item in table:
            story = [element.strip("\n") for element in item]
            row = ';'.join(story)
            workfile.write(row + "\n")


def write_answer_to_file(table, filepath):
    """
        Saves answer to the specified file.
        Write the data as rows.
    """
    filepath = ANSWER_FILE

    with open(answers, 'w') as workfile:
        for item in table:
            story = [element.strip("\n") for element in item]
            row = ';'.join(story)
            workfile.write(row + "\n")

