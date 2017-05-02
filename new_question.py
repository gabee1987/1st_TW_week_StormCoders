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
    datas = openfile()
    new_list = []
    new_list.append(0, ID_generator(datas))
    question_attributes = ['id', 'submisson_time', 'title', 'message']
    for element in question_attributes:
        new_list.append(element)
    datas.append(new_list)
    write_to_file(datas)
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
