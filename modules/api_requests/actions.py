import requests
from .constants import TEXT_ACTIONS_ENDPOINT
from . import authorization

headers = authorization.get_authorization_headers()

def append_checkitem_in_action(action, checkitem):
    action_id = action['id']
    checkitem_value = '\n1. {}'.format(checkitem['name'])
    updated_action_text = action['data']['text'] + checkitem_value
    params = {'value': updated_action_text }
    url = TEXT_ACTIONS_ENDPOINT.format(action_id);
    response = requests.put(url, headers=headers, params=params)
    return response;