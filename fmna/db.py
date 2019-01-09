import mysql.connector

import fmna.experiment as exp


def connect():
    return mysql.connector.connect(user='root', password='sf@R!!!eee', database='experiments')


def update(request):
    cnx = connect()
    cursor = cnx.cursor()
    print(request)
    cursor.execute(request)
    cursor.close()
    cnx.commit()


def drop_table():
    try:
        update("DROP TABLE %s" % exp.table_name())
    except mysql.connector.errors.ProgrammingError:
        print("Failed to drop table")


def new_table(fields):
    spec = "id INT NOT NULL AUTO_INCREMENT"
    for f in fields:
        spec += ", " + f[0] + " " + f[1]
    spec += ", PRIMARY KEY (id)"

    create_table = "CREATE TABLE %s (%s) ENGINE=InnoDB" % (exp.table_name(), spec)
    update(create_table)


def insert(values):
    insert = "INSERT INTO %s (%s) VALUES (%s)" % (
        exp.table_name(),
        ",".join(map(lambda v: v[0], values)),
        ",".join(map(lambda v: str(v[1]), values)))
    update(insert)


def load(what="*", where=""):
    request = "SELECT %s FROM %s" % (what, exp.table_name())
    if len(where) > 0:
        request += " WHERE %s" % where

    print(request)
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(request)
    return cursor.fetchall()


def arbitrary_select(request):
    print(request)
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(request)
    return cursor.fetchall()
