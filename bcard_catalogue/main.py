from sql_funcs import *
create_db()
fill_empty_db()

supported_commands = {
    'add': add,
    'list': list_contacts,
    'delete': delete,
    'get': get,
    'help': hlp,
    'quit': None
}

print('''
Hello! This is your business card catalog. What would you like to do?
(enter "help" to list all available options)
''')


def main():

    while True:

        command = input('Enter command: ')

        if command not in supported_commands:
            print(f'"{command}" is not a supported command.')

        elif command == 'quit':
            break
        else:
            supported_commands[command]()

    print('''
Closing catalogue. Bye!
''')


if __name__ == '__main__':
    main()
