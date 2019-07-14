from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/invalid", methods=['POST'])
def invalid():
    Username = request.form['Username']
    password = request.form['Password']
    verifypassword = request.form['VerifyPassword']
    email = request.form['Email']

    usererror =""
    passerror = ''
    verifypasserror = ''
    EmailError = ''

    if Username == '':
        usererror = 'Field is empty'
    # or Password or VerifyPassword or Email == "":
    
    #if len(username) == " " in username
    if len(Username) <3 or len(Username)>20:
        usererror = "invalid submission"
    
    if password == '':
        passerror = "Field is empty"
   
    if verifypassword == '':
        verifypasserror = "Field is empty"

    if password != verifypassword:
        verifypasserror = "Passwords do not match."
    
    


    if len(email) > 0:
        
        if len(email) < 3 or len(email)>20:
            EmailError='Email does not have proper length'
            
    #    if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
    #        return True

        elif email.count('@') != 1 or email.count('.') != 1:
            EmailError='Not a valid Email address'

    
    if usererror == '' and passerror == '' and verifypasserror == '' and EmailError == '':
        return "<h1>Welcome " + Username + " </h1>"  

    return render_template('template.html', usererror = usererror, passerror=passerror, verifypasserror=verifypasserror, EmailError=EmailError, Username=Username)

    
@app.route("/")
def index():
    return render_template('template.html')

if __name__=='__main__':
    app.run()