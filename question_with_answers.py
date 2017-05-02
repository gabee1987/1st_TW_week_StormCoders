from flask import Flask, url_for, request, render_template


app = Flask(__name__)


@app.route("/question/<question_id>", methods=["GET"])
def show_id_question(list, question_id):
    """
        Shows a single question with all its answers,
        and all its data
    """

    return render_template("question.html", question_id=question_id)
