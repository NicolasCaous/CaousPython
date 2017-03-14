from flask import Flask, render_template, request, send_from_directory
from time import strftime
from __projetos__ import projetos
import os

PROJ = projetos()

app = Flask(__name__)

@app.after_request
def after_request(response):
	f = open('http.log', 'a+')
	timestamp = strftime('[%d-%b-%Y %H:%M:%S]')
	f.write(timestamp + '  ' + request.remote_addr + '  ' + request.method + '  ' + request.scheme + '  ' + request.full_path + '  ' + response.status + '\n')
	print('LOGGING --> ' + timestamp + '  ' + request.remote_addr + '  ' + request.method + '  ' + request.scheme + '  ' + request.full_path + '  ' + response.status)
	f.close()
	return response

class createapproute():
	def __init__(self, path):
		@app.route('/projetos/' + path)
		def func():
			return render_template(path)
		self.f = func

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>')
def catch_all(path):
	if(request.method == 'GET' and '.html' not in path):
		split = path.split('/')
		nome = split[len(split) - 1]
		temp = os.path.realpath(__file__).replace('__init__.py', '')
		temp = temp + 'templates/'
		for s in split[0:len(split) - 1]:
			temp = temp + s + '/'
		return send_from_directory(temp, nome)
	else:
		return render_template(path.replace('projetos/', ''))

@app.route('/')
@app.route('/projetos/')
def index():
	return render_template('caous.html', PROJ=PROJ)

if(__name__ == '__main__'):
	funcs = []
	for Tupla in PROJ:
		funcs.append(createapproute(Tupla[1]))
	app.run(debug=True, host='0.0.0.0', port=int("81"))
