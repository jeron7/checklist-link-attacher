from options import attach_link, finish_checkitem

def main():
    print('Welcome to Checklist Link Attacher :))')
    finished = False;
    while (not finished):
        option = show_menu()
        if (option == 1):
            attach_link.run()
        else:
            finish_checkitem.run()

        answer = input("Do you want do another thing? [Y/n]: ")
        if (answer.upper() != "Y"):
            finished = True

def finish_checkitem():
    print('TODO')


def show_menu():
    print('1. Attach a link on a checklist')
    print('2. Finish a readed checkitem')
    option = int(input('\n> Select an option above: '))
    if (not valid_option(option)):
        print('Please, select a valid option :)')
        return show_menu()
    else:
        return option;
    
def valid_option(option):
    return option <= 2 or option >= 1;
   
if __name__ == "__main__":
    main()