import json

class Authorisation():
    def sign_in(self):
        print("Welcome to the Vol-org app\n Firstly, sign in:")
        username = input("Enter your usernname:")
        password = input("Enter your password:")
        data = {}
        data[username] = password

        with open('data.json', 'w') as file1:
            json.dump(data, file1)
            file1.close()
            
    def auth(self):       
        with open('data.json', 'r') as file1:
            data = json.load(file1)
            file1.close()
            
        us1 = input("Enter your username: ")
        pswrd1 = input("Enter your password: ")
    
        if data[us1] != pswrd1:
            print("Incorrect password")
            self.auth()
        else:
            print("You are enterred succesfully")