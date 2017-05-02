"""
    Frequently used functions for the AskMate project.
    by StormCoders
"""


import csv
import random


def ID_generator(table):
    """
        Generates an ID for the questions and answers.
        The is unique in the list.
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


def open_file(answers=False):
    """
        Opens the specified file and
        reads its content as rows, return a list.
    """
    try:
        with open(answers, 'r') as workfile:
            row = workfile.readlines()
            table = [item.replace("\n", "").split(';') for item in row]
            return table
    except FileNotFoundError:
        table = None


def write_to_file(table, answers=False):
    """
        Saves data to the specified file.
        Write the data as rows.
    """
    with open(answers, 'w') as workfile:
        for item in stories:
            story = [element.strip("\n") for element in item]
            row = ';'.join(story)
            workfile.write(row + "\n")
