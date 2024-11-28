contacts = {}


def is_in_contacts(name):
    return True if name in contacts else False


def add_contact(name, number):
    if not is_in_contacts(name):
        contacts[name] = number
        return 'Contact successfully added!'
    else:
        return (f'{name} is already in your contacts. If you want to charge number of {name}'
                f', use command \'change\'')


def charge_contact(name, number):
    if is_in_contacts(name):
        contacts[name] = number
        return 'Successfully changed'
    else:
        return (f'There is no contact {name} in your contacts. If you want to add this contact,'
                f'please use the command \'add\'')


def show_phone(name):
    if is_in_contacts(name):
        return contacts[name]
    else:
        return f'There is no {name} in your contacts'


def show_all_contacts():
    return contacts


