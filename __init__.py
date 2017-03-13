from flask import Flask, render_template
from __projetos__ import projetos
import os

PROJ = projetos()

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', PROJ=PROJ)

@app.route('/projetos/')
def projetos():
	return render_template('index.html', PROJ=PROJ)

@app.route('/projetos/xadrez/')
def xadrez():
	return render_template('xadrez.html')

if(__name__ == '__main__'):
	app.run(debug=True, host='0.0.0.0', port=int("81"))
