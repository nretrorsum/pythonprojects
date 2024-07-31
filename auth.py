import json
import sys
        
class Authorisation():
    
    file1 = ''
    
    def __init__(self, hs_table):
        self.file1 = hs_table
    
    def start_message(self):
        print("""
              Welcome to the Vol-org app
              Choose your action:
              [1] Sign up
              [2] Sign in
              
              [0] Exit
              """)
        ch_1 = input()
        if ch_1 == '1':
            Authorisation.sign_in(self)
        if ch_1 == '2':
            Authorisation.sign_up(self)
        if ch_1 == '0':
            sys.exit()
        elif ch_1 != '1' and ch_1 != '2' and ch_1 != '0':
            print("Enter correct number!")
            Authorisation.start_message(self)
        
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
            
    def sign_up(self):
        pass