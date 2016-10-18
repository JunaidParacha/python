from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)

		self.load_model('User')
		self.db = self._app.db
	
	def index(self):
		print session
		if 'id' in session:
			return redirect('/Users/logged_in')
		return self.load_view('Users/index.html')

	def create(self):
	
		user_info = {
		"first_name" : request.form['first_name'],
		"last_name" : request.form['last_name'],
		"email" : request.form['email'],
		"password" : request.form['password'],
		"confirm_pw" : request.form['confirm_pw']
		}
		# call create_user method from model and write some logic based on the returned value
		# notice how we passed the user_info to our model method
		create_status = self.models['User'].create_user(user_info)
		if create_status['status'] == True:
			# the user should have been created in the model
			# we can set the newly-created users id and name to session
			session['id'] = create_status['user']['id'] 
			session['first_name'] = create_status['user']['first_name']
			# we can redirect to the users profile page here
			return redirect('/Users/logged_in')
		else:
			# set flashed error messages here from the error messages we returned from the Model
			for message in create_status['errors']:
				flash(message, 'regis_errors')
			# redirect to the method that renders the form
			return redirect('/Users')
	def success(self):
		if not 'id' in session:
			return redirect('/')
		return self.load_view('Users/success.html')

	def loggin(self):
	
		user_info = {
		"email" : request.form['email'],
		"password" : request.form['password']
		}

		login_status = self.models['User'].login_user(user_info)
		if login_status['status'] == True:
			# the user should have been created in the model
			# we can set the newly-created users id and name to session
			session['id'] = login_status['user']['id'] 
			session['first_name'] = login_status['user']['first_name']
			# we can redirect to the users profile page here
			return redirect('/Users/logged_in')
		else:
			# set flashed error messages here from the error messages we returned from the Model
			for message in login_status['errors']:
				flash(message, 'regis_errors')
			# redirect to the method that renders the form
			return redirect('/Users')
	
	def logout(self):
		session.clear()
		return redirect('/Users')
	

