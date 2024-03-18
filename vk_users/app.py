from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash)
import os
import requests
from vk_users.vk_users_db import (
    get_vk_users,
    add_user_to_db,
    get_user_by_id,
    get_cities,
    add_city_to_db,
    get_city_by_id,
    )
from vk_users.requests_to_vk import get_user_info, get_cities_info


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
N = 1000 # How many users do you want to collect to ypur db?


@app.route('/')
def get_users():
    users = get_vk_users()
    cities = get_cities
    return render_template('index.html', users=users, cities=cities)


@app.route('/add_users')
def add_users():
    users_new = []
    for offset in range(0, N, 100):
        users_new += get_user_info(offset)
    for user in users_new:
        # check if user is already added to the db
        if not get_user_by_id(user['id']) and user['last_seen']['time'] >= 1704060060 and user['can_write_private_message'] == 1:
            flash('New users are added!', 'alert')
            add_user_to_db(user)
    return redirect(url_for('get_users'), code=302)


@app.route('/add_cities')
def add_cities():
    cities = get_cities_info()
    for city in cities:
        # check if city is already added to the db
        if not get_city_by_id(city['id']):
            flash('New city added!', 'alert')
            add_city_to_db(city)
    return redirect(url_for('get_users'), code=302)
