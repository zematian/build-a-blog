from flask import flask, request ,redirect,render_template
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)
app.config['DEBUG'] =True
#Configuration that connect us to the database[Connection String]
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+pymsql://build-a-blog:kibreabkidane@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO']=True

#Creat a tie that binds all togehter and helps the variable to run in the database 
db = SQLAlchemy(app)
#Before we start testing we have to store some data to our database and the use we do that is by creating a persistance Class.
#Class that can be stored in the database and the class should extend the db.Model I am allowing my task to be related to the database using the Sql Alchemy

class Task(db.Model):
# We need to specify two things [id (primary key) and ]
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))

#Provide a Constractor should take the unique which is name
    def __init__(self, name):
       self.name = name 


tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():


    if request.method == 'POST':
        task = request.form['task']
        task.append(task)
    return render_template('todos.html',title="build a blog!", tasks=tasks)
# If we want to sheild the app command in python we have to use the following 

if __name__ == '__main__':

    app.run()
