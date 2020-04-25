
from flask import Flask
from views.login import *
from views.movieQuiz import *
from database import *


app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(loginModule)
app.register_blueprint(movieQuiz)




if __name__ == '__main__':
    Db_con().main()
    app.run(debug=True)