
import server
import db
import json

score=0
data = []

def showQuestionPost(request, response):
    score = 0
    global data
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
    return server.send_json_handler(request, response, data)
