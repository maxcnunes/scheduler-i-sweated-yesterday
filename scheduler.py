from flask import Flask
import requests

app = Flask(__name__)

# Routes #

@app.route('/')
def index():
	return 'Scheduler - I Sweated Yesterday Application'

@app.errorhandler(404)
def not_found(error):
	return 'Not Found'

@app.route('/request_send_exercise_notifications')
def request_send_exercise_notifications():

	url = 'http://isweatedyesterday.herokuapp.com/exercises/send_exercise_notifications/'
	# must be changed
	user = 'secrete_user' 
	password = 'secrete_password'

	request = requests.head(url, auth=(user, password))
	
	return str(request.status_code)
