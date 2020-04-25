from controller.security import *
import random
import uuid
from controller.smtp import mail_verification_code
from database import db_query
from flask import session,redirect, url_for

def register_user(data):
    username=data["username"].strip()
    password=data["password"].strip()
    user_data=db_query().get_one("users","username='"+data["username"].strip()+"'  or email='"+data["email"].strip()+"'")
    if user_data==None:
        ids=str(uuid.uuid4()).replace("-","")
        code = random.randint(1111,9999)
        stored_password=hash_password(password)
        insert_data={"username":username,
                    "email":data["email"].strip(),
                    "password":stored_password,
                    "status":"deactive",
                    "code":code,
                    "role":"user",
                    "id":ids

                    }
        link="http://127.0.0.1:5000/activate?id="+ids+"&code="+str(code)+""
        insert_in_db=db_query().insert("users",insert_data)
        if insert_in_db:
            return link
            # try:
            #     # mail_verification_code(link,data["email"])
            #     return True
            # except Exception as e:
            #     raise e
            #     return False
        else:
            return False
    else:
        return False



def validate_login(data):
    user_data=db_query().get_one("users","username='"+data["username"].strip()+"' or email='"+data["username"].strip()+"'")
    if user_data==None:
        return "username not found"
    elif user_data!=None:
        if user_data["status"]=="active":
            print ("active")
            if user_data["username"]==data["username"] and verify_password(user_data["password"],data["password"]) or user_data["email"]==data["username"] and verify_password(user_data["password"],data["password"]):
                print ("matched")
                session['id']=user_data["id"]
                session['role']=user_data["role"]
                session['username']=user_data["username"]
                session['email']=user_data["email"]
                return True
            else:
                return "invalid user"
        else:
            return "You are not active"
#    