from flask import Flask, render_template
import csv
from common import *


@app.route("/list", methods=["POST", "GET"])
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
