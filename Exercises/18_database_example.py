import database_example as db


# Global variable to store initial DB values, can then be use and incremented as needed
first_Cust = 0
Latest_Cust_ID = 0


def startApp():
    option = ""

    theBank = db.Banking()
    theBank.welcomeMessage()

    for row in theBank.fetchAccountId_first():
        first_Cust = row[0]

    for row in theBank.fetchAccountId_Highest():
        Latest_Cust_ID = row[0]

    print("Current Accounts id from", first_Cust, " To ", Latest_Cust_ID)

    while option.lower() != "x":
        print(''' \n\n
            *************************************************
            *  1.   Create Database Table                   *		
            *  2.   Add initial DataSet                     *
            *  3.   Insert new Account                      *
            *  4.   Delete Account                          *
            *  5.   Update Account                          *
            *  6.   Show All Account                        *
            *  7.   Find Account by id                      *
            *  8.   Find Account by Customer name           *
            *  x.   Exit                                    *
            *************************************************
            ''')
        option = input("Select your option: ")
        if (option.isdigit()):
            userOption = int(option)

            if (userOption == 1):
                print("Your option is: ", option)
                theBank.createTable_Customers()

            elif (userOption == 2):
                print("Your option is: ", option)
                theBank.insert_initailDataSet()

            elif (userOption == 3):
                print("Your option is: ", option)
                theBank.createNewAccount(1, "Grace", 1334002, 25162012)

            elif (userOption == 4):
                print("Your option is: ", option)
                delAccId = input("Please enter Customer ID: ")
                theBank.DeleteAccount_Record(delAccId)

            elif (userOption == 5):
                print("Your option is: ", option)
                updAccId = input("Please enter Customer ID: ")
                updAccName = input("Please enter Customer Name: ")
                theBank.UpdateAccount_Detail(updAccId,  updAccName)

            elif (userOption == 6):
                print("Your option is: ", option)
                allCustomers = theBank.fetchAllAccount()

                print("\n-------------------------")
                print("Acct_number\tOwner")
                print("-------------------------")
                for row in allCustomers:
                    print(str(row[0]), "\t\t", row[1])

            elif (userOption == 7):
                print("Your option is: ", option)
                findAccId = input("Please enter Customer ID: ")
                CustomerFound = theBank.fetchAccount_By_Id(findAccId)
                print("\n-------------------------")
                print("Acct_number\tOwner")
                print("-------------------------")
                for row in CustomerFound:
                    print(str(row[0]), "\t\t", row[1])

            elif (userOption == 8):
                print("Your option is: ", option)
                findAccName = input("Please enter Customer Name: ")
                CustomerFound = theBank.fetchAccount_By_Name(findAccName)
                print("\n-------------------------")
                print("Acct_number\tOwner")
                print("-------------------------")
                for row in CustomerFound:
                    print(str(row[0]), "\t\t", row[1])

            else:
                print("Please Enter A Valid Menu Option")
        elif (option.lower() == "x"):
            print("Goodbye")
        else:
            print("Please Enter A Valid Menu Option")


startApp()
