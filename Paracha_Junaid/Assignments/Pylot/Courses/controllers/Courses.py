from system.core.controller import *
class Courses(Controller):
	def __init__(self, action):
		super(Courses, self).__init__(action)
		# Note that we have to load the model before using it
		self.load_model('CourseModel')

	def index(self):
		return self.load_view('index.html')

	# This is how a method with a route parameter that provides the id would work
	# We would set up a GET route for this method
	def show(self):
		# Note how we access the model using self.models
		course = self.models['CourseModel'].get_courses()
		return self.load_view('index.html', course=course)

	# This is how a method used to add a course would look
	# We would set up a POST route for this method
	def add(self):
		# in actuality, data for the new course would come 
		# from a form on our client
		course_details = {
			'title': request.form['name'],
			'description': request.form['discription']
		}
		self.models['CourseModel'].add_course(course_details)
		return redirect('/show')

	def destroy(self, id):
		remove_course = self.models['CourseModel'].get_revove_course(id)
		remove_course = remove_course[0]
		return self.load_view('destroy.html', remove_course=remove_course)

	def delete_course(self, id):
		self.models['CourseModel'].delete_course(id)
		return redirect('/show')