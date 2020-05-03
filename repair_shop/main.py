from utils import *

cl_commands = {
    'list_all_free_hours': list_all_free_hours,
    'list_free_hours': list_free_hours,
    'save_repair_hour': save_repair_hour,
    'update_repair_hour': update_repair_hour,
    'delete_repair_hour': delete_repair_hour,
    'list_vehicles': list_vehicles,
    'add_vehicle': add_vehicle,
    'update_vehicle <vehicle id>': update_vehicle,
    'delete_vehicle': delete_vehicle,
    'help': help
}

mech_commands = {
    'list_all_free_hours': list_all_free_hours,
    'list_free_hours': list_free_hours,
    'list_all_busy_hours': list_all_busy_hours,
    'list_busy_hours': list_busy_hours,
    'add_repair_hour': add_repair_hour,
    'add_service': add_service,
    'update_repair_hour <hour_id>': update_repair_hour,
    'help': help
}


def main():

    start = login()
    username = start[0]
    user_is_mechanic = start[1]
    print(f'Hi, {username}!\n')

    if user_is_mechanic:
        supported = mech_commands
    else:
        supported = cl_commands

    while True:

        command = input('Enter a command (help): ')

        if command == 'exit':
            break

        elif command in supported:
            supported[command](username)

        elif ' ' in command:
            com = command.split(' ')[0]
            arg = command.split(' ')[1]

            if com in supported:
                supported[com](arg, username)
            else:
                print(f'{com} is not a supported command')
                print()

        else:
            print(f'{command} is not a supported command')
            print()


if __name__ == '__main__':
    main()
