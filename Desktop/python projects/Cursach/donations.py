class donations():
    
    def choose_Donate(self):
        print("Choose organization to which you want to donate:\n 1.Wings of the Phoenix\n 2.Support the Ukrainian Army\n 3.Come Back Alive\n Enter your choise(1-3):\n")
        ch4 = input()
        self.donate(ch4)
        if ch4 == '0':
            from startMenu import start_Menu
            menu = start_Menu()
            menu.menu()
        
    def donate(self,ch4):
        if ch4 == '1':
            print("Number for donate: #1488\n To exit enter 0")
            
            ex2 = input()
            if ex2 =='0':
                self.choose_Donate()
            
        
        if ch4 == '2':
            print("Number for donate: #0609\n To exit enter 0")
            ex2 = input()
            if ex2 =='0':
                self.choose_Donate()
            
            
        if ch4 == '3':
            print("Number for donate: #1616\n To exit enter 0")
            ex2 = input()
            if ex2 =='0':
                self.choose_Donate()
