# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solaris_challenge.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/18 01:07:45 by anolivei          #+#    #+#              #
#    Updated: 2021/05/22 19:17:12 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("people_data.csv", encoding = "UTF-8", sep = ",", header = 0)

@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/data', methods = ['GET', 'POST'])
def data():
	return render_template('data.html', data = df.to_html())

@app.route('/youngers/<int:num>', methods = ['GET', 'POST'])
def youngers_n(num):
	youngers_n = df.sort_values(by = "data_nasc", ascending = False)
	youngers_n = youngers_n.head(n = num)
	return render_template('youngers_n.html', youngers_n = youngers_n.to_html())

@app.route('/olders/<int:num>', methods = ['GET', 'POST'])
def olders_n(num):
	olders_n = df.sort_values(by = "data_nasc", ascending = True)
	olders_n = olders_n.head(n = num)
	olders_n = olders_n.sort_values(by = "data_nasc", ascending = False)
	return render_template('olders_n.html', olders_n = olders_n.to_html())

@app.route('/gender-distribution', methods = ['GET', 'POST'])
def gender_distribution():
	gender_distribution = df["sexo"].value_counts('feminino') * 100
	return render_template('gender_distribution.html', gender_distribution = gender_distribution.to_json())

@app.route('/people/<string:num>', methods = ['GET', 'POST'])
def people(num):
	if len(num) < 11:
		num = num.zfill(11)
	cpf = '{}.{}.{}-{}'.format(num[:3], num[3:6], num[6:9], num[9:])
	people = df.loc[df["cpf"] == cpf]
	return render_template('people.html', people = people.to_json())

@app.route('/blood-type', methods = ['GET', 'POST'])
def blood_type():
	blood_type = df["tipo_sanguineo"].value_counts()
	return render_template('blood_type.html', blood_type = blood_type.to_json())

@app.route('/peoples', methods = ['GET', 'POST'])
def peoples():
	peoples = df.sort_values(by = "nome", ascending = True)
	return render_template('peoples.html', peoples = peoples.to_html())

@app.route('/peoples/search<string:name>', methods = ['GET', 'POST'])
def peoples_name(name):
	peoples = df[df["nome"].str.lower().str.contains(str.lower(name))]
	return render_template('peoples.html', peoples = peoples.to_html())

if __name__ == '__main__':
	app.run(debug=True)