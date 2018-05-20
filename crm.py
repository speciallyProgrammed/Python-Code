import sqlite3

conn = sqlite3.connect('EnergyCRM.db')
c = conn.cursor()

def beggining():
    print(" 1) New ")
    print(" 2) Load ")
    option = input(" --> ")
    if option == '1':
        create_table()
    if option == '2':
        start()

def create_table():
    c.execute("CREATE TABLE crm(name VARCHAR,number VARCHAR, email VARCHAR, job VARCHAR, date VARCHAR)")
    start()

def dynamic_data():
    name = input(" Enter Name Of Client: ")
    number = input(" Enter Phone Number For Client: ")
    email = input(" Enter Client Email: ")
    job = input(" Enter Client Job: ")
    date = input(" Enter Date: ")

    c.execute("INSERT INTO crm( name, number, email, job,date ) VALUES (?,?,?,?,?)",(name,number,email,job,date))
    conn.commit()
    start()

def start():
    print(" 1) Write Data ")
    print(" 2) Read Data ")
    option = input(" --> ")
    if option == '1':
        dynamic_data()
    if option == '2':
        read_from_database()


def read_from_database():
    print(" 1) Search by Name ")
    print(" 2) Search by Date ")
    print(" 3) Search by Email ")
    print(" 4) Search by Number ")
    print(" 5) Search by Job ")
    print(" 6) All ")
    option = input(" --> ")
    if option == '1':
        name = input(" Enter Name: ")
        sql = "SELECT * FROM crm WHERE name == ?"
        for row in c.execute(sql,[(name)]):
            print(" Name   Number   Email   Job     Date ")
            print(row)
    if option == '2':
        date = input(" Enter Date: ")
        sql = "SELECT * FROM crm WHERE date == ?"
        for row in c.execute(sql,[(date)]):
            print(" Name   Number   Email   Job     Date ")
            print(row)
    if option == '3':
        email = input(" Enter Email: ")
        sql = "SELECT * FROM crm WHERE email == ?"
        for row in c.execute(sql,[(email)]):
            print(" Name   Number   Email   Job     Date ")
            print(row)
    if option == '4':
        number = input(" Enter number: ")
        sql = "SELECT * FROM crm WHERE number == ?"
        for row in c.execute(sql,[(number)]):
            print(" Name   Number   Email   Job     Date ")
            print(row)
    if option == '5':
        job = input(" Enter Job: ")
        sql = "SELECT * FROM crm WHERE job == ?"
        for row in c.execute(sql,[(job)]):
            print(" Name   Number   Email   Job     Date ")
            print(row)
    if option == '6':
        sql = "SELECT * FROM crm"
        for row in c.execute(sql):
            print(" Name   Number   Email   Job     Date ")
            print(row)
    start()



beggining()
