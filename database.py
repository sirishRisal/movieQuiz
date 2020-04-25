import sqlite3
from sqlite3 import Error

import uuid
import random
from controller.security import *
ids=str(uuid.uuid4()).replace("-","")
code = random.randint(1111,9999)
stored_password=hash_password("admin")
insert_data={"username":"admin",
            "email":"admin@admin.com",
            "password":stored_password,
            "status":"active",
            "code":code,
            "role":"admin",
            "id":ids

            }


class Db_con():
	def __init__(self):
		self.db_file ="mysqlite.db"

	def conn_object(self):
		conn = None
		try:
			conn = sqlite3.connect(self.db_file)
			conn = conn.cursor()
			return conn
		except Error as e:
		    print(e)
		return conn

	def query_field(self):
		self.sql_users = """ CREATE TABLE IF NOT EXISTS users (
		                                    id text PRIMARY KEY,
		                                    username text NOT NULL,
		                                    code integer NOT NULL,
		                                    email text NOT NULL,
		                                    password text NOT NULL,
		                                    role text NOT NULL,
		                                    status text NOT NULL
		                                ); """

		self.sql_scores = """ CREATE TABLE IF NOT EXISTS scores (
		                                        id text PRIMARY KEY,
		                                        scores text NOT NULL,
		                                        score_date text NOT NULL,
		                                        user_id text NOT NULL,
		                                        FOREIGN KEY (user_id) REFERENCES users (id)
		                                    ); """

		self.sql_question = """CREATE TABLE IF NOT EXISTS question (
		                                id text PRIMARY KEY,
		                                question integer NOT NULL,
		                                answer text NOT NULL,
		                                options text NOT NULL
		                                ); """
	  
	def create_table(self):
	    try:
	        self.conn.execute(self.sql_users)
	        self.conn.execute(self.sql_scores)
	        self.conn.execute(self.sql_question)
	        c=self.conn.execute('''SELECT COUNT(*) from users ''')
	        result=c.fetchall()
	        if result[0][0]==0:
	        	db_query().insert("users",insert_data)

	        return "ok"
	    except Error as e:
	        print(e)


	def main(self):
		print (self.db_file)
		self.conn=self.conn_object()
		x=self.query_field()
		if self.conn is not None:
			result=self.create_table()
			return result
		else:
		    print("Error! cannot create the database connection.")


class db_query(object):
	
	def __init__(self):
		self.db=sqlite3.connect('mysqlite.db')
		self.cur=self.db.cursor()
		print(self.cur)
		
		
	def insert(self,table_name,data):
		try:
			columns = ', '.join(data.keys())
			placeholders = ':'+', :'.join(data.keys())
			query = 'INSERT INTO '+table_name+' (%s) VALUES (%s)' % (columns, placeholders)
			self.cur.execute(query, data)
			self.db.commit()
			return True
		except Exception as e:
			print(e)
			self.db.rollback()
			return False


	def get_all(self,table_name):
		try:
			conn = self.db
			conn.row_factory = sqlite3.Row
			c = conn.cursor()
			c.execute('select * from '+table_name+'')
			result = [dict(row) for row in c.fetchall()]
			return result
		except Exception as e:
			print(e)
			print ("error in operation")
			return None

	def get_all_with_condition(self,table_name,condition):
		try:
			conn = self.db
			conn.row_factory = sqlite3.Row
			c = conn.cursor()
			c.execute('select * from '+table_name+' where '+condition+'')
			result = [dict(row) for row in c.fetchall()]
			return result
		except Exception as e:
			print(e)
			print ("error in operation")
			return None

	def get_one(self,table_name,condition):
		try:
			conn = self.db
			conn.row_factory = sqlite3.Row
			c = conn.cursor()
			c.execute("select * from "+table_name+" where "+condition+"")
			result = [dict(row) for row in c.fetchall()][0]
			return result
		except Exception as e:
			print(e)
			print ("error in operation")
			return None
		
	def update(self,table_name,attribute,condition):
		try:
			query="UPDATE "+table_name+" SET "+attribute+"  WHERE "+condition+""
			self.cur.execute(query)
			self.db.commit()
			return True
			
		except Exception as e:
			print(e)
			print ("error in operation")
			return None
# UPDATE table_name
# SET column1 = value1, column2 = value2...., columnN = valueN
# WHERE [condition];


# UPDATE employees
# SET lastname = 'Smith'
# WHERE employeeid = 3;		

# print(db_query().update("users","status='active'","id='825b98e1972f4986a1d68d14a9171137'"))
# conn = create_connection(database)
# sql = ''' UPDATE users
#           SET status = active ,
              
#           WHERE id = 825b98e1972f4986a1d68d14a9171137'''
# cur = conn.cursor()
# cur.execute(sql, task)
# conn.commit()






# my_dict = {'username':'jack', 'id':"aklsshasdkj", 'code':'1245', 'email':"sasd@gmail.com",'password':"pas",'status':'deactive'}
# print(db_query().insert("users",my_dict))
# print(db_query().get_all("users"))

# print(db_query().get_one("users","id='825b98e1972f4986a1d68d14a9171137'"))

