from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField



class LoginForm(FlaskForm):
    email = StringField('email')
    password = StringField('Password')


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if not request.form["username"]:
        return render_template("index.html")
    else:
        print(request.form["username"])
        login_form = LoginForm()
        return render_template('submit.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)