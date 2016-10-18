"""
	Sample Controller File

	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.

	Create a controller using this template
"""
from system.core.controller import *
import random

class Ninja(Controller):
	def __init__(self, action):
		super(Ninja, self).__init__(action)
		"""
			This is an example of loading a model.
			Every controller has access to the load_model method.
		"""
		self.load_model('WelcomeModel')
		self.db = self._app.db

		"""
		
		This is an example of a controller method that will load a view for the client 

		"""
   
	def index(self):
		"""
		A loaded model is accessible through the models attribute 
		self.models['WelcomeModel'].get_users()
		
		self.models['WelcomeModel'].add_message()
		# messages = self.models['WelcomeModel'].grab_messages()
		# user = self.models['WelcomeModel'].get_user()
		# to pass information on to a view it's the same as it was with Flask
		
		# return self.load_view('index.html', messages=messages, user=user)
		"""
		if not 'gold' in session:
			session['gold'] = 0
		if not 'activities' in session:
			session['activities'] = []

		return self.load_view('index.html', your_gold = session['gold'])

	def process(self):
		buildings = {
			'farm':random.randint(10,20),
			'casino':random.randint(-50,50),
			'cave':random.randint(2,5),
			'house':random.randint(2,5)
		}
		if request.form['building'] in buildings:
			""" OMG What???"""
			result = buildings[ request.form['building'] ]
			session['gold'] = session['gold']+result
			result_dictionary = {
									'class': ('red','green')[result > 0],
									'activity': "You went to the {} and {} {} gold!".format(request.form['building'], ('lost','gained')[result > 0], result)
								}
			# session['activities'].append(result_dictionary)
			session['activities'].insert(0,result_dictionary)

		return redirect('/')