user = {'name': 'Jose', 'access_level': 'guest'}

def get_admin_password():
	return '1234'

def make_secure(func):
	def secure_function():
		if user['access_level'] == 'admin':
			return func()
		else: 
			return f"{user['name']} does not have admin permisison"
	return secure_function

get_admin_password = make_secure(get_admin_password)

print(get_admin_password())