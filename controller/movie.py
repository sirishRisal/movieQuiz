import json
import uuid
from datetime import datetime
from database import *
from flask import session
import pandas as pd

def insert_question(data):
	ids=str(uuid.uuid4()).replace("-","")
	data["id"]=ids
	data["options"]=str(data["options"])
	print (data)
	insert_in_db=db_query().insert("question",data)
	return insert_in_db


# {'answer': 'glass', 'options': ['glass', 'water'], 'question': 'what isthis?'}


def check_answer(ans):
	score=0
	for i in ans:
		check=db_query().get_one("question","id='"+i["questionId"]+"' and answer='"+i["answer"]+"'")
		print (check)
		if check==None:
			pass
		else:
			score+=10
	print (session)			
	ids=str(uuid.uuid4()).replace("-","")
	now=datetime.now()
	dt=now.strftime("%Y-%m-%d %H:%M")
	scores={"id":ids,"scores":score,"score_date":dt,"user_id":session["id"]}
	set_score=db_query().insert("scores",scores)
	if set_score:
		return scores
	else:
		return "try again"
	# print (sdkjfsdf)



def user_score():
	query=db_query().get_all_with_condition("scores","user_id!='"+session["id"]+"'")
	print (len(query),"sadasdaqqqqqqqqqqqqqqqqqqqq")
	if len(query)!=0:
		scores=pd.DataFrame(query)
		# scores=pd.DataFrame(db_query().get_all("scores"))
		# scores=(scores.groupby(["user_id"]).scores.agg(['max']).date.agg(['sum']).to_dict())
		aggregation_functions = {"score_date":"first","scores":"first","user_id":"first"}
		aggregated_score = list(scores.groupby(scores['user_id']).aggregate(aggregation_functions).T.to_dict().values())
		# print(list(df_new))
		user_score_data=[]
		for i in aggregated_score:
			user_data=(db_query().get_one("users","id='"+i['user_id']+"'"))
			score_data={"username":user_data["username"],"email":user_data["email"],"date":i['score_date'],"score":i['scores']}
			user_score_data.append(score_data)
		print (user_score_data,"ssssssssssss")
		return user_score_data
	return []