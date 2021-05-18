import requests
from constants import LISTS_BOARD_ENDPOINT
from . import authorization

headers = authorization.get_authorization_headers()

def get_open_lists_from_board(board):
    board_id = board['id']
    params = {'fields': 'name', 'filter':'open'};
    url = LISTS_BOARD_ENDPOINT.format(board_id)
    response = requests.get(url, headers=headers, params=params);
    return response.json();