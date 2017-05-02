"""
    Frequently used functions for the AskMate project.
    by StormCoders
"""


import csv
import random


def ID_generator(table):
    """
        Generates an ID for the questions and answers.
        The id is unique in the database.
    """
    generated = table[0][0]
    char_list = [
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789",
        "!@#$%^&*()?=<>[]|+-/"
    ]
    while generated in [x[0] for x in table]:
        generated = ""
        for char in char_list:
            generated += "".join([random.choice(char) for _ in range(2)])
    generated = list(generated)
    random.shuffle(generated)
    return "".join(generated)


def open_question_file(filepath):
    """
        Opens the question.csv file,
        reads it content as rows.
    """
    filepath = QUESTION_FILE

    with open(filepath, 'r') as workfile:
        row = workfile.readlines()
        row["0"] = int(row["0"])
        table = [item.replace("\n", "").split(';') for item in row]
        return table


def open_answer_file(filepath):
    """
        Opens the question.csv file,
        reads it content as rows.
    """
    filepath = ANSWERS_FILE

    with open(filepath, 'r') as workfile:
        row = workfile.readlines()
        row["0"] = int(row["0"])
        table = [item.replace("\n", "").split(';') for item in row]
        return table


def write_question_to_file(table, filepath):
    """
        Saves data to the specified file.
        Write the data as rows.
    """
    filepath = QUESTION_FILE

    with open(answers, 'w') as workfile:
        for item in stories:
            story = [element.strip("\n") for element in item]
            row = ';'.join(story)
            workfile.write(row + "\n")


def write_answer_to_file(table, filepath):
    """
        Saves data to the specified file.
        Write the data as rows.
    """
    filepath = ANSWER_FILE

    with open(answers, 'w') as workfile:
        for item in stories:
            story = [element.strip("\n") for element in item]
            row = ';'.join(story)
            workfile.write(row + "\n")

