import sqlite3


def create_db():
    connection = sqlite3.connect('bcards.db')
    cursor = connection.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS User(
           id INTEGER PRIMARY KEY,
           full_name VARCHAR(50) NOT NULL UNIQUE,
           email VARCHAR(50) NOT NULL UNIQUE,
           age INTEGER NOT NULL,
           phone VARCHAR(10) NOT NULL,
           additional_info TEXT
           );
        '''
    )

    connection.commit()
    connection.close()


def fill_empty_db():
    connection = sqlite3.connect('bcards.db')
    cursor = connection.cursor()

    cursor.execute(
        '''
        SELECT * FROM User
        '''
    )
    contact_list = cursor.fetchall()
    if contact_list:
        pass
    else:
        cursor.execute(
            '''
            INSERT INTO User(
              full_name, email, age, phone, additional_info)
              VALUES
              ('Pesho Koftito', 'mnogo@losho.bg', 30, '1234567890', NULL),
              ('Grigor Gligana', 'gligi@abv.bg', 23, '0987654321', 'Brat na Kofti'),
              ('Tosho Grebeca', 'grebna_baza@plovdiv.bg', 32, '1234509876', NULL),
              ('Toni Garderoba', 'paz@gtk.com', 50, '6789054321', NULL),
              ('Gosho Pateto', 'kva@kva.kva', 12, '0987612345', NULL);
            '''
        )

    connection.commit()
    connection.close()


def add():
    connection = sqlite3.connect('bcards.db')
    cursor = connection.cursor()

    name = input('Enter contact name: ')
    email = input('Enter email: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    add_info = input('Enter additional info (optional): ')

    if add_info == '':
        add_info = None

    insert_query = f'''
    INSERT INTO User(full_name, email, age, phone, additional_info)
      VALUES(?, ?, ?, ?, ?)
    '''

    cursor.execute(insert_query, (name, email, age, phone, add_info))

    connection.commit()
    connection.close()


def list_contacts():
    connection = sqlite3.connect('bcards.db')
    cursor = connection.cursor()

    cursor.execute(
        '''
        SELECT * FROM User
        '''
    )
    contact_list = cursor.fetchall()

    print('''
###################
# C O N T A C T S #
###################
''')

    for c in contact_list:
        print(f'ID: {c[0]}, Email: {c[2]}, Full name: {c[1]}')
    print()

    connection.commit()
    connection.close()


def get_contact_details():
    connection = sqlite3.connect('bcards.db')
    cursor = connection.cursor()

    select_query = f'''
    SELECT * FROM User
    WHERE id = ?;
    '''

    ajdi = input('Enter ID: ')

    cursor.execute(select_query, ajdi)
    contact_details = cursor.fetchall()

    connection.commit()
    connection.close()
    return contact_details


def delete():
    connection = sqlite3.connect('bcards.db')
    cursor = connection.cursor()

    delete_query = f'''
    DELETE FROM User
    WHERE id = ?;
    '''

    contact_details = get_contact_details()
    ajdi = str(contact_details[0][0])

    cursor.execute(delete_query, ajdi)

    print(f'''
The following contact has been deleted successfully:
    ID: {contact_details[0][0]},
    Full name: {contact_details[0][1]},
    Email: {contact_details[0][2]},
    Age: {contact_details[0][3]},
    Phone: {contact_details[0][4]},
    Additional info: {contact_details[0][5]}
    ''')

    connection.commit()
    connection.close()


def get():

    contact_details = get_contact_details()

    print(f'''
Contact Information:
    ID: {contact_details[0][0]},
    Full name: {contact_details[0][1]},
    Email: {contact_details[0][2]},
    Age: {contact_details[0][3]},
    Phone: {contact_details[0][4]},
    Additional info: {contact_details[0][5]}
    ''')


def hlp():

    print('''
#################
# O P T I O N S #
#################

1. 'add':    Insert a new business card.
2. 'list':   List all business cards.
3. 'delete': Delete a certain business card ('ID' is required).
4. 'get':    Display full information for a certain business card ('ID' is required).
5. 'help':   List all available options.

''')
