#!/usr/bin/python
from cmath import e
import psycopg2

#variables
# customer_id
# first_name
# last_name
# email
# addres_id
# active
# create_date
# last_update

def connect():
    # Global constant
    PSQL_HOST = "localhost"
    PSQL_PORT = "5432"
    PSQL_USER = "root"
    PSQL_PASS = "root"
    PSQL_DB = "root"

    try:
        # Connection
        connection_address = """
        host=%s port=%s user=%s password=%s dbname=%s
        """ % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
        connection = psycopg2.connect(connection_address)
        cursor01 = connection.cursor()
        #create_table(cursor01)
        # insert(cursor01)
        # insert(cursor01)
        # delete(cursor01, 1)
        update(cursor01,customer_id=13, first_name="Joseph")
        connection.commit()

    except Exception as err:
        print("Somenthing went wrong: ", err)
    connection.close()

############################################################################################
############################################################################################
############################################################################################

def insert(cursor):
    command = """
        insert into customer2(first_name) values('frander')
    """
    cursor.execute(command)
    print("insertion succesfull")

def delete(cursor, id=1):
    command = """
        delete from customer2 
        where customer_id = '%s'
    """ % (id)
    cursor.execute(command)
    print("Deleted succesfull")

def update(cursor, customer_id=1, first_name="", last_name="", address_id="",email=""):
    command = """
        update customer2
        set first_name='%s', 
            last_name='%s', 
            address_id='%s', 
            email='%s'
        where customer_id='%s'
    """ % (first_name, last_name, address_id, email, customer_id)
    cursor.execute(command)
    print("Updated succesfull")

def create_table(cursor):
    command = """
        CREATE TABLE if not exists customer2 (
            customer_id SERIAL PRIMARY KEY,
            first_name VARCHAR,
            last_name VARCHAR,
            email VARCHAR,
            address_id VARCHAR,
            active BOOLEAN DEFAULT TRUE,
            create_date DATE DEFAULT CURRENT_DATE,
            update_date TIMESTAMP DEFAULT now()
        )
    """
    cursor.execute(command)
    print("table created!")

def create_trigger(cursor):

    print("Trigger created !")


connect()
