import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()
TOKEN = os.getenv('VK_GROUP_TOKEN')
VERSION = os.getenv('VERSION')
AUTH_PARAMS = {
    'access_token': TOKEN,
    'v': VERSION
}
URL = 'https://api.vk.com/method/'


def get_cities_info():
    cities = 'Томск' # change this field to add other cities to the db
    params = {'q': cities,
              'need_all': 0,
              'count': 1000,
              **AUTH_PARAMS}
    method = 'database.getCities'
    response = requests.get(URL + method, params=params)
    cities_list = response.json()["response"]["items"]
    return cities_list


def get_user_info(offset):
    """Получаем информацию о пользователях """
    method = 'users.search'
    fields = ['last_seen', 'bdate', 'sex', 'city', 'country',
              'followers_count', 'contacts', 'relation',
              'connections', 'can_write_private_message',
              'can_post', 'interests']
    user_params = {
        'country_id': 1,
        'city_id': 1, # change this field to add users from other cities
        'fields': ','.join(fields),
        'count': 1000,
        'age_from': 18,
        'sort': 0,
        'can_write_private_message': 1,
        'offset': offset, 
        **AUTH_PARAMS
    }
    response = requests.get(URL + method, params=user_params)
    users_list = response.json()["response"]["items"]
    return users_list
