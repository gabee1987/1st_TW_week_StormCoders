from flask import Flask, url_for, request, render_template
from common import *

app = Flask(__name__)


@app.route("/question/<question_id>", methods=["GET"])
def show_id_question():
    """
        Shows a single question with all its answers,
        and all its data
    """
    answers = open_answer_file()
    questions = open_question_file()
    return render_template("question.html", answers=answers, questions=questions)

if __name__ == "__main__":
    app.run(debug=TRUE)
