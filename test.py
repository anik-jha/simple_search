import flask
import requests
import json
import os

app = flask.Flask(__name__)

@app.route('/')
def test():
	return 'Hello World'

@app.route('/temp', methods=["GET"])
def hello_world():
	json_data = flask.request.json
	a_value = json_data["name"]
	return 'Hello '+ a_value

@app.route('/search', methods=["GET"])
def action1():
	# print(flask.request.args)
	api_key = '1f09de1bd3cbbfaa45a35846ec346592e620622f'
	fields = 'name,aliases,developers,genres,original_release_date,original_game_rating'
	r = requests.get(url = 'http://www.giantbomb.com/api/search/?api_key='+api_key+'&format=json&query="metroid prime"&resources=game&field_list='+fields,
					 headers={'user-agent':'newcoder'})

	# extracting data in json format
	data = json.loads(r.text)
	print(data)
	# print(r.request)
	# query = flask.request.args.get("query")
	# game = flask.request.args.get("game")

	return "All good"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3333)

#docker build -t test_flask:latest .

#docker run -it -p 6666:3333 --volume "/home/ssd/Downloads/simple:/home/ssd/Downloads/simple:rw" -w="/home/ssd/Downloads/simple" simple-search