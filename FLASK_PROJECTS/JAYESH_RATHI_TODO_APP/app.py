# Importing Flask
from flask import Flask,render_template,request,redirect
# Import Database
from flask_sqlalchemy import SQLAlchemy
# Import Datetime module
from datetime import datetime

# Create an instance of this class
app = Flask(__name__) 

# Configure your Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Make Model of your Database
class ToDo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable = False)
    description = db.Column(db.String(500),nullable = False)
    date = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self):
        return f"{self.sno},{self.title},{self.description},{self.date}"

# Render html files----------------------->

# Routing for home page
@app.route('/', methods = ['GET','POST'])
def save_todo():
    if request.method == "POST":
        todo = ToDo(title = request.form["title"],description = request.form["desc"])
        db.session.add(todo)
        db.session.commit()
    all_todo = ToDo.query.all()
    return render_template("index.html",all_todo = all_todo)

# Routing for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Routing for delete todo
@app.route('/delete/<int:sno>')
def delete(sno):
    todo = ToDo.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

# Routing for update todo
@app.route('/update/<int:sno>',methods = ['GET','POST'])
def update(sno):
    todo = ToDo.query.filter_by(sno = sno).first()
    if request.method=="POST":
        todo.title = request.form['title']
        todo.description = request.form['desc']
        db.session.commit()
        return redirect('/')
    print(todo.description)
    return render_template('update.html',todo = todo)

if __name__ == "__main__":
    app.run(debug = True,port = 8000)