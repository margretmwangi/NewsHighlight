from .import main


#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	
@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	