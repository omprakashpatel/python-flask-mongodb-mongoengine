from flask import render_template
from application.app import app

# url scheams
@app.route("/")
def index():
	return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == "GET":
		return "<h2> Login Page </h2>"
	elif request.method == "POST":
		return ""


# run server
if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0")
