from ..api_requests import board, card, checkitem, checklist, links, lists

def run():
    selected_board = select_board()
    selected_list = select_list_from_board(selected_board)
    selected_card = select_card_from_list(selected_list)
    selected_checklist = select_checklist_from_card(selected_card)
    append_link_to_checklist(selected_checklist)

def append_link_to_checklist(checklist):
    link = input('\n> Type the link that you want to append: ')
    title = links.get_link_title(link)
    checkitem_name = "[{}]({})".format(title, link)
    response = checkitem.create_checkitem(checklist, checkitem_name)
    if (response.status_code == 200):
        print("Link was been appended successfully :D")
    else:
        print("Link was not appended. Some error might be occurred :C")
    print('')   

def select_card_from_list(list):
    open_cards = card.get_open_cards_from_list(list)
    display_open_cards(open_cards)
    choice = int(input('\n> Select a card above: '))
    return open_cards[choice - 1]
    
def select_checklist_from_card(card):
    open_checklists = checklist.get_open_checklists_from_card(card)
    display_open_checklists(open_checklists)
    choice = int(input('\n> Select a checklist above: '))
    return open_checklists[choice - 1]

def select_list_from_board(board):
    open_lists = lists.get_open_lists_from_board(board)
    display_open_lists(open_lists)
    choice = int(input('\n> Select a list above: '))
    return open_lists[choice - 1]

def select_board():
    open_boards = board.get_boards()
    display_open_boards(open_boards)
    choice = int(input('\n> Select a board above: '))
    return open_boards[choice - 1]

def display_open_cards(cards):
    number = 1;
    print('\nOpen cards from selected list:')
    for card in cards:
        print ("{} - {}".format(number, card['name']))
        number += 1

def display_open_lists(lists):
    number = 1;
    print('\nOpen lists from selected board:')
    for a_list in lists:
        print ("{} - {}".format(number, a_list['name']))
        number += 1

def display_open_checklists(checklists):
    number = 1
    print('\nOpen checklists from selected card:')
    for checklist in checklists:
        print ("{} - {}".format(number, checklist['name']))
        number += 1
    
def display_open_boards(boards):
    number = 1
    print('\nOpen boards:')
    for board in boards:
        print ("{} - {}".format(number, board['name']))
        number += 1