Explanation of the application

Requirements:
- Have Docker installed
- Have python installed
- Have python added in system environment variables
- Basic knowledge of functions in python
- Basic knowledge of a database

Preparation and Execution (for windows system):
- Preparation of the environment
Inside the init folder, open a powershell window and execute the "docker-compose up" command, this will start the execution environment in docker, once you finish executing this command in the docker window, the "init" environment will appear with 2 services started, pgAdmin (It is an interface to access databases) and postgres (which is the database engine), postgres .
In the case of python, an extra library is needed to make use of postgres, which is downloaded with the command "pip install psycopg2" that is executed in the powershell console

- Execution:
The .py file contains the functions to use, you can execute them one by one by writing them at the end of the file or you can simply execute the file with the python compiler in the console with "python main.py"
For this case, the connect function will start and call the others, establish the connection with postgres and create the tables and their attributes, there are update, delete and insert functions, you can manipulate 'connect' function order execution 

You can see the changes using pgAdmin which you can access from a browser, in the address bar go to "localhost:80" this will open the pgAdmin interface and ask for a credential
username: admin@admin.com
password: admin
pgAdmin will need the credentials to connect to postgres: these are just 'root'.
Once the connection is established, you can verify the databases from the interface, these will be: 'postgres' and 'config_DB' inside this one are the tables created from python file code.
Make sure docker has both services started from the created container called 'init'