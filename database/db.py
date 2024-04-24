import pymysql

db_host = "127.0.0.1"
db_user = "root"
db_passw = "12345"
db_name = "db_users_131"

def connectionSQL():
    try:
        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_passw,
            database= db_name
        )
        print("Succesfull Connection to the database")
        return connection
    except:
        print("Error connecting to the database")
        return None

def insert_record():
    instruction = "INSERT INTO users VALUES (452, 'jonier', 'porras', '7852')"
    connection = connectionSQL()
    cursor = connection.cursor()
    try:
        cursor.execute(instruction)
        connection.commit()
        print("The user was created")
    except:
        print("Error creating the user")