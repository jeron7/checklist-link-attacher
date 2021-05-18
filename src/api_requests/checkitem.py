import requests
from constants import CHECKITEMS_CHECKLIST_ENDPOINT, CHECKITEM_CHECKLIST_CARD_ENDPOINT
from . import authorization

headers = authorization.get_authorization_headers()

def create_checkitem(checklist, checkitem_name):
    checklist_id = checklist['id']
    params = {'name': checkitem_name}
    url = CHECKITEMS_CHECKLIST_ENDPOINT.format(checklist_id)
    response = requests.post(url, headers=headers, params=params)
    return response;

def get_checkitems(checklist):
    checklist_id = checklist['id']
    params = {'name': checkitem_name}
    url = CHECKITEMS_CHECKLIST_ENDPOINT.format(checklist_id)
    response = requests.get(url, headers=headers, params=params)
    return response;

def finish_checkitem(card, checklist, checkitem):
    checklist_id = checklist['id']
    params = {'name': checkitem_name}
    url = CHECKITEM_CHECKLIST_CARD_ENDPOINT.format(card_id, checklist_id, checkitem_id)
    response = requests.post(url, headers=headers, params=params)
    return response;