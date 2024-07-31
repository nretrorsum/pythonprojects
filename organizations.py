


class organizations:
    
    def ShowOrganizations(self):
        print("Current list of organizations:\n 1.Wings of the Phoenix\n 2.Support the Ukrainian Army\n 3.Come Back Alive\n Enter your choise(1-3):\n")
        choise1 = input()
        
        if choise1 == '9':
            from startMenu import start_Menu
            menu = start_Menu()
            menu.menu()
            
        if choise1 == "1":
            with open("wof.txt", "r") as file1:
                line1 = file1.read()
            print(line1)
            ex = input()
            if ex == '0':
                self.ShowOrganizations()
                
        if choise1 == "2":
            with open("sua.txt", "r") as file2:
                line2 = file2.read()
            print(line2, "If you want return enter 0")
            ex = input()
            if ex == '0':
                self.ShowOrganizations()
                
        if choise1 == "3":
            with open("cba.txt", "r") as file3:
                line3 = file3.read()
            print(line3)
            ex = input()
            if ex == '0':
                self.ShowOrganizations()
                
        while choise1 != '1' != '2' != '3' !='9' !='0':
            print("Enter correct number!")       
            self.ShowOrganizations()