from flask import Flask, render_template
import csv
from common import *

'''
app = Flask(__name__)
'''


@app.route("/", methods=["POST", "GET"])
def home_list_handler():
    questions = open_file()
    table_headers = [
                    "#ID",
                    "Question",
                    "Submission time",
                    "Edit",
                    "Delete"
                    ]
    return render_template("home.html", questions=questions, table_headers=table_headers)

'''
if __name__ == '__main__':
    app.run(debug=True)
'''