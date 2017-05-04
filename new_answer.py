@app.route('/question/<q_id>/new-answer', methods=['POST'])
def add_new_answer(data, request, q_id=None):
    """
    Add the new answer to database.
    """
    q_id = request.form["new_comment"]
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
                q_id,
                request['answer_title'],
                request['answer_message']
                ])
    write_answer_to_file(data)
    return render_template('/question/<q_id>')
