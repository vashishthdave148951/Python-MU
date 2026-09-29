class student:
    def __init__(self):
        print('this is non parametrized constructor')
    def show (self,name):
        print('hello',name)
obj=student()
obj.show('Raj')