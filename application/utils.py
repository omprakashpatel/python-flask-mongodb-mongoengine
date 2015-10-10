from functools import wraps
'''
This is Global Utils
'''
class CustomException(Exception):
    status_code = 400
    '''
    CustomException class to raise Custom API Exception with status_code
    and payload
    '''

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def _repr(self):
        rv = dict(self.payload or ())
        rv['error_msg'] = self.message
        rv['status'] = 'failed'
        rv['code'] = self.status_code
        return rv

class Codes:
    Ok = OK = PASS = 200
    CREATED = 201
    ACCEPTED = 202
    RESET = 205
    SEE_OTHER = 303
    LOGIN_REQUIRED = 401
    REQUIRED_PARAMETER = 402
    ACCESS_DENIED = 403
    NOT_FOUND = 404
    NOT_ALLOWED = 405
    CONFLICT = 409
    NULL_PARAM = 412
    CONDITION_FAIL = 412
    INVALID_PARAM = 412
    FAIL = 500
    INTERNAL_ERROR = 500

def check_req_param(req):
    def init_dec(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            print "req_param Check"
            for a in req:
                if not kwargs.get(a):
                    raise CustomException("{} is a Required Parameter".format(a))
            return f(*args, **kwargs)
        return decorated_function
    return init_dec

def format_data_type(list_var=[], int_var=[], non_list_var=[]):
    def init_format(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            print "format_data_type"

            for a in list_var:
                if kwargs.get(a) and not isinstance(kwargs[a], list):
                    kwargs[a] = [kwargs[a]]

            for c in non_list_var:
                if kwargs.get(c):
                    if isinstance(kwargs[c], list):
                        kwargs[c] = kwargs[c][0]

            for b in int_var:
                if kwargs.get(b):
                    if isinstance(kwargs[b], list):
                        kwargs[b] = kwargs[b][0]
                    kwargs[b] = int(kwargs[b])

            return f(*args, **kwargs)
        return decorated_function
    return init_format
