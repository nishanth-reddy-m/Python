class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def print(self):
        prefix = 8
        print(('|'.rjust(prefix))*self.get_level(),end = '')
        print('--'+self.data.rjust(prefix,'-'))
        if self.children:
            for i in self.children:
                i.print()

class management(TreeNode):
    def __init__(self, data, designation):
        super().__init__(data)
        self.designation = designation
    def print(self,mode='both'):
        if mode == 'name':
            prefix = 8
            print(('|'.rjust(prefix))*self.get_level(),end = '')
            print('--'+self.data.rjust(prefix,'-'))
            if self.children:
                for i in self.children:
                    i.print(mode)
        elif mode == 'designation':
            prefix = 8
            print(('|'.rjust(prefix))*self.get_level(),end = '')
            print('--'+self.designation.rjust(prefix,'-'))
            if self.children:
                for i in self.children:
                    i.print(mode)
        elif mode == 'both':
            prefix = 8
            print(('|'.rjust(prefix))*self.get_level(),end = '')
            print('--'+f'{self.data} ({self.designation})'.rjust(prefix,'-'))
            if self.children:
                for i in self.children:
                    i.print(mode)
        else:
            raise Exception('Invalid Input')

class world(TreeNode):
    def print_tree(self,level):
        if self.get_level() > level:
            return
        prefix = 8
        print(('|'.rjust(prefix))*self.get_level(),end = '')
        print('--'+self.data.rjust(prefix,'-'))
        if self.children:
            for i in self.children:
                i.print_tree(level)
        
def products():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptops')
    laptop.add_child(TreeNode('Macbook'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    tv = TreeNode('TVs')
    tv.add_child(TreeNode('Sony'))
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))

    phone = TreeNode('Phones')
    phone.add_child(TreeNode('Iphone'))
    phone.add_child(TreeNode('Pixel'))
    phone.add_child(TreeNode('Galaxy'))

    root.add_child(phone)
    root.add_child(laptop)
    root.add_child(tv)

    return root

def managers():
    ceo = management('Nilupul','CEO')

    ih = management('Vishwa','Infrastructure Head')
    ih.add_child(management('Dhaval','Cloud Manager'))
    ih.add_child(management("Abhijit",'App Manager'))

    cto = management('Chinmay','CTO')
    cto.add_child(ih)
    cto.add_child(management('Aamir','Application Head'))

    hr = management('Gels','HR Head')
    hr.add_child(management('Peter','Recruitment Manager'))
    hr.add_child(management('Waqas','Policy Manager'))

    ceo.add_child(cto)
    ceo.add_child(hr)

    return ceo

def globe():
    Global = world('Global')
    India = world('India')
    Gujarat = world('Gujarat')
    Ahmedabad = world('Ahmedabad')
    Baroda = world('Baroda')
    Karnataka = world('Karnataka')
    Bangaluru = world('Bangaluru')
    Mysore = world('Mysore')
    Usa = world('USA')
    Nj = world('New Jersey')
    Princeton = world('Princeton')
    Trenton = world('Trenton')
    California = world('California')
    Sf = world('San Francisco')
    Mv = world('Mountain View')
    Pa = world('Palo Alto')

    Gujarat.add_child(Ahmedabad)
    Gujarat.add_child(Baroda)

    Karnataka.add_child(Bangaluru)
    Karnataka.add_child(Mysore)

    Nj.add_child(Princeton)
    Nj.add_child(Trenton)

    California.add_child(Sf)
    California.add_child(Mv)
    California.add_child(Pa)

    India.add_child(Gujarat)
    India.add_child(Karnataka)

    Usa.add_child(Nj)
    Usa.add_child(California)

    Global.add_child(India)
    Global.add_child(Usa)

    return Global

if __name__ == "__main__":
    root = products()
    root.print()
    print()
    ceo = managers()
    ceo.print('name')
    print()
    ceo.print('designation')
    print()
    ceo.print()
    print()
    Global = globe()
    Global.print_tree(1)
    print()
    Global.print_tree(2)
    print()
    Global.print_tree(3)