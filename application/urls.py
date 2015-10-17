from flask import render_template, request, redirect, url_for, jsonify, g
from application import handler
from application.utils import CustomException, fix_param

from application.app import app
from application.auth import UserLogin
from flask.ext.login import login_user, logout_user, login_required, current_user

user = current_user

# url scheams
@app.route("/")
def index():
	user = {}
	if current_user.is_authenticated:
		user = current_user
		return render_template('home.html', user=user)
	return render_template('index.html', user=user)

@app.route("/profile")
def profile():
	if current_user.is_authenticated:
		user = current_user
		return render_template('profile.html', user=user)
	return redirect( url_for( 'index' ) )


@app.route("/signin", methods=['GET', 'POST'])
def signin():
	if request.method == "GET":
		return render_template('signin.html')
	elif request.method == "POST":
		_res = handler.login(**(request.form or {}))
		# login in session
		login_user(UserLogin(**_res), remember=True)
		return redirect(url_for('profile'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
	logout_user()
	return redirect(url_for('signin'))

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	if request.method == "GET":
		return render_template('signup.html')
	elif request.method == "POST":
		_res = handler.create_user(**(request.form or {}))
		login_user(UserLogin(**_res))
		return redirect(url_for('profile'))


@app.route('/current_user', methods=['GET'])
def get_current_user():
	if current_user.is_authenticated:
		return jsonify(status="success",
				data={'id': str(current_user.id),
					'name': current_user.name,
					'email': current_user.name})
	else:
		return "User not logged in"

@app.errorhandler(404)
def page_not_found(error):
	return render_template("page_not_found.html"), 404

@app.errorhandler(CustomException)
def custom_exception(error):
    # Need to Add Error Filtering. Right now masking all Exception.
    print "**************************"
    print str(error)
    print "**************************"
    return str(error)

@app.errorhandler(Exception)
def exception_handler(error):
    # Need to Add Error Filtering. Right now masking all Exception.
    print "**************************"
    print str(error)
    print "**************************"
    return str(error)
