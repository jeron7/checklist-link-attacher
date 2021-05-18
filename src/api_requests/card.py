import requests
from constants import CARD_LISTS_ENDPOINT
from . import authorization

headers = authorization.get_authorization_headers()

def get_open_cards_from_list(list):
    list_id = list['id']
    params = {'fields': 'name', 'filter':'open'}
    url = CARD_LISTS_ENDPOINT.format(list_id);
    response = requests.get(url, headers=headers, params=params)
    return response.json();