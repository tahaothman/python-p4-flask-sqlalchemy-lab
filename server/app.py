#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if animal:
        return f'''
        <h2><ul>
            <ul>ID: {animal.id}</ul><br>
            <ul>Name: {animal.name}</ul><br>
            <ul>Species: {animal.species}</ul><br>
            <ul>Zookeeper: {animal.zookeeper.name}</ul><br>
            <ul>Enclosure: {animal.enclosure.environment}</ul><br>
        </ul></h2>
        '''
    return 'Animal not found'

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        animals_list = '<ul>'
        for animal in zookeeper.animals:
            animals_list += f'<ul>Animal: {animal.name}</ul><br>'
        animals_list += '</ul>'
        return f'''
        <h2><ul>
            <ul>ID: {zookeeper.id}</ul><br>
            <ul>Name: {zookeeper.name}</ul><br>
            <ul>Birthday: {zookeeper.birthday}</ul><br>
            {animals_list}
        </ul></h2>
        '''
    return 'Zookeeper not found'

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        animals_list = '<ul>'
        for animal in enclosure.animals:
            animals_list += f'<ul>Animal: {animal.name}</ul><br>'
        animals_list += '</ul>'
        return f'''
        <ul><h2>
            <ul>ID: {enclosure.id}</ul><br>
            <ul>Environment: {enclosure.environment}</ul><br>
            <ul>Open to Visitors: {enclosure.open_to_visitors}</ul><br>
            {animals_list}
        </ul></h2>
        '''
    return 'Enclosure not found'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
