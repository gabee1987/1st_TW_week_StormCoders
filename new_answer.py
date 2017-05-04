@app.route('/new_answer', methods=['POST'])
def add_new_answer(data, request):
    """
    Add the new answer to database.
    """
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
                request['answer_title'],
                request['answer_message']
                ])
    return data
