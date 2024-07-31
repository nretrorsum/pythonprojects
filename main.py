from auth import Authorisation
from startMenu import start_Menu,organizations,donations


def main():
    auth = Authorisation('data.json')
    start_menu = start_Menu()
    auth.start_message()           
    auth.auth()        
    start_menu.start()
    start_menu.menu()
    organizations.ShowOrganizations()
    donations.choose_Donate()
    
if __name__ == "__main__":
    main()