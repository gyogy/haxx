import sqlite3

conn = sqlite3.connect('repair_shop.db')

base_users = [(1, 'Petya', 'poshta@petya.org', '0888777888', 'Sofia, 1111'),
              (2, 'Todor Kolev', 'todor@amerikancite.bg', '0898908090', 'ul. Petar Delyan 13'),
              (3, 'Gosho', None, '0877665544', 'Mladost 3, bl. 10'),
              (4, 'Kiko Pecev', 'kimonli@gmail.com', '0883361507', '28 Lomschtrasse')]

clients = [(1,), (3,)]

vehicles = [(1, 'Sedan', 'Audi', 'A4', 'CO1234PK', 'Manual', 1),
            (2, 'SUV', 'BMV', 'X5', 'CO4321PK', 'Automatic', 1),
            (3, 'Banicamobile', 'Renault', 'Kangoo', 'B00B135', 'Manual', 3)]

mechanics = [(2, 'Senior Mechanic'),
             (4, 'Junior Mechanic')]

services = [(1, 'Oil change'), (2, 'Diagnostics'), (3, 'Transmission transplant')]

mechs_servs = [(1, 4, 1), (2, 4, 2), (3, 2, 3)]

hours = [(1, '2020-05-01', '09:00', 2, 0, 2),
         (2, '2020-05-01', '10:30', 3, 75, 1),
         (3, '2020-05-02', '10:30', None, None, None),
         (4, '2020-05-04', '06:00', 3, 75, 1),
         (5, '2020-05-05', '14:45', None, None, None),
         (6, '2020-05-06', '22:30', 3, 75, 1),
         (7, '2020-05-15', '09:00', 2, 2000, 3)]


# params[x] = (table name, column count, row values)
params = [('BaseUser', '(?,?,?,?,?)', base_users),
          ('Client', '(?)', clients),
          ('Vehicle', '(?,?,?,?,?,?,?)', vehicles),
          ('Mechanic', '(?,?)', mechanics),
          ('Service', '(?,?)', services),
          ('MechanicService', '(?,?,?)', mechs_servs),
          ('RepairHour', '(?,?,?,?,?,?)', hours)]


def create_tables():

    with conn:
        conn.executescript(
            '''
            CREATE TABLE IF NOT EXISTS BaseUser(
            id INTEGER PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            email VARCHAR(50),
            phone VARCHAR(10),
            address TEXT
            );

            CREATE TABLE IF NOT EXISTS Client(
            base_id INTEGER NOT NULL,
            FOREIGN KEY(base_id) REFERENCES BaseUser(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS Vehicle(
            id INTEGER PRIMARY KEY,
            category VARCHAR(20) NOT NULL,
            make VARCHAR(20) NOT NULL,
            model VARCHAR(20) NOT NULL,
            reg_no VARCHAR(20) UNIQUE NOT NULL,
            gear_box VARCHAR(20) NOT NULL,
            owner INTEGER NOT NULL,
            FOREIGN KEY(owner) REFERENCES Client(base_id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS Mechanic(
            base_id INTEGER NOT NULL,
            title VARCHAR(30),
            FOREIGN KEY(base_id) REFERENCES BaseUser(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS Service(
            id INTEGER PRIMARY KEY,
            name VARCHAR(30)
            );

            CREATE TABLE IF NOT EXISTS MechanicService(
            id INTEGER PRIMARY KEY,
            mechanic_id INTEGER NOT NULL,
            service_id INTEGER NOT NULL,
            FOREIGN KEY(mechanic_id) REFERENCES Mechanic(base_id) ON DELETE SET NULL,
            FOREIGN KEY(service_id) REFERENCES Service(id) ON DELETE SET NULL
            );

            CREATE TABLE IF NOT EXISTS RepairHour(
            id INTEGER PRIMARY KEY,
            date VARCHAR(10) NOT NULL,
            start_hour VARCHAR(5) NOT NULL,
            vehicle INTEGER,
            bill REAL,
            mechanic_service INTEGER,
            FOREIGN KEY(vehicle) REFERENCES Vehicle(id) ON DELETE CASCADE,
            FOREIGN KEY(mechanic_service) REFERENCES MechanicService(id) ON DELETE SET NULL
            );'''
        )


def fill_empty_tables():
    c = conn.cursor()

    for p in params:

        with conn:
            c.execute(f'SELECT * FROM {p[0]}')
            contents = c.fetchall()

            if contents == []:
                conn.executemany(f'INSERT INTO {p[0]} VALUES {p[1]}', p[2])


if __name__ == '__main__':
    create_tables()
    fill_empty_tables()
