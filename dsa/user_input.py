class user_input:
    def search_input(self):
        try:
            List,key = list(map(int,input("Enter the List: ").split())),int(input("Enter the key: "))
        except ValueError:
            print('Invalid Input! Please try again')
            return self.search_input()
        except KeyboardInterrupt:
            print('\nProgram ended')
            exit()
        return List,key
    def sort_input(self):
        try:
            List = list(map(int,input("Enter the List: ").split()))
        except ValueError:
            print('Invalid Input! Please try again')
            return self.sort_input()
        except KeyboardInterrupt:
            print('\nProgram ended')
            exit()
        return List
