import server
import uuid
import requests
import json
import admin
import user

def build_routes():
    server.add_route('get', '/login', login)
    server.add_route('post', '/login_success', login_success)
    server.add_route('get', '/admin', adminPage)
    server.add_route('get','/questions',questions)
    server.add_route('get', '/add-a-question', admin.add_a_question)
    server.add_route('post','/add-a-question', admin.add_a_question_post)
    server.add_route('get', '/view-questions', admin.view_questions)
    server.add_route('get', '/testPython', user.showQuestion)
    server.add_route('post', '/testPython', user.showQuestionPost)
    
def login(request, response):
    with open("./public/html/pyExamLogin.html", "rb") as file_descriptor:
            res = file_descriptor.read()
    return server.send_html_handler(request,response, res)

def login_success(request, response):
    csrf_guid = str(uuid.uuid4())
    account_kit_api_version = 'v1.0'
    app_id = '611513125703977'
    app_secret = 'c35593347c45e6047165f99811b39c6c'
    me_endpoint_base_url = 'https://graph.accountkit.com/v1.0/me'
    token_exchange_base_url = 'https://graph.accountkit.com/v1.0/access_token'
    token_exchange_url = token_exchange_base_url + '?grant_type=authorization_code&code='+request['content']['code']+'&access_token=AA|'+app_id+'|'+app_secret
    r = requests.get(token_exchange_url)
    rJson = json.loads(r.text)
    print("\n\nid: ",rJson['access_token'],"\n\n")
    me_endpoint_url = 'https://graph.accountkit.com/v1.0/me?access_token='+rJson['access_token']
    print(me_endpoint_url)
    s = requests.get(me_endpoint_url)
    sJson = json.loads(s.text)
    # print(sJson)
  #   res = """<head>
  # <title>Account Kit Python App</title>
  # </head>
  # <body>
  # <div>User ID: {0}</div>
  # <div>Phone: {1}</div>
  # <div>Access Token: {2}</div>
  # <div>Refresh Interval: {3}</div>
  # </body>""".format(rJson['id'],sJson['phone']['number'],rJson['access_token'],rJson['token_refresh_interval_sec'])
    with open("./public/html/index.html", "rb") as file_descriptor:
            res = file_descriptor.read()
    return server.send_html_handler(request,response, res)

    # return server.send_html_handler(request,response, res)

def questions(request, response):
    with open("./public/html/questions.html", "rb") as file_descriptor:
            res = file_descriptor.read()
    return server.send_html_handler(request,response, res)

def adminPage(request, response):
    with open("./public/html/pyAdmin.html", "rb") as file_descriptor:
            res = file_descriptor.read()
    return server.send_html_handler(request,response,res)

if __name__ == "__main__":
    build_routes()
    server.start_server("0.0.0.0", 5555)
