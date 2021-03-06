import requests
from .constants import CHECKITEMS_CHECKLIST_ENDPOINT, CHECKITEM_CARD_ENDPOINT
from . import authorization

headers = authorization.get_authorization_headers()

def create_checkitem(checklist, checkitem_name):
    checklist_id = checklist['id']
    params = {'name': checkitem_name}
    url = CHECKITEMS_CHECKLIST_ENDPOINT.format(checklist_id)
    response = requests.post(url, headers=headers, params=params)
    return response;

def delete_checkitem(card, checkitem):
    checkitem_id = checkitem['id']
    card_id = card['id']
    url = CHECKITEM_CARD_ENDPOINT.format(card_id, checkitem_id)
    response = requests.delete(url, headers=headers)
    return response;