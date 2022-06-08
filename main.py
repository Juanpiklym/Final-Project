import json
import pandas as pd


def start():
    option = input('Hello '
                   '\nPress 1 to add a new contact '
                   '\nPress 2 to edit information '
                   '\nPress 3 to delete a contact'
                   '\nPress 4 to to see all contacts'
                   '\nPress Q to close program \n')

    if option == '1':
        add_contact()
    elif option == '2':
        edit_contact()
    elif option == '3':
        del_contact()
    elif option == '4':
        see_contact()
    elif option == 'Q' or option == 'q':
        quit()
    else:
        print('Invalid option, please try again \n')
        return start()


def add_contact():
    data = json.load(open('agenda.json'))
    # Ask for input
    first_name = input('Insert first name: ')
    last_name = input('Insert last name: ')
    phone_numb = input('Insert phone number: ')

    contact = {"N": (len(data) + 1),
               "First Name": first_name,
               "Last Name": last_name,
               "Phone Number": phone_numb}
    data.append(contact)

    with open('agenda.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    print('\n New contact added successfully! \n')

    repeat = input('Do you want to add another contact?'
                   'If yes = Y; if no = N\n')
    if repeat == 'Y' or repeat == 'y':
        add_contact()
    elif repeat == 'N' or repeat == 'n':
        start()
    else:
        'Not valid option \n'
        start()


def edit_contact():
    with open('agenda.json') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    print(df.loc[:, df.columns != 'N'])

    edite_contact = int(input('Write the number position of the contact you want to edit: '))
    print(df.loc[edite_contact])
    print('\n Is this the contact you want to edit? \n')

    confirmation = input('If yes = Y; if not = N ')

    if confirmation == 'Y' or confirmation == 'y':
        edition = input('What do you want to edit:'
                        ' First Name = F; Last Name = L; Phone Number = P \n')
        if edition == 'F' or edition == 'f':
            new_name = input('Write the new First Name: ')
            data[edite_contact]['First Name'] = new_name
            print('Contact successfully edited \n')
        elif edition == 'L' or edition == 'l':
            new_last = input('Write the new Last Name: ')
            data[edite_contact]['Last Name'] = new_last
            print('Contact successfully edited \n')
        elif edition == 'P' or edition == 'p':
            new_phone = input('Write the new Phone Number: ')
            data[edite_contact]['Phone Number'] = new_phone
            print('Contact successfully edited \n')
        else:
            print('Not valid option, please try again \n')
            return del_contact()
    elif confirmation == 'N' or confirmation == 'n':
        return del_contact()
    else:
        'Not valid option, please try again'
        return del_contact()

    with open('agenda.json', 'w') as outfile:
        json.dump(data, outfile)

    return start()


def del_contact():
    with open('agenda.json') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    print(df.loc[:, df.columns != 'N'])

    deleted_contact = int(input('Write the number position of the contact you want to delete: \n'))
    print(df.loc[deleted_contact])
    print('Is this the contact you want to delete? \n')

    confirmation = input('If yes write Y; if not write N \n')

    if confirmation == 'Y' or confirmation == 'y':
        data.pop(deleted_contact)
        print('Contact successfully deleted \n')
    elif confirmation == 'N' or confirmation == 'n':
        return del_contact()
    else:
        'Please try again \n'
        return del_contact()

    with open('agenda.json', 'w') as outfile:
        json.dump(data, outfile)

    return start()


def see_contact():
    with open('agenda.json') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    if data:
        print(df.loc[:, df.columns != 'N'])
    else:
        print('No contacts added yet.\n')
    return start()


start()
