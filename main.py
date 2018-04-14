from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template('user_name.html')

@app.route("/validate_user", methods=['POST'])
def validate_user():    
    u_name = request.form['user_name']
    p_word = request.form['pass_word']
    p_word2 = request.form['pass_word2']
    emal = request.form['e_mail']
    u_error = ""
    p_error = ""
    m_error = ""
    e_error = ""

    if u_name == "":
        u_error = "The username is invalid"
        return render_template('user_name.html', user_name=u_name, username_error=u_error,  e_mail=emal)
    if len(u_name) < 3 or len(u_name) > 20:
        u_error = "The username must be between 3 and 20 characters"
        return render_template('user_name.html',user_name=u_name, username_error=u_error,  e_mail=emal)
    if " " in u_name:
        u_error = "The username cannot contain any spaces"
        return render_template('user_name.html',user_name=u_name, username_error=u_error,  e_mail=emal)
    if p_word == "":
        p_error = "The password is invalid"
        return render_template('user_name.html', user_name=u_name, password=p_word, password_error=p_error,  e_mail=emal)
    if len(p_word) < 3 or len(p_word) > 20:
        p_error = "The password must be between 3 and 20 characters"
        return render_template('user_name.html', user_name=u_name, password=p_word, password_error=p_error,  e_mail=emal)
    if " " in p_word:
        p_error = "The password cannot contain any spaces"
        return render_template('user_name.html', user_name=u_name, password=p_word, password_error=p_error, e_mail=emal)
    if p_word != p_word2:
        m_error = "The passwords do not match"
        return render_template('user_name.html', user_name=u_name, password=p_word, match_error=m_error, e_mail=emal)
    if len(emal) > 0:    
        if "@" and "." not in emal:
            e_error = "Please enter a valid email address"
            return render_template('user_name.html', user_name=u_name, password=p_word, password_error=p_error, e_mail=emal, email_error=e_error)
        if len(emal) < 3 or len(emal) > 30:
            e_error = "The email address must be between 3 and 20 characters"
            return render_template('user_name.html', user_name=u_name, password=p_word, password_error=p_error, e_mail=emal, email_error=e_error)
        if " " in emal:
            e_error = "The email address cannot contain any spaces"
            return render_template('user_name.html', user_name=u_name, password=p_word, password_error=p_error, e_mail=emal, email_error=e_error)
        else:
            return  redirect('/welcome')
    else:
        return  redirect('/welcome')

    

@app.route("/welcome")
def welcome_page():
    return '''<h1>'Welcome to the site'</h1>'''


app.run()