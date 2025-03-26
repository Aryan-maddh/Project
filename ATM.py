class Atm:
    def __init__(self):
        self.pin=0
        self.balance=0
        self.menu()
    def menu(self):
        user_input=int(input("""
        1.Press 1 To set a Pin
        2.Press 2 To deposit
        3.Press 3 To withdraw 
        4.Press 4 To check balance
        5.Press 5 To Exit(0)"""))
        if user_input==1:
            self.new_pin()
        elif user_input==2:
            self.deposit()
        elif user_input==3:
            self.withdraw()
        elif user_input==4:
            self.check_balance()
        elif user_input==5:
            return 0
        else:

            print("Invalied choice")
    def new_pin(self):
        self.pin=int(input("Put Your Pin"))
        print("Pin Set Successfully")
        self.menu() 
    def check_balance(self):
        
        temp=int(input("Enter Pin"))
        if temp==self.pin:
            print(f"Balance is {self.balance}")   
        else:
            print("Wrong Pin")
        self.menu()
    def withdraw(self):
        temp=int(input("Enter Your pin"))
        if temp==self.pin:
            amount=int(input("Enter Amount"))
            if self.balance>=amount:
                print("Sucess")
                self.balance-=amount
                print(f"Account Balance is {self.balance}")
            else:
                print("influcient balance")
        else:
            print("Wrong pin")
        self.menu()
    def deposit(self):
        temp=int(input("Enter Your pin"))
        if temp==self.pin:
            amo=int(input("Enter The Value"))
            self.balance+=amo
            print('deposit successfull')
            print(f"Account Balance is {self.balance}")
        else:
            print("Wrong Pin")
        self.menu()
            
sbi=Atm()     #Calling
