from application.models.base import User
from application.utils import format_data_type, CustomException



def get_user(id):
	_user = User.objects.get(id=id)
	return {'id': _user.id, 'name': _user.name, 'email': _user.email }


@format_data_type(non_list_var=['name', 'email', 'password'])
def create_user(name, email, password, **kwargs):
	""" User registration handler """
	try:
		_user = User(name=name, email=email, password=password)
		_obj = _user.save()
	except Exception, e:
		raise e
	return get_user(_obj.id)


@format_data_type(non_list_var=['email', 'password'])
def login(email, password, **kwargs):
	""" User Login handler """
	try:
		_user = User.objects.get(email=email, password=password)
	except Exception, e:
		raise e
	_ret = {'id': _user.id, 'name': _user.name, 'email': _user.email }
	print _ret
	return _ret


