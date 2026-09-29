#maltilvl inharitance

class Grandfather:
    def grandfather_method(self):
        print('this is grandfather')


class Father(Grandfather):
    def father_method(self):
        print('this is father')


class Child(Father):
    def child_method(self):
        print('this is child')


fam = Child() 
fam.child_method()        
fam.father_method()       
fam.grandfather_method()  

#multiple inharitance

class Father:
    def father_method(self):
        print('this is father')


class Mother:
    def mother_method(self):
        print('this is mother')


class Child(Father, Mother):
    def child_method(self):
        print('this is child')

# Demonstration
fam = Child()

fam.child_method()   
fam.father_method()  
fam.mother_method()  