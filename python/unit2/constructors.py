class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)


emp1=Employee('vashi',101)
emp2=Employee('utsav',102)
emp1.display()
emp2.display() 

