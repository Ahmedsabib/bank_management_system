from datetime import datetime

class Manager:
    def __init__(self, name, nid):
       self.name = name
       self.nid = nid
       self.email = None
       self.password = None


    def create_account(self, bank):
       print("Hello.. ", self.name)
       email = input("enter your email: ")
       password = input("enter your password: ")
       done = bank.manager_register(self, email, password)
       if done == 0:
           return
       elif done == 1:
           self.login(bank)
       elif done == 2:
          print("You have successfully created an account, so please login")
          self.login(bank)




    def login(self, bank):
       print("Hello.. ",self.name)
       email = input("enter your email: ")
       password = input("enter your password: ")
       done = bank.manager_login(email,password)

       if done == 0:
           return
       elif done == 1:
           self.create_account(bank)
       elif done == 2:


        print("press 1 to chack ballance")
        print("press 2 to stop loan service")
        print("press 3 to on loan service")
        print("press 4 to see history")
        print("press 5 to see total loan")
        print("to exit press other")
        choice = int(input("enter your choice: "))

        if choice == 1:
            self.check_balance(bank)
        elif choice == 2:
            self.stop_loan_feature(bank)
        elif choice == 3:
            self.activate_loan_feature(bank)
        elif choice == 4:
            self.check_tarnsaction_history(bank)
        elif choice == 5:
            self.see_loan(bank)
        else:
           print("Thank you")
           return



    def check_balance(self, bank):
       print(bank.balance)

    def stop_loan_feature(self, bank):
        bank.available_loan = False

    def activate_loan_service(self, bank):
        bank.available_loan = True

    def check_tarnsaction_history(self, bank):
      bank.see_history()

    def see_loan(self, bank):
       print(bank.loan_amount())


    def __repr__(self) -> str:
       return f'Post : Manager\nName : {self.name}\nEmail : {self.email}'


class Transaction:
    def __init__(self, user, amount):
       self.name = user.name
       self.amount = amount
       self.time = datetime.today()
       self.userId = user.user_code
       self.cur_balance = user.balance



class Loan_Transaction(Transaction):
    def __init__(self, user, amount):
        super().__init__(user, amount)

    def __repr__(self) -> str:
        return f'-------- LOAN ---------\nUser Name : {self.name}\nUser id : {self.userId}\nLoan amount : {self.amount}\nCurrent Balance > {self.cu_balance}\nTime : {self.time}'


class Deposit_Transaction(Transaction):
    def __init__(self, user, amount):
        super().__init__(user, amount)

    def __repr__(self) -> str:
        return f'-------- DIPOSIT ---------\nUser Name : {self.name}\nUser id : {self.userId}\nDeposit Amount : {self.amount}\nCurrent Balance : {self.crrent_ballance}\nTime : {self.time}'

class Withdrawal_Transaction(Transaction):
    def __init__(self, user, amount):
        super().__init__(user, amount)

    def __repr__(self) -> str:
        return f'-------- WITHDRAWAL ---------\nUser Name : {self.name}\nUser Id :  {self.userId}\nWithdraw Amount : {self.amount}\nCurrent Balance : {self.cur_balance}\nTime : {self.time}'


class Send_Money(Transaction):
    def __init__(self, user, amount, receiver):
        super().__init__(user, amount)
        self.receiver_id = receiver.user_code
        self.receiver_name = receiver.name


    def __repr__(self) -> str:
        return f'-------- SEND MONEY ---------\nReceiver Name : {self.receiver_name}\nReceiver CODE : {self.receiver_id}\nSend Amount : {self.amount}\nCurrent Balance : {self.cur_balance}\nTime : {self.time}'



class Receive_Money(Transaction):
    def __init__(self, user, amount, receiver):
        super().__init__(user, amount)
        self.receive_balance = receiver.balance

    def __repr__(self) -> str:
        return f'-------- RECEIVE MONEY ---------\nSender Name :  {self.name}\nSender Code : {self.userId}\nSend Amount : {self.amount}\nCurrent Balance : {self.receive_balance}\nTime : {self.time}'


class Money_transfer(Transaction):
    def __init__(self, user, amount, receiver):
        super().__init__(user, amount)
        self._name = receiver.name
        self._id = receiver.user_code
        self._balance = receiver.balance

    def __repr__(self) -> str:
        return f"""
-------- MONEY TRANSFER ---------
    ------ SENDER -----
Sender Name :  {self.name}
Sender Code : {self.userId}
Transfered Amount : {self.amount}
Sender Current Balance : {self.cur_balance}

    ------- RECEIVER -------
RECEIVER NAME :  {self._name}
RECEIVER CODE : {self._id}
SEND AMOUNT : {self.amount}
Current Balance : { self._balance}
Time : {self.time}
        """

class User:
    def __init__(self, name, nid) -> None:
        self.name = name
        self.nid = nid
        self.user_code = None
        self.email = None
        self.password = None
        self.balance = 0
        self.Loan = 0
        self.history = []



    def create_user_account(self, bank):
        print("Hello.. ", self.name)
        if self.user_code != None:
            print("You are already a user!!")
            done = int(input("press 1 to login your account "
                             "to exit press any rather than 1: "))
            if done == 1:
                self.login(bank)
            else :
                print("Thank you")
        else:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            done = bank.register_system(self, email, password)
            if done == 0:
                return
            print("You have successfully registered to bank!!")
            print("Now please login again to continue the next activities")
            self.login(bank)


    def login(self, bank):
        print("Hello ", self.name)
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        done = 0
        done = bank.login(email,password)
        if done == 0:
            print("Invalid email or password try again or create a new account")
            return None
        print("You have successfully login to bank!!")
        print("press 1 to check balance: ")
        print("press 2 to withdraw: ")
        print("press 3 to deposit: ")
        print("press 4 to send money: ")
        print("press 5 to loan: ")
        print("press 6 history: ")
        print("press exit press other: ")


        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.chack_balance()
        elif choice == 2:
            amount = int(input("Enter the amount you want to withdraw: "))
            self.withdraw(bank, amount)

        elif choice == 3:
           amount = int(input("Enter the amount you want to depost: "))
           self.deposit(bank, amount)
        elif choice == 4:
          userid = int(input("Enter the use id: "))
          amount = int(input("Enter the amount you want to send: "))
          self.transfer_money(bank, userid, amount)
        elif choice == 5:
            amount = int(input("Enter the amount you want to loan: "))
            self.loan(bank, amount)

        elif choice == 6:
           self.check_history()
        else:
            return f''



    def check_balance(self):
        print("Your current balance is ", self.balance)

    def deposit(self, bank, amount):
        bank.deposit_request(self, amount)


    def withdraw(self, bank, amount):
        bank.withdraw_request(self, amount)

    def loan(self, bank, amount):
       bank.loan_request(self, amount)

    def check_history(self):
        for i in self.history:
            print("----------")
            print(i)

    def transfer_money(self, bank, receiver_id, amount):
        bank.send_money_request(self, receiver_id, amount)




    def __repr__(self) -> str:
       return f'Name : {self.name}\nNid : {self.nid}\nEmail : {self.email}\nIdcode : {self.user_code}\nBalance : {self.balance}\nLoan = {self.Loan}\n'


class Bank:
   def __init__(self, name, initial_account_balance):
      self.name = name
      self .__balance = initial_account_balance
      self.next_user_code = 101
      self.history =[]
      self.user_with_id = {}
      self.email_pass = {}
      self.loan_if_available = True
      self.total_subscriber = 0
      self.total_loan = 0
      self.manager = None
      self.manager_pass = None
      self.manager_email = None

   def manager_register(self, manager, email, password):
      if self.manager == manager:
         print("You are registered as manager so please login")
         return 1
      if self.manager != None:
         print("We have already a manager so we do not need another one")
         return 0
      self.manager = manager
      self.manager_email = email
      self.manager_pass = password
      manager.email = email
      manager.password = password
      return 2


   def manager_login(self, email, password):
      if self.manager == None:
         print("You are not register again and we also need a manager so please register first")
         return 1
      if email != self.manager_email or password != self.manager_pass:
         print("Invalid password or email!")
         print(email, self.manager_email)
         print(password, self.manager)
         return 0
      if email == self.manager_email and password == self.manager_pass:
         print("Successfully logged in")
         return 2



   def see_history(self):
      print("---------OVER ALL TRANSACTION HISTORY OF THE BANK ----------")
      for i in self.history:
         print(i)

   @property
   def balance(self):
      return self.__balance

   def loan_amount(self):
       return self.total_loan


   def register_system(self, user, email, passwoed):
      if email in self.email_pass:
         print("There is already a user id with this email so you can not create a new id")
         return 0
      user.user_code = self.next_user_code
      self.next_user_code += 1
      self.email_pass[email] = passwoed
      self.user_with_id[user.user_code] = user
      self.total_subscriber += 1
      user.email = email
      user.password = passwoed
      return 1

   def login(self, email, passwoed):
      if email not in self.email_pass:
         return 0
      if self.email_pass[email] != passwoed:
         return 0
      return 1

   def deposit_request(self, user, amount):
      if amount > 0:
         self.__balance += amount
         user.ballance += amount
         new_tansaction = Deposit_Transaction(user, amount)
         user.history.append(new_tansaction)
         self.history.append(new_tansaction)
         print("See the new transaction")
         print(new_tansaction)

   def withdraw_request(self, user, amount):
      if user.balance < amount:
         print("You do not have sufficient balacne")
         return
      else :
         user.ballance -= amount
         self.__balance -= amount
         new_tansaction = Withdrawal_Transaction(user, amount)
         user.history.append(new_tansaction)
         self.history.append(new_tansaction)
         print("See the new tansaction")
         print(new_tansaction)

   def loan_request(self, user, amount):
      if self.loan_if_available  or amount < self.__balance:
        if amount > user.balance * 2:
           print("You are not eligible to get a loan of this amount ")
           return
        else:
           user.balance += amount
           self.__balance -= amount
           new_tansaction = Loan_Transaction(user, amount)
           user.history.append(new_tansaction)
           self.history.append(new_tansaction)
           user.Loan += amount
           print("See the new tansaction")
           print(new_tansaction)
           self.total_loan += amount

      else:
         print("Sorry this service is not available due to our internet problem!")

   def send_money_request(self, sender, receiver_id, amount):
      if sender.balance < amount:
         print("You do not have enough money")
         return
      if receiver_id not in self.user_with_id:
         print("Could not find any user with the given id")
         return
      sender.balance -= amount
      self.user_with_id[receiver_id].ballance += amount
      new_transaction = Send_Money(sender, amount, self.user_with_id[receiver_id])
      sender.history.append(new_transaction)
      trans_money =  Money_transfer(sender,amount, self.user_with_id[receiver_id])
      self.history.append(trans_money)
      print("See the new transaction")
      print(new_transaction)
      new_tansaction1 = Receive_Money(sender,amount, self.user_with_id[receiver_id])
      self.user_with_id[receiver_id].history.append(new_tansaction1)
      print(new_tansaction1)

def main():
    bank1 = Bank("Bangladesh Bank", 1000000000)
    manager1 = Manager("Sabib", "123456")
    manager1.create_account(bank1)
    person1 = User("Aspia",12234)
    person1.create_user_account(bank1)
    person2 = User("Priangshu", 12244)
    person2.create_user_account(bank1)
    print("The person2 information is ")
    print(person2)
    person1.login(bank1)
    manager1.login(bank1)

if __name__ == "__main__":
    main()
