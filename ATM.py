class Atm:
    def __init__(self):
        self.pin=''
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
        self.pin=(input("Put Your Pin"))
        print("Pin Set Successfully") 
    def check_balance(self):
        temp=int(input("Enter Pin"))
        if temp==self.pin:
            print(f"Balance is {self.balance}")   
        else:
            print("Wrong Pin")
    def withdraw(self):
        temp=int(input("Enter Your pin"))
        if temp==self.pin:
            amount=int(input("Enter Amount"))
            if self.balance>amount:
                print("Sucess")
            else:
                print("influcient balance")
        else:
            print("Wrong pin")
    def deposit(self):
        temp=int(input("Enter Your pin"))
        if temp==self.pin:
            amo=int(input("Enter The Value"))
            self.balance+=amo
        else:
            print("Wrong Pin")
        
            
sbi=Atm()
