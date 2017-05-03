from flask import Flask, render_template
import csv
from common import *
import time
timestamp = int(time.time())

'''
app = Flask(__name__)
'''


@app.route("/", methods=["GET"])
def home_list_handler():
    questions = open_question_file()
    table_headers = [
                    "#ID",
                    "Submission time",
                    "View number"
                    "Vote number"
                    "Title",
                    "Message"
                    ]
    return render_template("home.html", questions=questions, table_headers=table_headers)


'''
if __name__ == '__main__':
    app.run(debug=True)
'''