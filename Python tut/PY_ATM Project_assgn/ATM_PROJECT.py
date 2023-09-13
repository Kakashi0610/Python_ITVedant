"""FINAL PROJECT"""

class Bank:
    balance=5000

    def login(self,pin):
        if pin==1111:
            return True
        else:
            return False

    def login1(self,name):
        if name == "Aniket" or name=="aniket":
            return True
        else:
            return False

    def credit(self,amt):
        self.balance+=amt

    def debit(self,amt):
        self.balance-=amt

    def display(self):
        print("Current balance is "+str(self.balance))
        
    def display1(self):
        print("After transaction current balance is "+str(self.balance))

obj = Bank()
flag=False
print("****** WELCOME TO ARIZONA STATE BANK ******")
print("""
           TRANSACTION LIST
        **********************
           Credit     c
           Debit      d 
           Balance    b
           Exit       e
        **********************
        """)
for i in range(1,4):
       if obj.login1(input("ENTER YOUR NAME : ")) and obj.login(int(input("ENTER YOUR PIN TO ACCESS THE ACCOUNT : \n"))):
           flag=True
           break
if flag:
    while True:
        o=input("""Press \'c' for credit \nPress \'d' for debit \nPress \'b' for balance \nPress \'e' for exit \nEnter the code here : """) 
        if o=='c' or o=='C':
            obj.credit(int(input("Enter amount for credit : ")))
            obj.display1()
      
        elif o=='d' or o=='D':
            amt=int(input("Enter amount for debit : "))
            if amt<=obj.balance:
                if amt>4500:
                    print ("Sorry! You cannot withdraw if post-transaction balance is less than 500")
                else :
                    obj.debit(amt)
                    obj.display1()
            else:
                print("Sorry ! You might have insufficient balance... please     try later !")

        elif o=='b' or o=='B':
            print("Total balance is : ")
            obj.display()
        elif o=='e' or o=='E':
            print("""
                printing receipt..............
          ******************************************
              Thanks for choosing us as your bank                  
          ******************************************
          """)
            break
else:
    print("Your pin code attempt has been completed. Reenter the correct name and correct Pin to Access your account.")