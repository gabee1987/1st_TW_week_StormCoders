"""
    Contain file paths, and data fields for AskMate project.
    by StormCoders
"""

QUESTION_FILE = "data/question.csv"
ANSWER_FILE = "data/answer.csv"
QUESTION_FIELDS = (
    "id",
    "submisson_time",
    "view_number"
    "vote_number"
    "title",
    "message"
    "image"
)
ANSWER_FIELDS = (
    "id",
    "submisson_time",
    "vote_number"
    "question_id"
    "message"
    "image"
)

ENCODE_QUESTION_FIELDS = (
    "title",
    "message",
    "image"
)

ENCODE_ANSWER_FIELDS = (
    "message",
    "image"
)





