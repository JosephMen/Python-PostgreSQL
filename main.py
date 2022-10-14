from typing import Optional
from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel
from typing import Text

app = FastAPI()

# Global constant 
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "root"
PSQL_PASS = "root"
PSQL_DB = "config_DB"

try:
    # Connection
    connection_address = """
    host=%s port=%s user=%s password=%s dbname=%s
    """ % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
    connection = psycopg2.connect(connection_address)
    cursor01 = connection.cursor()
    # delete(cursor01, 1)

except Exception as err:
    print("Somenthing went wrong: ", err)

##############################################################
#Function section for data base interaction

class Body(BaseModel):
    first_name: Optional[str] = "None"
    last_name: Optional[str] = "None"
    address_id: Optional[str] = "None"
    email: Optional[str] = "None"

def insert_post(first_name : str, last_name : str, address_id : str, email : str):
    command = """
        insert into customer2(first_name, last_name, address_id, email) values('%s','%s','%s','%s');
    """ % (first_name, last_name, address_id, email)
    cursor01.execute(command)
    print("insertion succesfull")

def delete_post(id):
    command = """
        delete from customer2 
        where customer_id = '%s';
    """ % (id)
    cursor01.execute(command)
    print("Deleted succesfull")

def update_post(customer_id, first_name="", last_name="", address_id="",email=""):
    command = """
        update customer2
        set first_name='%s', 
            last_name='%s', 
            address_id='%s', 
            email='%s'
        where customer_id='%s';
    """ % (first_name, last_name, address_id, email, customer_id)
    cursor01.execute(command)
    print("Updated succesfull")

def create_customer_table():
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
        );
    """
    cursor01.execute(command)
    print("table created!")

def create_configuration_table():
    command = """
        CREATE TABLE if not exists ConfigurationTable(
            client_id INTEGER,
            client_url TEXT,
            metric BOOLEAN DEFAULT FALSE,
            planning BOOLEAN DEFAULT FALSE,
            clustering BOOLEAN DEFAULT FALSE,
            valve_critically BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (client_id) 
                REFERENCES customer2(customer_id)
        );
    """
    cursor01.execute(command)
    print("Configuration table created succesfull")

def create_trigger():
    command = """
        create or replace function update_customer2() returns Trigger 
        as
        $$
        begin 
        new.update_date := now();
        return new;
        end
        $$
        language plpgsql;

        create trigger update_trigger_customer 
            after update on customer2
            for each row
            execute procedure update_customer2();
    """
    cursor01.execute(command)
    print("Trigger created !")
###############################################################
#EndPoint section

#Basic hello world
@app.get("/")
def read_root():
    return {"Hello": "World"}

#Endpoint for create tables
@app.post("/create_table/")
def create_tables():
    create_customer_table()
    create_trigger()
    create_configuration_table()


#Endpoint for post
@app.post("/")
def insert_cust(body:Body):

    try:
        insert_post( 
            first_name  =   body.first_name, 
            last_name   =   body.last_name, 
            address_id  =   body.address_id, 
            email       =   body.email)
        connection.commit()
    except Exception as err:
        print("Something went wrong: ")


    print("Insert customer")
    return {
        "first_name": body.first_name, 
        "last_name":body.last_name, 
        "address_id": body.address_id, 
        "email": body.email}

#Endpoint for put
@app.put("/{id_customer}")
def update_cust(id_customer,body:Body):

    try:
        update_post(
            customer_id =   id_customer,
            first_name  =   body.first_name,
            last_name   =   body.last_name,
            address_id  =   body.address_id,
            email       =   body.email)
        connection.commit()

    except Exception as err:
        print("Something went wrong: ")

    print("Update customer")
    return {
        "first_name":   body.first_name, 
        "last_name":    body.last_name, 
        "address_id":   body.address_id, 
        "email":        body.email}

#Endpoint for delete customer
@app.delete("/{id_customer}")
def delete_cust(id_customer : str):

    try:
        delete_post(id_customer)
        connection.commit()

    except Exception as err:
        print("Something went wrong: ")


    print("Deleted customer")
    return {"deleted":id_customer}


