from .attach_link import select_board, select_list_from_board, select_card_from_list, select_checklist_from_card
from ..api_requests import checkitem

CHECKITEM_STATE = 'state'
CHECKITEM_NAME = 'name'
INCOMPLETE_CHECKITEM = 'incomplete'
MARKDOWN_LINK_NAME_STARTS = '['
MARKDOWN_LINK_NAME_ENDS = ']'

def run():
    selected_board = select_board()
    selected_list = select_list_from_board(selected_board)
    selected_card = select_card_from_list(selected_list)
    selected_checklist = select_checklist_from_card(selected_card)
    selected_checkitem = select_checkitem(selected_checklist)
    finish_checkitem(selected_checkitem, selected_card)    

def finish_checkitem(checki, card):
    response = checkitem.finish_checkitem(card, checki)
    if (response.status_code == 200):
        print("Link quoted was finished :D")
    else:
        print("Link was not finished. Some error might be occurred :C")
    print('')

def select_checkitem(checklist):
    checkitems = checklist['checkItems']
    display_checkitems(checkitems)
    choice = int(input('\n> Select a checkitem above: '))
    return checkitems[-choice]
    
def display_checkitems(checkitems):
    number = 1;
    checkitems.reverse()
    print('\nUnfinished checkitems from selected checklist:')
    for i in range(len(checkitems) - 1, -1, -1):
        checki = checkitems[i]
        if (isIncomplete(checki)):
            name = checki[CHECKITEM_NAME].split(MARKDOWN_LINK_NAME_ENDS)[0].strip(MARKDOWN_LINK_NAME_STARTS)
            print ("{} - {}".format(number, name))
            number += 1
        else:
            checkitems.pop(i)
    if (len(checkitems) == 0):
        raise Exception('This checklist was none unfinished checkitems :(')

def isIncomplete(checkitem):
    return checkitem[CHECKITEM_STATE] == INCOMPLETE_CHECKITEM