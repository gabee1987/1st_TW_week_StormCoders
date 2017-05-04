"""
AskMate Q&A website
by StormCoders
"""
from flask import Flask, request, redirect, render_template
from common import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    table_headers = [
                    "#ID",
                    "Submission time",
                    "View number",
                    "Vote number",
                    "Title",
                    "Message"
                    ]
    list_of_questions = open_question_file()
    list_of_questions = data_sorting(list_of_questions, True)
    return render_template('home.html', table_headers=table_headers, list_of_questions=list_of_questions)


@app.route('/question/new', methods=['GET'])
def new_question():
    return render_template('question_form.html')


@app.route('/new_question', methods=['POST'])
def add_new_question():
    data = open_question_file()
    max_id = 0
    if len(data) > 0:
        max_id = max(int(i[0]) for i in data)
    current_time = str(int(time.time()))
    decoded_time = str(datetime.datetime.fromtimestamp(float(current_time)).strftime('%Y-%m-%d %H:%M:%S'))
    data.append([
                str(max_id+1),
                decoded_time,
                '0',
                '0',
                request.form['question_title'],
                request.form['question_message'],
                ])
    write_question_to_file(data)
    return redirect('/')


@app.route('/question/<q_id>', methods=['GET', 'POST'])
def display_question(q_id=None):
    list_of_questions = open_question_file()
    q_id = request.form["view_button"]
    current_question = []
    for row in list_of_questions:
        if row[0] == q_id:
            row[2] = str(int(row[2])+1)
            current_question.append(row[0])
            current_question.append(row[4])
            current_question.append(row[5])
            write_question_to_file(list_of_questions)
    answer_list = open_answer_file()
    current_answers = []
    for row in answer_list:
        if row[3] == q_id:
            current_answers.append(row)
    return render_template('question.html', q_id=q_id, current_question=current_question)


@app.route('/question/<q_id>/new-answer', methods=['GET', 'POST'])
def new_answer(q_id=0):
    return render_template('answer_form.html')


@app.errorhandler(404)
def page_not_found(error):
    return 'Oops, page not found!', 404


if __name__ == "__main__":
    app.run(debug=True)


