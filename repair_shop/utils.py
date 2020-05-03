from prettytable import PrettyTable
import sqlite3

conn = sqlite3.connect('repair_shop.db')
c = conn.cursor()

valid_user_types = ['client', 'mechanic']

is_mechanic = None

cl_list = ['list_all_free_hours', 'list_free_hours <date>',
           'save_repair_hour', 'update_repair_hour',
           'delete_repair_hour', 'list_vehicles',
           'add_vehicle', 'update_vehicle', 'delete_vehicle', 'help']

mech_list = ['list_all_free_hours', 'list_free_hours <date>',
             'list_all_busy_hours', 'list_busy_hours <date>',
             'add_repair_hour', 'add_service', 'update_repair_hour <hour_id>', 'help']


def tabulate(col_names, rows):
    table = PrettyTable(col_names)

    for row in rows:
        table.add_row(row)

    return table


def help(username):
    if is_mechanic:
        commands = mech_list
    else:
        commands = cl_list

    print('\nHere\'s a list of avaliable commands:')
    for c in commands:
        print(c)
    print()


def list_all_free_hours(username):

    with conn:

        c.execute('''
            SELECT id, date, start_hour as time
            FROM RepairHour
            WHERE vehicle is NULL AND mechanic_service IS NULL;''')

        col_names = [cd[0] for cd in c.description]
        rows = c.fetchall()

    print(tabulate(col_names, rows))


def list_all_busy_hours(username):

    with conn:

        c.execute('''
            SELECT id, date, start_hour as time, vehicle, bill, mechanic_service as ms_id
            FROM RepairHour WHERE vehicle IS NOT NULL;''')

        col_names = [cd[0] for cd in c.description]
        rows = c.fetchall()

    print(tabulate(col_names, rows))


def list_free_hours(date):

    with conn:

        c.execute('''
            SELECT id, start_hour as time
            FROM RepairHour
            WHERE date is (?)
            AND vehicle IS NULL;''', (date,))

        col_names = [cd[0] for cd in c.description]
        rows = c.fetchall()

    print(tabulate(col_names, rows))


def list_busy_hours(date):

    with conn:

        c.execute('''
            SELECT id, start_hour as time, vehicle, bill, mechanic_service as ms_id
            FROM RepairHour
            WHERE date is (?)
            AND vehicle IS NOT NULL;''', (date,))

        col_names = [cd[0] for cd in c.description]
        rows = c.fetchall()

    print(tabulate(col_names, rows))


def add_repair_hour(username):
    rdate = input('Choose date (YYYY-MM-DD):\n')
    rtime = input('Enter hour (HH:MM):\n')

    with conn:

        c.execute('''
            INSERT INTO RepairHour(date, start_hour)
            VALUES (?,?);''', (rdate, rtime))

    print('\nYou\'ve created a new reapair hour!')
    list_all_free_hours()


def save_repair_hour(hr_id, username):
    print('Choose vehicle to repair:')

    with conn:
        c.execute('''
            SELECT Vehicle.id,
            make || ' ' || model || ' with RegNo: ' || reg_no as vehicle
            FROM Vehicle
            JOIN BaseUser ON BaseUser.id = Vehicle.owner
            WHERE username = (?);''', (username,))

        col_names = [cd[0] for cd in c.description]
        rows = c.fetchall()

    print(tabulate(col_names, rows))
    veh_id = int(input())

    with conn:
        c.execute('''
            SELECT make || ' ' || model || ' with RegNo: ' || reg_no
            FROM Vehicle
            WHERE id = (?)''', (veh_id,))

        veh_name = c.fetchone()

    print('Choose service:')

    with conn:
        c.execute('SELECT * FROM Service')

        col_names = [cd[0] for cd in c.description]
        rows = c.fetchall()

    print(tabulate(col_names, rows))
    serv_id = int(input())

    with conn:
        c.execute('SELECT name FROM Service WHERE id = (?)', (serv_id,))
        serv_name = c.fetchone()

    with conn:
        c.execute('''
            UPDATE RepairHour
            SET vehicle = (?),
                mechanic_service = (SELECT id
                                    FROM MechanicService
                                    WHERE service_id = (?))
            WHERE id = (?);''', (veh_id, serv_id, hr_id))

    with conn:
        c.execute('SELECT date, start_hour FROM RepairHour WHERE id = (?)', (hr_id,))
    rdate_time = c.fetchone()

    print(f'\nThank you! You\'ve saved and hour on {rdate_time[0]} at {rdate_time[1]} for {serv_name[0]}!')
    print(f'Vehicle: {veh_name[0]}')


def update_repair_hour(hr_id, username):

    with conn:
        c.execute('''
            SELECT date, start_hour, username, make || ' ' || model, bill
            FROM RepairHour
            JOIN Vehicle on vehicle.id = RepairHour.vehicle
            JOIN BaseUser on BaseUser.id =Vehicle.owner
            WHERE RepairHour.id = (?);''', (hr_id,))

        rhour = c.fetchone()

    print(f'''
On {rhour[0]} at {rhour[1]}:
Client: {rhour[2]}
Vehicle: {rhour[3]}
Current Bill: {rhour[4]}
Choose one of the following:
1 - change start hour
2 - change bill
3 - return to main menu''')

    choice = input()
    if choice == '1':
        print(f'Current start hour is {rhour[1]}.')
        new_hr = input('New start hour: ')

        with conn:
            c.execute('UPDATE RepairHour SET start_hour = (?) WHERE id = (?);', (new_hr, hr_id))

    elif choice == '2':
        print(f'Current bill is {rhour[4]}.')
        new_bill = input('New bill: ')

        with conn:
            c.execute('UPDATE RepairHour SET bill = (?) WHERE id = (?);', (new_bill, hr_id))

    elif choice == '3':
        pass


def delete_repair_hour(hr_id, username):

    with conn:
        c.execute('''
            UPDATE RepairHour
            SET vehicle = NULL,
                bill = NULL,
                mechanic_service = NULL
            WHERE id = (?)''', (hr_id,))


def add_service(username):
    new_serv_name = input('Provide new service name: ')
    with conn:
        c.execute('INSERT INTO Service(name) VALUES (?)', (new_serv_name,))


def list_vehicles(username):
    with conn:
        c.execute('''
            SELECT Vehicle.id as id, make || ' ' || model as vehicle, reg_no
            FROM Vehicle
            JOIN BaseUser ON BaseUser.id = Vehicle.owner
            WHERE username = (?);''', (username,))

        col_names = [cd[0] for cd in c.description]
        rows = c.fetchall()

    print(tabulate(col_names, rows))


def add_vehicle(username):
    with conn:
        c.execute('SELECT id FROM BaseUser WHERE username = (?)', (username,))
        owner = c.fetchone()

    cat = input('Enter category: ')
    make = input('Enter make: ')
    model = input('Enter model: ')
    reg_no = input('Enter registration number: ')
    gbox = input('Enter gearbox type: ')

    details = (cat, make, model, reg_no, gbox, owner[0])

    with conn:
        c.execute('''
            INSERT INTO Vehicle(category, make, model, reg_no, gear_box, owner)
            VALUES(?,?,?,?,?,?);''', details)


def update_vehicle(veh_id, username):

    with conn:
        c.execute('''
            SELECT make || ' ' || model, reg_no, gear_box
            FROM Vehicle
            WHERE id = (?)''', (veh_id,))
        vehicle = c.fetchone()

    print(f'''
{vehicle[0]} with reg.no. {vehicle[1]} and a {vehicle[2]} gear box.
Choose one of the following:
1 - change registration number
2 - change gear box type
3 - return to main menu''')

    choice = input()
    if choice == '1':
        print(f'Current reg. no. is {vehicle[1]}.')
        new_rn = input('New reg. no: ')

        with conn:
            c.execute('UPDATE Vehicle SET reg_no = (?) WHERE id = (?);', (new_rn, veh_id))

    elif choice == '2':
        print(f'Current gearbox is {vehicle[2]}.')
        new_gb = input('New gearbox: ')

        with conn:
            c.execute('UPDATE Vehicle SET gear_box = (?) WHERE id = (?);', (new_gb, veh_id))

    elif choice == '3':
        pass


def delete_vehicle(veh_id, username):
    with conn:
        c.execute('DELETE FROM Vehicle WHERE id = (?)', (veh_id,))


def create_new_user(username):
    typ = input('Are you a client or a mechanic?\n')
    assert typ.lower() in valid_user_types, f'{typ} is not a valid user type.'

    if typ.lower() == 'mechanic':
        title = input('Enter your title: ')

    username = input('Enter a username: ')
    email = input('Enter an email: ')
    phone = input('Enter a phone number: ')
    address = input('Enter your address: ')

    with conn:

        conn.execute('''
            INSERT INTO BaseUser(username, email, phone, address)
            VALUES (?,?,?,?)''', (username, email, phone, address))

        c.execute('SELECT id FROM BaseUser WHERE username=?', (username,))
        ajdi = c.fetchone()

        if typ.lower() is 'client':
            conn.execute('INSERT INTO Client(base_id) VALUES (?)', ajdi[0])
        else:
            conn.execute('INSERT INTO Mechanic(base_id, title) VALUES (?, ?)', (ajdi[0], title))


def is_mechanic(username):
    with conn:
        c.execute('SELECT id FROM BaseUser WHERE username = ?', (username,))
        ajdi = c.fetchone()

        c.execute('SELECT * FROM Mechanic WHERE base_id = ?', ajdi)
        result = c.fetchone()

        if result is None:
            is_mechanic = False
            return is_mechanic
        else:
            is_mechanic = True
            return is_mechanic


def does_exist(username):

    with conn:
        c.execute('SELECT * FROM BaseUser WHERE username = ?', (username,))
        result = c.fetchone()

        if result is None:
            return False
        else:
            return True


def login(username):
    print('Hello! Please enter your username:')
    username = input()

    if does_exist(username) and is_mechanic(username):
        return username, True

    elif does_exist(username):
        return username, False

    else:

        while True:
            print('Would you like to create a new user? (y/n)')
            ans = input()

            if ans.lower() == 'y':
                create_new_user()
                print('Next time, log in with your new username.')
                return

            elif ans.lower() == 'n':
                print('Ok, bye!')
                return

            else:
                print('Please, enter "y" or "n"!')
