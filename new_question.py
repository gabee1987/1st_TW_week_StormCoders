from common import *


"""def add_new_question(data, request):
    
    Add the new question to database.
    
    max_id = 0
    if len(data) > 0:
        max_id = max(int(i[0]) for i in data)
    data.append([
                str(max_id+1),
                time_stamp_encode(),
                '0',
                '0',
                request['question_title'],
                request['question_message'],
                ''
                ])
    return data
"""