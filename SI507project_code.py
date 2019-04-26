from SI507project_tools import *
import random
import csv
import sys
import io
import os
from flask import Flask, render_template, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_parks.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

db = SQLAlchemy(app)
session = db.session
bootstrap = Bootstrap(app)


main_soup = BeautifulSoup(main_page, features="html.parser")
list_of_states = main_soup.find('ul',{'class':'dropdown-menu SearchBar-keywordSearch'})

all_links = list_of_states.find_all('a')

name_list = []
type_list = []
description_list =[]
state_list =[]
states_pages = []
for l in all_links:
    page_data = access_page_data('https://www.nps.gov/' + l.get('href'))
    soup_of_page = BeautifulSoup(page_data, features="html.parser")
    # print(soup_of_page)
    list_page = soup_of_page.find('ul',{'id':'list_parks'})
    list_sites = list_page.find_all('li',{'class':'clearfix'})
    states_pages.append(list_sites)

for page_result in states_pages:
    for page_item in page_result:
        if page_item.find('a').get_text():
            name_list.append(page_item.find('a').get_text())
        if page_item.find('h2').get_text():
            type_list.append(page_item.find('h2').get_text())
        else:
            type_list.append('None')
        if page_item.find('p').get_text():
            description_list.append(page_item.find('p').get_text())
        else:
            description_list.append('None')
        if page_item.find('h4').get_text():
            state_list.append(page_item.find('h4').get_text())
            # states_list.append(abbre(page_item.find('h4').get_text()))
        else:
            state_list.append('None')

# Step1: Create the database

with open("park_data.csv","w",encoding='utf-8') as outfile:
#outfile = open("park_data.csv","w",encoding='utf-8')
    outfile.write('ParkName, Type, Description, State')
    outfile.write('\n')
    for n in range(len(name_list)):
        parkname_write =  '"' + name_list[n] + '"'
        type_write = '"' + type_list[n] + '"'
        description_write = '"' + description_list[n] + '"'
        state_write = '"' + state_list[n] + '"'
        row_string = '{},{},{},{}'.format(parkname_write, type_write, description_write, state_write)
        outfile.write(row_string)
        outfile.write('\n')
        # state_w1 = get_or_create_state(state_list[n])
        # type_w1 = get_or_create_type(type_list[n])
        # description_w1 = get_or_create_description(description_list[n])
        # park = Park(name=name_list[n], state_id=state_list[n],type_id=type_list[n])
        # session.add(park)
        # session.commit()

@app.route('/', methods=["GET", "POST"])
def index():
    parks = Park.query.all()
    num_parks = len(parks)
    name = request.form.get("Park Name")
    state = request.form.get("State")
    type = request.form.get("Type")
    return render_template('index.html', num_parks=num_parks)

@app.route('/new_park',methods=["Post"])
def new_park():
    name = request.form["Park Name"]
    state = request.form["State"]
    type = request.form["Type"]
    description = request.form["Description"]
    if Park.query.filter_by(name=name).first():
        return render_template('saved_park.html')
    else:
        # state = get_or_create_state(state)
        # type = get_or_create_type(type)
        # description = get_or_create_description(description)
        park = Park(name=name, state_id=state,type_id=type,descriptions=description)
        session.add(park)
        session.commit()
        return render_template('save_park.html',park=name, state = state, type = type, description=description)
        # return render_template('save_park.html',park=park.name, state = state.name, type = type.name, description=park.descriptions)

@app.route('/all_parks')
def see_all():
    all_parks = []
    parks = Park.query.all()
    for s in parks:
        state = s.state_id
        type = s.type_id
        all_parks.append((s.name,state,type))
    return render_template('all_parks.html',all_parks=all_parks)

@app.route('/all_states')
def see_all_states():
    states = Park.query.all()
    names = []
    for a in states:
        num_states = len(Park.query.filter_by(state_id=a.state_id).all())
        parks = Park.query.filter_by(state_id=a.name).all()
        newtup = (a.state_id,num_states,parks)
        names.append(newtup)
    return render_template('all_states.html',state_names=names)

# @app.route('/parks/descriptions/')
# def show_park_description():
#     output_str = ""
#     with open("park_data.csv","r",encoding = 'utf-8') as f:
#         reader = csv.reader(f)
#         parks_list = list(reader)
#         for num in range(20):
#             parks_input = parks_list[random.randint(1, len(parks_list) - 1)]
#             output_str = output_str + str(Park(parks_input)) + ' <br> '
#     return render_template('parks_description_template.html', string = output_str)

@app.route('/new/park/<name>/<state>/<type>/<description>')
def a_new_park(name,state,type,description):
    if Park.query.filter_by(name=name).first():
        return render_template('saved_park.html')
    else:
        # state = get_or_create_state(state)
        # type = get_or_create_type(type)
        # description = get_or_create_description(description)
        park = Park(name=name, state_id=state,type_id=type,descriptions = description)
        session.add(park)
        session.commit()
        return render_template('save_park.html',park=park.name, state = state, type = type, descriptions = description)

# Check for closed file
# fo = open("saved_park.html", "wb")
# print ("Name of the file: ", fo.name)
# print ("Closed or not : ", fo.closed)
# print ("Opening mode : ", fo.mode)

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run()
