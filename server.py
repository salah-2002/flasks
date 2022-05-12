
from flask_sqlalchemy import SQLAlchemy
from flask import Flask , render_template, request
import datetime


app=Flask(__name__,template_folder='template')
date=datetime.datetime.now().date()

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///store.db'
db=SQLAlchemy(app)

class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    titre=db.Column(db.String(20),nullable=False)
    description=db.Column(db.String(100),nullable=False)
    image=db.Column(db.String(20),nullable=False)

class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(20),nullable=False)
    mail=db.Column(db.String(100),nullable=False)
    message=db.Column(db.String(20),nullable=False)

products=Products.query.all()
messages=[]

@app.route("/")
def home():
    return render_template("home.html",date=date,prods=products,title="home")
@app.route("/about")
def abou():
    return render_template("about.html",date=date,title='about')

@app.route("/contact",methods=['GET','POST'])
def cont():
    valid=False
    messages=Message.query.all()
    if request.method=='POST':
        nom=request.form.get('nom')
        mail=request.form.get('mail')
        message=request.form.get('message')
        msg=Message(nom=nom,mail=mail,message=message)
        db.session.add(msg)
        db.session.commit()
        valid=True
    messages=Message.query.all()
    return render_template("contact.html",date=date,title='contact',valid=valid,messages=messages)
if __name__=="__main__":
    app.run(debug=True)