import sqlite3
import json
import server

conn = sqlite3.connect("pythonExamDb.db")
cursor = conn.cursor()

def query_db(query, args=(), one=False):
    cursor.execute(query, args)
    r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
    conn.commit()
    return r;


def add_question_pyExam(quest):
    cursor.execute("INSERT INTO pyQuestionsMCQ(Question,AnsOpt1,AnsOpt2,AnsOpt3,AnsOpt4,Answer,Score) VALUES(?,?,?,?,?,?,?)",quest)
    conn.commit()

def view_questions_pyExam():
    cursor.execute('SELECT * FROM pyQuestionsMCQ')
    return cursor.fetchall()

def show_Quest_pyExam():
    my_query = query_db("SELECT * FROM pyQuestionsMCQ ORDER BY RANDOM() LIMIT ?", (3,), one=True)
    return my_query

def track_session(qList, request):
    session_data = server.get_session(request)
    print("\n\nsession data : {0}".format(session_data))
    # l = []
    # l.append(session_data["user_id"])
    # l.append(qList)    
    cursor.execute("INSERT INTO sessionTrack VALUES(?,?)",(session_data["user_id"],str(qList),))
 
def get_qlist(uid):
    cursor.execute("SELECT Qnos FROM sessionTrack WHERE Uid = ?",str(uid))
    return list(cursor.fetchone())

