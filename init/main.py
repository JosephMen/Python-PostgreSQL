#!/usr/bin/python
import psycopg2
from config import config

# Global constant
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "root"
PSQL_PASS = "root"
PSQL_DB = "root"

# Connection
connection_address = """
host=%s port=%s user=%s password=%s dbname=%s
""" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
connection = psycopg2.connect(connection_address)

#cursor = connection.cursor()

# # Query
# SQL = "SELECT * FROM Distro;"
# cursor.execute(SQL)

# # Get Values
# all_values = cursor.fetchall()

# cursor.close()
# connection.close()

# print('Get values: ', all_values)
