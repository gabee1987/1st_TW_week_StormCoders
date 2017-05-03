from flask import Flask
from flask import render_template
from flask import Request
import time
from common import ID_generator, write_question_to_file

timestamp = int(time.time())

app = Flask(__name__)


@app.route('/question/new', methods=['POST'])
def new_question():
    """
    Add the new question to question.csv,
    and return to the home page.
    """
    datas = open_question_file()
    new_list = []
    new_list.append(ID_generator(datas))
    new_list.append(timestamp)
    question_attributes = ['title', 'message']
    for element in question_attributes:
        new_list.append(element)
    datas.append(new_list)
    write_question_to_file(datas)
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
