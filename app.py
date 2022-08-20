from crypt import methods
from flask import Flask,render_template,request


from wtform_field import *

app=Flask(__name__)

app.secret_key= 'replace later'



@app.route("/",methods=['get','post'])
def index():
    
    reg_form = RegistartionForm()
    if reg_form.validate_on_submit():
        return "great success"
    return render_template("index.html",form=reg_form)


if __name__=="__main__":
    app.run(debug=True)
