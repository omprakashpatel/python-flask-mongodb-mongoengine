from application.app import app
from flask.ext.login import LoginManager, UserMixin, AnonymousUserMixin
from handler import get_user


class UserLogin(UserMixin):
	def __init__(self, id, name, email, **kwargs):
		self.id = id
		self.name = name
		self.email = email


class Anonymous(AnonymousUserMixin):
    name = u"Anonymous"

login_manager = LoginManager()
login_manager.anonymous_user = Anonymous
login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(id):
	print "reloading user data"
	print id
	return UserLogin(**get_user(id))


login_manager.setup_app(app)
