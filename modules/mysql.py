import mysql.connector
from app.config import db

db = mysql.connector.connect(
    host = db.DB_HOST,
    user = db.DB_USER,
    password = db.DB_PASS,
    database = db.DB_NAME 
)

queryTypes = ('INSERT', 'SELECT', 'UPDATE', 'DELETE')

def Query(statement:str, all:bool = False):

    if not statement:
        raise Exception("Error statement")
    
    queryType = statement.split(' ')[0].upper()

    if ( queryType in queryTypes ) == False:
        raise Exception("Query error")

    cursor = db.cursor()
    cursor.execute(statement)

    if queryType == ('INSERT' or 'UPDATE' or 'DELETE'):
        return db.commit()
    else:
        if all == True:
            return cursor.fetchall()
        else:
            return cursor.fetchone()