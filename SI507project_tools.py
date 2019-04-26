import requests, json
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
from flask_sqlalchemy import SQLAlchemy
import sys
import io
import random
import csv
import os
from flask import Flask, render_template, session, redirect, url_for, request
from flask_bootstrap import Bootstrap
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import relationship
from sqlite3 import dbapi2 as sqlite
from sqlalchemy import create_engine

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_parks.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
session = db.session

START_URL = "https://www.nps.gov/index.htm"
FILENAME = "finalproject_cache.json"
PROGRAM_CACHE = Cache(FILENAME)

sites = db.Table('sites',db.Column('states_id',db.Integer, db.ForeignKey('states.id')),db.Column('types_id',db.Integer, db.ForeignKey('types.id')))

class Park(db.Model):
    __tablename__ = "parks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)
    descriptions = db.Column(db.String(64),unique=True)
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"))
    type_id = db.Column(db.Integer, db.ForeignKey("types.id"))
    def __repr__(self):
        return self.name

class State(db.Model):
    __tablename__ = "states"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    types = db.relationship('Type',secondary=sites,backref=db.backref('states',lazy='dynamic'),lazy='dynamic')
    park = db.relationship('Park',backref='State')
    def __repr__(self):
        return "{}".format(self.name)

class Type(db.Model):
    __tablename__ = "types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    park = db.relationship('Park',backref='Type')
    def __repr__(self):
        return "{}".format(self.name)


def access_page_data(url):
    data = PROGRAM_CACHE.get(url)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data)
    return data

main_page = access_page_data(START_URL)

# def write_database_state(state_name):
#     state = State(name=state_name)
#     session.add(state)
#     session.commit()
#     return state
#
# def write_database_type(type_name):
#     type = Type(name=type_name)
#     session.add(type)
#     session.commit()
#     return type
#
# def write_database_description(description):
#     descriptions = Park(descriptions=description)
#     session.add(descriptions)
#     session.commit()
#     return descriptions

def get_or_create_state(state_name):
    state = State.query.filter_by(name=state_name).first()
    if state:
        return state
    else:
        state = State(name=state_name)
        session.add(state)
        session.commit()
        return state

def get_or_create_type(type_name):
    type = Type.query.filter_by(name=type_name).first()
    if type:
        return type
    else:
        type = Type(name=type_name)
        session.add(type)
        session.commit()
        return type

def get_or_create_description(description):
    description = Park.query.filter_by(descriptions=description).first()
    if description:
        return description
    else:
        description = Park(descriptions=description)
        session.add(description)
        session.commit()
        return description
