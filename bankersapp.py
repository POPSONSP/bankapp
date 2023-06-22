import time
import sys
import mysql.connector as connection
myconn = connection.connect(host="127.0.0.1", user="root", passwd="Popson_2013", database="bank")
cursor = myconn.cursor()

time.sleep(1)
def homepage():
    print("Welcome to Online Banking Services")
    time.sleep(2)
    print("""Select the banking service to use !!!
    Enter 1 for GTB
    Enter 2 for Polaris Bank
    Enter 3 to deposit
    Enter 4 to Logout
    """)
    dec = input(">>> ")
    if dec == "1":
        from GTBbankapp import welcome
        welcome()
    elif dec == "2":
            from Polarisbankapp import welcome
            welcome()
    elif dec == "3":
         deposit()   
    elif dec == "4":
         sys.exit()         
    else:
        homepage()   

def deposit():
    print("""
     Enter 1 to deposit to GTB
     Enter 2 to deposit to Polaris
     """)        
    let=input(">>> ") 
    if let == "1":
        time.sleep(2)
        print("Kindly provide beneficiary detals")
        time.sleep(1)
        deposit_gtb()
    elif let == "2":
         time.sleep(2)
         print("kindly Provide beneficiary details")
         time.sleep(1)
         deposit_polaris()   

def deposit_gtb():
        request=int(input("Kindly provide the account number of the beneficiary: "))
        time.sleep(2)
        val= (request, )
        query = "select * from gtb where acc_nu = %s"
        cursor.execute(query, val)
        resultWE = cursor.fetchone()
        if resultWE:
            print(f" you are sending money to {resultWE[1]} {resultWE[2]} {resultWE[3]}")
            time.sleep(2)
            request1 = int(input("Amount to deposit: "))
            new_balance = resultWE[10] + request1
            val2 = (new_balance, request)
            querry= "UPDATE gtb SET Balance = %s where acc_nu = %s"
            cursor.execute( querry, val2)
            myconn.commit()
            time.sleep(2)
            print("Processing Transaction...")
            time.sleep(3)
            print(f"You have successfully deposited {request1} naira to {resultWE[1]} {resultWE[3]}")
        else:
            print("Invalid username or password")
            deposit()     

def deposit_polaris():
    request=int(input("Kindly provide the account number of the beneficiary: "))
    time.sleep(2)
    val= (request,)
    query = "select * from polaris where acc_nu =%s"
    cursor.execute(query, val)
    results = cursor.fetchone()
    if results:
        print(f" you are sending money to {results[1]} {results[2]} {results[3]}")
        time.sleep(2)
        request1=int(input("Amount to deposit: "))
        new_balance= (results[10] + request1)
        val = (new_balance, request)
        querry= "UPDATE polaris SET Balance =%s where acc_nu =%s"
        cursor.execute( querry, val)
        myconn.commit()
        time.sleep(2)
        print("Processing Transaction... ")
        time.sleep(3)
        print(f"You have successfully deposited {request1} naira to {results[1]} {results[3]}" ) 
    else:
        print("Invalid username or password")
        deposit()    
homepage()




    

