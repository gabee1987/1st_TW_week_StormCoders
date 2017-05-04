@app.route('/new_answer', methods=['POST'])
def add_new_answer(data, request):
    """
    Add the new answer to database.
    """
    max_id = 0
    if len(data) > 0:
        max_id = max(int(i[0]) for i in data)
    data.append([
                str(max_id+1),
                time_stamp_encode(),
                '0',
                '0',
                request['answer_title'],
                request['answer_message'],
                ''
                ])
    return data
