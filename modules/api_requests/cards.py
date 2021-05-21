import requests
from .constants import CARD_LISTS_ENDPOINT, ACTIONS_CARD_ENDPOINT
from . import authorization

headers = authorization.get_authorization_headers()

def get_open_cards_from_list(list):
    list_id = list['id']
    params = {'fields': 'name,idChecklists' , 'filter':'open'}
    url = CARD_LISTS_ENDPOINT.format(list_id);
    response = requests.get(url, headers=headers, params=params)
    return response.json();

def get_actions_of_card(card):
    card_id = card['id']
    params = {'fields': 'id,data,date', 'filter': 'commentCard'}
    url = ACTIONS_CARD_ENDPOINT.format(card_id)
    response = requests.get(url, headers=headers, params=params)
    return response.json();