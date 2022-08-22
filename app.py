from flask import Flask,render_template,request

from flask_sqlalchemy import SQLAlchemy

from wtform_field import *
import models.py


app=Flask(__name__)

app.secret_key= 'replace later'
app.config['SQLAlchemy_DATABASE_URI']='postgres://usznvsgptebxwh:ef9d76be3ccacf97c67cb09055ff68051d928777bac09af5b1be5a6145d9b8dd@ec2-34-199-68-114.compute-1.amazonaws.com:5432/d5kvm0bvl9bmjq'
db=SQLAlchemy(app)




@app.route("/",methods=['get','post'])
def index():
    
    reg_form = RegistartionForm()
    if reg_form.validate_on_submit():
        username=reg_form.username.data
        password=reg_form.password.data

        user_object=User.query.filter_by(username=username).first()
        if user_object:
            return "someone else taken this username"


        user=User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return "inserted into db!"    
    
    return render_template("index.html",form=reg_form)


if __name__=="__main__":
    app.run(debug=True)
