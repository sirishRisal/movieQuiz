from flask import Blueprint,render_template,request,session,redirect, url_for
from controller.login import *
import json
from database import *

loginModule=Blueprint('loginModule', __name__)


@loginModule.route('/',methods=['GET','POST'])
def login():
	if request.method=="POST":
		data = {"username":request.form['username'],"password":request.form['password']}
		check=validate_login(data)
		if check==True:
			return redirect(url_for("movieQuiz.index"))
		else:
			return render_template("login.html",info=check)
	if 'role' in session.keys():
		if session["role"]=="user":
			return redirect(url_for("movieQuiz.index"))
		elif session["role"]=="admin":
			return redirect(url_for("movieQuiz.createquestions"))
	return render_template("login.html",info="")



@loginModule.route('/register',methods=['GET','POST'])
def register():
	if request.method=="POST":
		data = json.loads(request.data.decode('utf-8'))
		register_reaponse=register_user(data)
		if register_reaponse==False:
			return "already"
		else:
			return register_reaponse
	return render_template("register.html")


@loginModule.route('/activate',methods=['GET'])
def activate():
	user = request.args.get('username')
	id = request.args.get('id')
	code = request.args.get('code')
	query=db_query().update("users","status='active'","id='"+id+"'")
	if query==True:
		return redirect(url_for("loginModule.login"))
	else:
		return render_template("login.html",info="contact admin or re-register")



@loginModule.route('/logout', methods=['GET','POST'])
def logout():
	print(session.keys())
	for i in list(session.keys()):
		session.pop(i)
	return redirect(url_for("loginModule.login"))


@loginModule.route('/error', methods=['GET','POST'])
def error():
	return render_template("error.html")
	