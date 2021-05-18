import requests
from .constants import CHECKLISTS_CARD_ENDPOINT
from . import authorization

headers = authorization.get_authorization_headers()

def get_open_checklists_from_card(card):
    card_id = card['id']
    params = {'fields': 'name'}
    url = CHECKLISTS_CARD_ENDPOINT.format(card_id)
    response = requests.get(url, headers=headers, params=params)
    return response.json();