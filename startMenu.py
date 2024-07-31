import sys
from organizations import organizations
from donations import donations

class start_Menu():
    
    def __init__(self):
        self.organizations = organizations()
        self.donations = donations()
    
    def start(self):

        print("""Welcome to the Vol-org app\n 
                The idea of creation such a list arose because of need for ukrainians to know the differencies between national organizations, their specializations\n 
                and (what's the most important) -- honesty 
                If u want to get something useful to understand to whom u want to donate your money -- come to us!""")

    def menu(self):
            print("""
              Choose your action\n
              [1] if you looking for organizaion list;
              [2] if you looking for rating the organizations;\n
              [0] if you want to exit;""")
            
            ch3 = input("Enter your choise to continue:\n")
            if ch3 == '1':
                self.organizations.ShowOrganizations()
            if ch3 == '2':
                self.donations.choose_Donate()
            if ch3 == '0':
                sys.exit()
            elif ch3 != '1' !='2' !='0':
                print("Enter correct number!")
                self.menu()