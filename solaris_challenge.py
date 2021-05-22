# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    flask_excel.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/18 01:07:45 by anolivei          #+#    #+#              #
#    Updated: 2021/05/22 15:41:50 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Counter
from flask import Flask, render_template, url_for, request, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/data', methods = ['GET', 'POST'])
def data():
	data = pd.read_csv("people_data.csv", encoding = "UTF-8", sep = ",", header = 0)
	return render_template('data.html', data = data.to_html())

@app.route('/youngers/<int:num>', methods = ['GET', 'POST'])
def youngers_n(num):
	df = pd.read_csv("people_data.csv", encoding = "UTF-8", sep = ",", header = 0)
	youngers = df.sort_values(by = "data_nasc", ascending = False)
	youngers_n = youngers.head(n = num)
	return render_template('youngers_n.html', youngers_n = youngers_n.to_html())

@app.route('/olders/<int:num>', methods = ['GET', 'POST'])
def olders_n(num):
	df = pd.read_csv("people_data.csv", encoding = "UTF-8", sep = ",", header = 0)
	olders_n = df.sort_values(by = "data_nasc", ascending = True)
	olders_n = olders_n.head(n = num)
	return render_template('olders_n.html', olders_n = olders_n.to_html())

@app.route('/gender-distribution', methods = ['GET', 'POST'])
def gender_distribution():
	df = pd.read_csv("people_data.csv", encoding = "UTF-8", sep = ",", header = 0)
	n = df["sexo"].value_counts('feminino') * 100
	fem = int(n[0])
	mas = int(n[1])
	return jsonify({'Feminino': fem, 'Maculino': mas})

@app.route('/blood-type', methods = ['GET', 'POST'])
def blood_type():
	df = pd.read_csv("people_data.csv", encoding = "UTF-8", sep = ",", header = 0)
	n = df["tipo_sanguineo"].value_counts().sort_index()
	print(n)
	ap = int(n[0])
	am = int(n[1])
	abp = int(n[2])
	abm = int(n[3])
	bp = int(n[4])
	bm = int(n[5])
	op = int(n[6])
	om = int(n[7])
	return jsonify({'A+': ap, 'A-': am, 'AB+': abp, 'AB-': abm, 'B+': bp, 'B-': bm, 'O+': op, 'O-': om})

@app.route('/peoples', methods = ['GET', 'POST'])
def peoples():
	df = pd.read_csv("people_data.csv", encoding = "UTF-8", sep = ",", header = 0)
	peoples = df.sort_values(by = "nome", ascending = True)
	return render_template('peoples.html', peoples = peoples.to_html())

if __name__ == '__main__':
	app.run(debug=True)