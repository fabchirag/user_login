class User:
    def __init__(self):
        self.first_last = {}
        self.login_attempt = 0

    def register_user(self):
        print("Welcome, please register")
        r_first_name = input("Enter your First Name: ")
        r_last_name = input("Enter your Last Name: ")
        self.first_last[r_first_name] = r_last_name
        print("Registration Successful..\n")


    def login(self):
        print("Please Login with your details..")
        user_name = input("Enter your name: ")
        user_lastname = input("Enter your last name: ")
        if user_name in self.first_last.keys() and user_lastname in self.first_last.values():
            print("Login Successful..")
        else:
            print("Login details are incorrect, Please Register before Login")

    def increment_login(self, attempts):
        print("Remember only 3 attempts are allowed!")
        attempts += self.login_attempt
        if attempts > 3:
            print("Account is blocked")
        else:
            print("Increment Successful")


    def logout(self):
        print("\n")
        for key, value in self.first_last.items():
            print(f"{key}, {value} you are successfully Logged out".title())



user1 = User()
user1.register_user()
user1.login()
user1.increment_login(5)