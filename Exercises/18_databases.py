import sqlite3
from _sqlite3 import OperationalError

"""
tablie is entity
column = attritube
row = instance
"""


def createTable_Customers():
    """createTable_Customers will create the database table(s)"""
    connection = sqlite3.connect("online_shares.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS customers')
    cursor.execute(
        "CREATE TABLE customers (cust_name TEXT, cust_password  TEXT, cust_cash INT, cust_invest INT)")
    connection.close()


def insert_initailDataSet():
    """insert_initailDataSet will add initial data to the database table(s)"""
    try:
        connection = sqlite3.connect("online_shares.db")
        cursor = connection.cursor()

        starter_accounts = [
            ("John", "password", 100, 20),
            ("Amy", "password", 50, 50),
            ("Matt", "password", 305, 50),
            ("Claire", "password", 0, 50)
        ]

        cursor.executemany(
            'INSERT INTO customers VALUES (?,?,?,?)', starter_accounts)
        connection.commit()
        print("Bulk rows added successfully")

    except OperationalError as errMsg:
        print(errMsg)
    except:
        print("error on INSERT many records at a time")
        connection.rollback()
    else:
        print("Success, no error!")
    finally:
        connection.close()


def createNewAccount(custName, custPassword, custCash, custInvest):
    """createNewAccount will add specified data to the database table(s)"""
    try:
        connection = sqlite3.connect("online_shares.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customers (custName, custPassword, custCash, custInvest)  VALUES (? , ? , ? , ?)",
                       (custName, custPassword, custCash, custInvest))
        connection.commit()
        print("one record added successfully")
    except OperationalError as errMsg:
        print(errMsg)
    except:
        print("error on INSERT")
        connection.rollback()
    else:
        print("Success, no error!")
    finally:
        connection.close()


createTable_Customers()
insert_initailDataSet()
