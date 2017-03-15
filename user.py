import server
import db
import json

score=0
data = []

def showQuestionPost(request, response):
    score = 0
    flag = 0
    global data
    session_data = server.get_session(request)
    que_list = db.get_qlist(session_data["user_id"])
    for qno in list(request['content'].keys()):
        if qno not in que_list:
            flag = 1
    if flag == 1:
        return server.send_html_handler(request, response, str(-1))
    for qno in list(request['content'].keys()):
        for q in data:
            if str(q['QNo'])==qno:
                if str(q['Answer'])==request['content'][qno]:
                    score+=q["Score"]
    print("\n\nScore : {0}".format(score))
    return server.send_html_handler(request, response, str(score))

def showQuestion(request, response):
    global data
    data = db.show_Quest_pyExam()
    qno_list = []
    que_list = []
    for i in data:
        que_dict = {}
        for j in i:
            if j!='Answer' and j!='Score':
                que_dict[j]=i[j]
            if j=='QNo':
                qno_list.append(i[j])
        que_list.append(que_dict)
    db.track_session(qno_list, request)
    return server.send_json_handler(request, response, que_list)
