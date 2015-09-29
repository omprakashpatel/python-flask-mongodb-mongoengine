from flask import render_template
from application.app import app

# url scheams
@app.route("/")
def index():
	return '''<h1><center>Hello World </center></h1>
			<h3><center> welcome to my first web app </center></h3>'''


@app.route("/login")
def login():
	return "<h2> Login Page </h2>"


# run server
if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0")