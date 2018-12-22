import mysql.connector


def connect():
    return mysql.connector.connect(user='root', password='sf@R!!!eee', database='experiments')

def execute(request):
    cnx = connect()
    cursor = cnx.cursor()
    print(request)
    cursor.execute(request)
    cnx.commit()
    cursor.close()


def drop_table(name):
    execute("DROP TABLE %s" % name)


def new_table(name, fields):
    spec = "id INT"
    for f in fields:
        spec += ", " + f[0] + " " + f [1]
    spec += ", PRIMARY KEY (id)"

    create_table = "CREATE TABLE %s (%s) ENGINE=InnoDB" % (name, spec)
    execute(create_table)
