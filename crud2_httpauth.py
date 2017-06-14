from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
        if username == 'sti':
                return 'sti'
        return None

@auth.error_handler
def unauthorized():
        return make_response(jsonify({'error': 'Unauthorized access'}), 401)

