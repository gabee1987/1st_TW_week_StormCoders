from flask import Flask
from flask import render_template
from flask import Request


app = Flask(__name__)


@app.route('/question/new', methods=['POST'])
def new_question():
    """
    Add the new question to question.csv,
    and return to the home page.
    """
    stories = openfile()
    new_list = []
    new_list.append(0, ID_generator(stories))
    return

if __name__ == '__main__':
    app.run()