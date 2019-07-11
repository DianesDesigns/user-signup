from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True


form ="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}   
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;           
            }}
        </style>
    </head>
    <body>
        <form action="/hello" method="post">
            <label for="rotate-by">Rotate by:</label>
                <input id="rotate-by" type=text name="rot" />      
            <input type="submit" name="submit button" value="Submit"></input>
        </form>
        </body>
</html> 
"""

@app.route("/hello", methods=['POST'])
def encrypt():
    text = request.form['text']
    num = int(request.form['rot'])
    rotate=rotate_string(text,num)
    return form.format(rotate)
    
@app.route("/")
def index():
    return form.format(0)

if __name__=='__main__':
    app.run()