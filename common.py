"""
    Frequently used functions for the AskMate project.
    by StormCoders
"""


import csv
import random
import constants
import base64


def ID_generator():
    """
        Generates an ID for the questions and answers.
        The ID is unique in the database.
    """
    generated_q_ids = []
    generated_a_ids = []


def open_question_file():
    """
        Opens the question.csv file,
        reads it content as rows.
    """
    filepath = QUESTION_FILE
    fields = QUESTION_FIELDS
    decode = ENCODE_QUESTION_FIELDS

    data = dict()
    with open(filepath) as workfile:
        reader = csv.DictReader(filepath, fieldnames=fields, delimiter(','))
        for row in reader:
                row['id'] = int(row['id'])
                for field in decode:
                    base64_decoded = base64.b64decode(row[field])
                    byte_like_decoded = base64_decoded.decode('utf_8')
        return data


def open_answer_file():
    """
        Opens the answer.csv file,
        reads it content as rows.
    """
    filepath = ANSWERS_FILE
    fields = ANSWER_FIELDS
    decode = ENCODE_ANSWER_FIELDS

    data = dict()
    with open(filepath) as workfile:
        reader = csv.DictReader(filepath, fieldnames=fields, delimiter(','))
        for row in reader:
                row['id'] = int(row['id'])
                for field in decode:
                    base64_decoded = base64.b64decode(row[field])
                    byte_like_decoded = base64_decoded.decode('utf_8')
        return data


def write_question_to_file(data, filepath):
    """
        Saves question to the specified file.
        Write the data as rows.
    """
    filepath = QUESTION_FILE
    fields = QUESTION_FIELDS
    encode = ENCODE_QUESTION_FIELDS

    with open(filepath, 'w') as workfile:
        writer = csv.DictWriter(filepath, fieldnames=fields, delimiter=',')
        for row in data:
            for field in encode:
                byte_like_encoded = data[row][field].encode('utf_8')
                base64_encoded = base64.b64encode(byte_like_encoded)
            writer.writerow(data[row])


def write_answer_to_file(data, filepath):
    """
        Saves answer to the specified file.
        Write the data as rows.
    """
    filepath = ANSWERS_FILE
    fields = ANSWER_FIELDS
    encode = ENCODE_ANSWER_FIELDS

    with open(filepath, 'w') as workfile:
        writer = csv.DictWriter(filepath, fieldnames=fields, delimiter=',')
        for row in data:
            for field in encode:
                byte_like_encoded = data[row][field].encode('utf_8')
                base64_encoded = base64.b64encode(byte_like_encoded)
            writer.writerow(data[row])

