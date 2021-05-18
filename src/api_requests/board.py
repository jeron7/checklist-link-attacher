import requests
from constants import BOARD_USER_ENDPOINT
from . import authorization

headers = authorization.get_authorization_headers()

def get_boards():
    params = {'fields': 'name', 'filter':'open'};
    url = BOARD_USER_ENDPOINT;
    response = requests.get(url, headers=headers, params=params)
    return response.json();