from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length, InputRequired
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    name = StringField(label='E-Mail', validators=[InputRequired(), Email()])
    password = PasswordField(label='Password', validators=[Length(min=8)])
    submit = SubmitField(label='Submit')


app = Flask(__name__)
app.secret_key = "aK3Yth@t1want"
EMAIL_ID = "admin@email.com"
PASSWORD = "12345678"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login_data():
    login_form = MyForm()
    if login_form.validate_on_submit() and request.method == 'POST':
        if login_form.name.data == EMAIL_ID and login_form.password.data == PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
