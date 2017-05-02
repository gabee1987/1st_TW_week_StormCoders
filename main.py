"""
AskMate Q&A website
by StormCoders
"""
from flask import Flask, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return "Index page with all questions."


@app.route('/question/new', methods=['GET', 'POST'])
def new_question():
    return 'New question form page.'


@app.route("/question/<q_id>")
def display_question(q_id=0):
    return "Display question with id"


@app.route('/question/<q_id>/new-answer', methods=['GET', 'POST'])
def new_answer(q_id=0):
    return "New answer to question with id"


@app.errorhandler(404)
def page_not_found(error):
    return 'Oops, page not found!', 404


if __name__ == "__main__":
    app.run(debug=True)


