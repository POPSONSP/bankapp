import time
import random
import sys
import mysql.connector as connection
myconn = connection.connect(host="127.0.0.1", user="root", passwd="Popson_2013", database="bank")
cursor = myconn.cursor()
def welcome():
    time.sleep(1)
    print("Redirecting to Polaris... ")
    time.sleep(2)
    print("You are welcome to Polaris bank \n Enter 1 to login or 2 to create new account")
    choice = input(">>> ")
    if choice =="1":
        login()
    elif choice == "2":
        registration()
    else:
        print("You have made a wrong choice")
        welcome()
def registration():
        print("Kindly proceed with your registration by providing your details below ")
        val= []
        bank_info= ("First_name", "Middle_name", "Last_name", "Gender", "Age","Email", "BVN", "NIN","acc_nu","Balance", "Pass_word" , "Pin")
        querry= "INSERT INTO polaris (First_name, Middle_name, Last_name, Gender, Age, Email, BVN, NIN,acc_nu, Balance, Pass_word , Pin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s,%s, %s)"
        for holder in range(12):
            if bank_info[holder] == "BVN":
                user = random.randint(5129370000, 5129399999)
            elif bank_info[holder]== "NIN":
                user= random.randint( 4321371000, 4321379876)
            elif bank_info[holder]=="Balance":
                 user = 0
            elif bank_info[holder]=="acc_nu":  
                user= random.randint(2145043000, 2145049999)     
            else:    
                user= input(f"Enter your {bank_info[holder]}: ")
            val.append(user)
            time.sleep(2)
        print("Thank you for registering with us ")
        cursor.execute(querry, val)
        myconn.commit()
        time.sleep(2)
        print(f"Dear {val[0]} {val[1]} {val[2]} your account number is {val[8]} \n Your username is {val[5]}, password is {val[10]} pin is {val[11]}")
        time.sleep(2)
        print("""
        Enter 1 to login or 2 logout
        """)
        step= input(">>> ")
        if step == "1":      
           login()
        else:
            sys.exi()
def login():
    global username
    global Pass_word
    username = input("Enter your Email address: ")
    Pass_word = input("Enter your password ")
    val = (username, Pass_word)
    querry = "select * from polaris where Email=%s and Pass_word=%s "
    cursor.execute(querry, val)
    global result
    result = cursor.fetchone()
    if result:
        print("You have successfully login")
        operation()
    else:
        print("Invalid username or password")
        login() 

def operation():
    print("""
    These are the operations you can perform:
    1. TRANFERS
    2. BUY AIRTIME AND DATA
    3. Logout
   
    """)
    task = input("What transaction will you like to perform: ")
    if task == "1":
        time.sleep(2)
        transfer()
    elif task == "2":
        time.sleep(2)
        airtime_data()  
    elif task == "3":
        sys.exit()       
    else:
        print("Invalid input")
        time.sleep(2)
        operation()   

def transfer():
    print("""
    Below is the operation you can perform
    1.Transfer to GTB
    2. Transfer to Polaris 
    3. Perform Another Transaction
    """)
    user= input("what type of transfer will you like to carry out: ")
    if user=="1":
        transfer_GTB()
    elif user=="2":
        transfer_polaris()
    elif user == "3":
        operation()
    else:
        print("you hae entered an invalid input ")
        time.sleep(2)
        transfer()    

def transfer_GTB():
    request=int(input("Kindly provide the account number of the beneficiary: "))
    val= (request,)
    query = "select * from gtb where acc_nu = %s"
    cursor.execute(query, val)
    resultWE = cursor.fetchone()
    if resultWE:
        time.sleep(2)
        print("Confiming beneficiary details: ")
        time.sleep(1)
        print(f"Beneficiary name: {resultWE[1]} {resultWE[3]}")
        time.sleep(2)
        request1 = int(input("Amount to deposit: "))
        print(f"you are sending the sum of {request1} to {resultWE[1]} {resultWE[3]}, kindly confirm the transaction ")
        time.sleep(1)
        print("Proceed by entering your 4 digit passcode")
        time.sleep(1)
        request3=int(input("Enter your four digit pin: "))
        pin = result[12]
        if request3 == pin:
            new_balance = resultWE[10] + request1
            val2 = (new_balance, request)
            querry= "UPDATE gtb SET Balance = %s where acc_nu = %s"
            cursor.execute( querry, val2)
            myconn.commit()
            print(f"You have successfully deposited {request1} naira to {resultWE[1]} {resultWE[3]}")
            sent_bal=result[10]-request1
            val=(sent_bal,username)
            querry2="UPDATE polaris SET Balance=%s where Email=%s"
            cursor.execute(querry2,val)
            myconn.commit()
            print(username)
            time.sleep(2)
            drop= input("would you like to perform another transaction: ")
            if drop =="yes":
                operation()
            else:
                sys.exit()
        else:
            print("you have entered a wrong pin")  
            transfer_GTB()

def transfer_polaris():
    request=int(input("Kindly provide the account number of the beneficiary: "))
    val= (request,)
    query = "select * from polaris where acc_nu = %s"
    cursor.execute(query, val)
    resultWE = cursor.fetchone()
    if resultWE:
        time.sleep(2)
        print("Confiming beneficiary details: ")
        time.sleep(1)
        print(f"Beneficiary name: {resultWE[1]} {resultWE[3]}")
        time.sleep(2)
        request1 = int(input("Amount to deposit: "))
        print(f"you are sending the sum of {request1} to {resultWE[1]} {resultWE[3]}, kindly confirm the transaction ")
        time.sleep(1)
        print("Proceed by entering your 4 digit passcode")
        time.sleep(1)
        request3=int(input("Enter your four digit pin: "))
        pin = result[12]
        if request3 == pin:
            new_balance = resultWE[10] + request1
            val2 = (new_balance, request)
            querry= "UPDATE polaris SET Balance = %s where acc_nu = %s"
            cursor.execute( querry, val2)
            myconn.commit()
            print(f"You have successfully deposited {request1} naira to {resultWE[1]} {resultWE[3]}")
            sent_bal=result[10]-request1
            val=(sent_bal,username)
            querry2="UPDATE polaris SET Balance=%s where Email=%s"
            cursor.execute(querry2,val)
            myconn.commit()
            print(result)
            print(username)
            time.sleep(2)
            drop= input("would you like to perform another transaction: ")
            if drop =="yes":
                operation()
            else:
                sys.exit()
        else:
            print("you have entered a wrong pin")  
            transfer_polaris()
    
def airtime_data():
    print("""These are the operations avalable to be performed here:
    1. Airtime purchase
    2. Data purchase
    """)
    choice=input("what action do you want to take: ")
    if choice== "1":
        airtime()
    elif choice== "2":
        data()    
    else:
        print("The operation you have entered is presently unavailable for use kindly use other services provided ")
        airtime_data()


def airtime():
    air_phone= input("Enter your phone number: ")
    air_amount=int(input("Enter amount: "))
    mtn=("0903", "0810", "0906")
    glo=("0905","0805", "0807")
    airtel=("0802", "0902","0808")
    if air_phone.startswith(mtn):
         print(f" you are about to purchase MTN airtime into {air_phone} the sum of {air_amount}")  
    elif air_phone.startswith(glo):
         print(f" you are about to purchase GLO airtime into {air_phone} the sum of {air_amount}")    
    elif air_phone.startswith(airtel):
         print(f" you are about to purchase Airtel airtime into {air_phone} the sum of {air_amount}")  
    else:
        print("You hae entered a wrong number")
        time.sleep(1)
        airtime()   
    time.sleep(1)  
    resp= input("Enter your four digit number: ")
    if resp==Pass_word:
        time.sleep(1)
        print("Transaction succesful")
        drop= input("would you like to perform another transaction: ")
        if drop =="yes":
            operation()
        else:
            sys.exit()    
    else:
        print("Transaction failed")    
        airtime()

def data():
    air_phone= input("Enter your phone number: ")
    air_amount=int(input("Enter amount: "))
    mtn=("0903", "0810", "0906")
    glo=("0905","0805", "0807")
    airtel=("0802", "0902","0808")
    if air_phone.startswith(mtn):
         print(f" you are about to purchase MTN data bundle into {air_phone} the sum of {air_amount}")  
    elif air_phone.startswith(glo):
         print(f" you are about to purchase GLO data bundle into {air_phone} the sum of {air_amount}")    
    elif air_phone.startswith(airtel):
         print(f" you are about to purchase Airtel data bundle into {air_phone} the sum of {air_amount}")  
    else:
        print("You hae entered a wrong number")
        time.sleep(1)
        data()   
    time.sleep(1)  
    resp= input("Enter your four digit number: ")
    if resp==Pass_word:
        time.sleep(1)
        print("Transaction succesful")
        time.sleep(2)
        drop= input("would you like to perform another transaction: ")
        time.sleep(1)
        if drop =="yes":
            operation()
        else:
            sys.exit()    
    else:
        print("Transaction failed")    
        data()
welcome()        
