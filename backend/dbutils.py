import pymysql
###### https://www.db4free.net/phpMyAdmin/index.php

# Connect to the database
connection = pymysql.connect(host='db4free.net',
                             user='itccohort19',
                             password='bootcamp',
                             db='pymonsquad',
                             charset='utf8',
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)



def getCursor(sql):
    result = 0
    try:
        with connection.cursor() as cursor:
            result = cursor.execute(sql)
    except Exception as e:
        print(repr(e))
        pass
    return result

#Run a DB query that expects a list of results
def queryAll(sql):
    result = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(repr(e))
        pass
    return result

#Run a DB query that expects one result
def queryOne(sql):
    result = None
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
    except Exception as e:
        print(repr(e))
        pass
    return result

def updateOrInsert(sql):
    success = False
    try:
        with connection.cursor() as cursor:
            success = cursor.execute(sql)
    except Exception as e:
        print(repr(e))
        pass
    return success

def delete_game(id):
    try:
        with connection.cursor() as cur:
            sql = "Select status From game Where id = {}".format(id)
            cur.execute(sql)
            status = cur.fetchone()
            if status['status'] == "open":
                sqlplayers = "Select game From playergame Where game = {}".format(id)
                cur.execute(sqlplayers)
                players = cur.fetchone()
                if players:
                    sqlchild = "Delete From playergame Where game = {}".format(id)
                    cur.execute(sqlchild)
                    sqlparent = "Delete From game Where id = {}".format(id)
                    cur.execute(sqlparent)
                else:
                    sql = "Delete From game Where id = {}".format(id)
                    cur.execute(sql)
            else:
                sqlchild = "Delete From playergame Where game = {}".format(id)
                cur.execute(sqlchild)
                sqlparent = "Delete From game Where id = {}".format(id)
                cur.execute(sqlparent)
            connection.commit()
            return {"Status": "Successfully Deleted game {}".format(id)}
    except:
        return {"Status":"Error in deleting game {}".format(id)}
