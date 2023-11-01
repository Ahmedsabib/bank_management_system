class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.loan = 0
        # self.total_cash = self.cash
        self.TranferCash = False
        self.admin_details_list = []
        self.loggedin_admin = False
        self.loan_feature = True
        self.transaction_history = []

    def register_user(self, name , ph , password):
        cash = self.cash
        conditions = True
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 11 digit number")
            conditions = False

        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
            conditions = False

        if conditions == True:
            print("Account created successfully")
            self.client_details_list = [name , ph , password , cash]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")


    def register_admin(self, name, ph, password):
        cash = self.cash
        conditions = True
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 11 digit number")
            conditions = False

        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
            conditions = False

        if conditions == True:
            print("Account created successfully")
            self.admin_details_list = [name , ph , password , cash]
            with open(f"{name}.txt","w") as f:
                for details in self.admin_details_list:
                    f.write(str(details)+"\n")



    def take_loan(self, amount):
        if amount <= self.cash and self.loan_feature:
            self.loan += amount


    def login_user(self, name , ph , password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name

            else:
                print("Wrong details")

    def login_admin(self, name , ph , password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.admin_details_list = details.split("\n")
            if str(ph) in str(self.admin_details_list):
                if str(password) in str(self.admin_details_list):
                    self.loggedin_admin = True

            if self.loggedin_admin == True:
                print(f"{name} logged in")
                # self.cash = self.total_cash
                self.name = name

            else:
                print("Wrong details")

    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            # self.total_cash += amount
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")


    def withdraw_cash(self, amount):
        if amount > 0:
            if self.cash >= amount:
                self.cash -= amount
                # self.total_cash -= amount
                self.transaction_history.append(f'You have transactioned {amount} from your account')
                with open(f"{name}.txt","r") as f:
                    details = f.read()
                    self.client_details_list = details.split("\n")

                with open(f"{name}.txt","w") as f:
                    f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))

                print("Amount added successfully")

        else:
            print("Enter correct value of amount")

    def Tranfer_cash(self, amount , name ,ph):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TranferCash = True

            if self.TranferCash == True:
                for x in self.client_details_list:
                    if x[0] == name:
                        x[3] += amount
                        break

                self.cash -= amount


        if self.TranferCash == True:
            # total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

            with open(f"{self.name}.txt","r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))

            print("Amount Transfered Successfully to",name,"-",ph)
            print("Balance left =",left_cash)
            self.cash = left_cash

    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))
            print("new Password set up successfully")

    def ph_change(self , ph):
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph)))
            print("new Phone number set up successfully")



if __name__ == "__main__":
    total_cash = 0
    Bank_object = Bank()
    print("------------------ Welcome to my Bank -------------------------")
    print("1.Login")
    print("2.Create a new Account")
    print("3.Admin Login")
    print("4.Create new Admin Account")
    user = int(input("Make decision: "))

    print('-----------------------------------------------------------------\n\n')

    if user == 1:
        print("Logging in")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.login_user(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1.Deposit amount")
                print("2.Check Balance")
                print("3.Transfer amount")
                print("4.Edit profile")
                print("5.Withdraw Amount")
                print("6.Check Transaction History")
                print("7.Take Loan")
                print("8.Logout")
                login_user_key = int(input())
                if login_user_key == 1:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)
                    total_cash += amount
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user_key == 2:
                    print("Balacne =",Bank_object.cash)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user_key == 3:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    if amount >= 0 and amount <= Bank_object.cash:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Tranfer_cash(amount,name,ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0 :
                        print("Enter please correct value of amount")

                    elif amount > Bank_object.cash:
                        print("Not enough balance")

                elif login_user_key == 4:
                    print("1.Password change")
                    print("2.Phone Number change")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("Enter new Password: ")
                        Bank_object.password_change(new_passwrod)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new Phone Number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break


                elif login_user_key == 5:
                    amount = int(input("Enter amount: "))
                    Bank_object.withdraw_cash(amount)
                    if total_cash < amount:
                        print('This bank is bankrupt')
                    else:
                        total_cash -= amount
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user_key == 6:
                    for doc in Bank_object.transaction_history:
                        print(doc)


                elif login_user_key == 7:
                    amount = int(input("Enter amount: "))
                    Bank_object.take_loan(amount)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break


                elif login_user_key == 8:
                    break


    if user == 2:
        print("Creating a new  Account")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.register_user(name, ph, password)



    if user == 3:
        print("Logging in")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.login_admin(name, ph, password)
        while True:
            if Bank_object.loggedin_admin:
                print("1.Total Available Balance")
                print("2.Check Total Loan")
                print("3.Loan Feature")
                print("4.Logout")
                login_admin_key = int(input())
                if login_admin_key == 1:
                    print("Balance =",total_cash)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_admin_key == 2:
                    print("Total Loan =",Bank_object.loan)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_admin_key == 3:
                    if Bank_object.loan_feature == False:
                        print("Do you want to turn on loan feature?")
                        print("1.YES")
                        print("2.NO")
                        choose = int(input())
                        if choose == 1:
                            Bank_object.loan_feature = True

                    else:
                        print("Do you want to turn off loan feature?")
                        print("1.YES")
                        print("2.NO")
                        choose = int(input())
                        if choose == 1:
                            Bank_object.loan_feature = False

                elif login_admin_key == 4:
                    break


    if user == 4:
        print("Creating a new  Account")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.register_admin(name, ph, password)

