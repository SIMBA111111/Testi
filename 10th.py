import sqlite3


class DB:
    def __init__(self, db_file="example.db"):
        self.conn = sqlite3.connect(db_file)
        self.create()

    def create(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            salary REAL NOT NULL
        )
        '''
        self.execute_query(query)

    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def add_employee(self, name, salary):
        query = 'INSERT INTO Employees (name, salary) VALUES (?, ?)'
        params = (name, salary)
        self.execute_query(query, params)

    def read_employees(self):
        query = 'SELECT * FROM Employees'
        cursor = self.execute_query(query)
        if cursor:
            return cursor.fetchall()
        else:
            return []

    def update_employee(self, employee_id, name, salary):
        query = 'UPDATE Employees SET name=?, salary=? WHERE id=?'
        params = (name, salary, employee_id)
        self.execute_query(query, params)

    def delete_employee(self, employee_id):
        query = 'DELETE FROM Employees WHERE id=?'
        params = (employee_id,)
        self.execute_query(query, params)

    def close_connection(self):
        self.conn.close()


db = DB()

db.add_employee("qwerty", 102992443)