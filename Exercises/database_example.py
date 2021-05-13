import sqlite3
from _sqlite3 import OperationalError


class Banking:
    """Banking application will manage database connectivity"""

    def __init__(self):
        """This initialiser/class constructor will create the database currency_manager.db, if it doesn't exist and open a connection to it"""
        connection = sqlite3.connect("currency_manager.db")
        cursor = connection.cursor()

    def welcomeMessage(self):
        """welcomeMessage will print a welcome message"""
        print("\nWelcome to Banking Management Software!\n")

    def createTable_Customers(self):
        """createTable_Customers will create the database table(s)"""
        connection = sqlite3.connect("currency_manager.db")
        cursor = connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS customers')
        cursor.execute(
            "CREATE TABLE customers (cust_id  INTEGER, cust_name TEXT, currentAcc_num  INTEGER, SavingAcc_num  INTEGER)")
        connection.close()

    def insert_initailDataSet(self):
        """insert_initailDataSet will add initial data to the database table(s)"""
        try:
            connection = sqlite3.connect("currency_manager.db")
            cursor = connection.cursor()

            starter_accounts = [
                (710, "Matt", 334003, 5162022),
                (510, "Jon", 334004, 5162032),
                (310, "Liz", 334005, 5162042),
                (220, "Beth", 334006, 5162052),
                (880, "Tom", 334007, 5162062),
                (500, "Judith", 334008, 5162072),
                (290, "Raymond", 334009, 5162082),
                (420, "Frances", 334010, 5162020)
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

    def createNewAccount(self, custId, custName, currentAcc, SavingAcc):
        """createNewAccount will add specified data to the database table(s)"""
        try:
            connection = sqlite3.connect("currency_manager.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO customers (cust_id, cust_name, currentAcc_num, SavingAcc_num)  VALUES (? , ? , ? , ?)",
                           (custId, custName, currentAcc, SavingAcc))
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

    def fetchAllAccount(self):
        """fetchAllAccount will fetch/select all the data in the table"""
        rowSet = ()

        try:
            connection = sqlite3.connect("currency_manager.db")
            cursor = connection.cursor()
            rowSet = cursor.execute(
                "SELECT cust_id, cust_name, currentAcc_num, SavingAcc_num FROM customers").fetchall()
        except OperationalError as errMsg:
            print(errMsg)
        except:
            print("error on Fetch")
            connection.rollback()
        finally:
            connection.close()
            return rowSet

    def fetchAccountId_first(self):
        """fetchAccountId_first will fetch/select the first account that was created/ has the smallest id """
        rowSet = ()

        try:
            connection = sqlite3.connect("currency_manager.db")
            cursor = connection.cursor()
            rowSet = cursor.execute(
                "SELECT MIN(cust_id) FROM customers").fetchall()
        except OperationalError as errMsg:
            print(errMsg)
        except:
            print("error on Fetch")
            connection.rollback()
        finally:
            connection.close()
            return rowSet

    def fetchAccountId_Highest(self):
        """fetchAccountId_Highest will fetch/select last account created/ most recent/lastest id """
        rowSet = ()

        try:
            connection = sqlite3.connect("currency_manager.db")
            cursor = connection.cursor()
            rowSet = cursor.execute(
                "SELECT MAX(cust_id) FROM customers").fetchall()
        except OperationalError as errMsg:
            print(errMsg)
        except:
            print("error on Fetch")
            connection.rollback()
        finally:
            connection.close()
            return rowSet

    def fetchAccount_By_Id(self, findThis_id):
        """ fetchAccount_By_Id will fetch / select matching data for the specified id. """

        rowSet = ()

        try:
            connection = sqlite3.connect("currency_manager.db")
            cursor = connection.cursor()
            rowSet = cursor.execute(
                "SELECT cust_id, cust_name, currentAcc_num, SavingAcc_num FROM customers WHERE cust_id = ?",
                (findThis_id,),
            ).fetchall()
        except OperationalError as errMsg:
            print(errMsg)
        except:
            print("error on Fetch")
            connection.rollback()
        finally:
            connection.close()
            return rowSet

    def fetchAccount_By_Name(self, findThis_name):
        """fetchAccount_By_Name will fetch/select matching data for the specified name"""
        rowSet = ()

        try:
            connection = sqlite3.connect("currency_manager.db")
            cursor = connection.cursor()
            rowSet = cursor.execute(
                "SELECT cust_id, cust_name, currentAcc_num, SavingAcc_num FROM customers WHERE cust_name = ?",
                (findThis_name,),
            ).fetchall()
        except OperationalError as errMsg:
            print(errMsg)
        except:
            print("error on Fetch")
            connection.rollback()
        finally:
            connection.close()
            return rowSet

    def UpdateAccount_Detail(self, findThis_id,  New_name):
        """UpdateAccount_Detail will Update customer name for the given ID"""

        try:
            connection = sqlite3.connect("currency_manager.db")
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE customers SET  cust_name   = :who  WHERE cust_id = :whoseID",
                {"who": New_name, "whoseID": findThis_id}
            )
            connection.commit()
            print("Account_Detail for:",  findThis_id, " Updated successfully")

        except OperationalError as errMsg:
            print(errMsg)
        except:
            print("error on INSERT")
            connection.rollback()
        else:
            print("Success, no error!")
        finally:
            connection.close()

    def DeleteAccount_Record(self, findThis_id):
        """DeleteAccount_Record will delete row by id"""

        try:
            connection = sqlite3.connect("currency_manager.db")
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM customers WHERE cust_id = ?", (findThis_id,))
            connection.commit()
            print("Account_Detail for:",  findThis_id,
                  " has been deleted successfully")

        except OperationalError as errMsg:
            print(errMsg)
        except:
            print("error on INSERT")
            connection.rollback()
        else:
            print("Success, no error!")
        finally:
            connection.close()


'''

test1 = Banking()
test1.welcomeMessage() 

#### One-off or reset #### 
test1.createTable_Customers()    
test1.insert_initailDataSet()


help(test1)
'''
