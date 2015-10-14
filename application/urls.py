from flask import render_template, request
from application import handler
from application.utils import CustomException

from application.app import app

# url scheams
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/signin", methods=['GET', 'POST'])
def signin():
	if request.method == "GET":
		return render_template('signin.html')
	elif request.method == "POST":
		_res = handler.login(**(request.form or {}))
		return render_template('profile.html', context=_res)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	if request.method == "GET":
		return render_template('signup.html')
	elif request.method == "POST":
		return handler.create_user(**(request.form or {}))

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
