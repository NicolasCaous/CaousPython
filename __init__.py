from flask import Flask, render_template, request, send_from_directory
from __projetos__ import projetos
import os

PROJ = projetos()

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>')
def catch_all(path):
	if(request.method == 'GET' and '.html' not in path):
		split = path.split('/')
		nome = split[len(split) - 1]
		temp = os.path.realpath(__file__).replace('__init__.py', '')
		temp = temp + 'static/' 
		for s in split[1:len(split) - 1]:
			temp = temp + s + '/'
		return send_from_directory(temp, nome)
	else:
		return render_template(path.replace('projetos/', ''))

@app.route('/')
def index():
	return render_template('index.html', PROJ=PROJ)

@app.route('/projetos/')
def projetos():
	return render_template('index.html', PROJ=PROJ)

@app.route('/projetos/ValemobiEstagio/index.html')
def xadrez():
	return render_template('ValemobiEstagio/index.html')

if(__name__ == '__main__'):
	app.run(debug=True, host='0.0.0.0', port=int("81"))
