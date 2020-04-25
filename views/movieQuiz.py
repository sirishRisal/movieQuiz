from flask import Blueprint,render_template,request,session
import json
from controller.movie import *
from database import *
import ast
from controller.roles import *


movieQuiz=Blueprint('movieQuiz', __name__)

@movieQuiz.route('/index',methods=['GET','POST'])
@roles_admin_user()
def index():
	scores=user_score()
	return render_template("index.html",scores=scores)


@movieQuiz.route('/quiz',methods=['GET','POST'])
@roles_user()
def quiz():
	if request.method=="POST":
		# data=json.loads(requests.data.content.decode('utf-8'))
		# data=requests.data.json()
		data = json.loads(request.data.decode('utf-8'))
		score=check_answer(data)
		print(score)
		session["score"]=score

		return {"status":"ok"}
		# print("sdfjsdlfksdjflksdjf",data)
	
	return render_template("takeQuiz.html")







@movieQuiz.route('/getQuizQuestion',methods=['GET',])
@roles_user()
def getQuizQuestion():
	if request.method=="GET":
		question=db_query().get_all("question")
		print (question,"qqqqqqqqqqqqqqqqqq")
		question=[{"options":ast.literal_eval(i["options"]),"id":i["id"],"question":i["question"] } for i in question]
		# question=(map(lambda x:(x["options"]),question))
		return json.dumps(question)
		# data=json.loads(requests.data.content.decode('utf-8'))
		# data=requests.data.json()
		# data = json.loads(request.data.decode('utf-8'))
		# print("sdfjsdlfksdjflksdjf",data)
	
	return render_template("takeQuiz.html")



@movieQuiz.route('/createquestions',methods=['GET','POST'])
@roles_admin()
def createquestions():
	if request.method=="POST":
		data = json.loads(request.data.decode('utf-8'))
		data
		check=db_query().get_one("question"," question='"+data["question"]+"'")
		# print (check)
		if check==None:
			res=insert_question(data)
			if res==True:
				return "Question set sccessfully"
		else:
			return "Question already set"
		
	return render_template("createQuestions.html")
