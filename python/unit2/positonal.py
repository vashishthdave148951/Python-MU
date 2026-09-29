def student (name,age):
    print ("name",name)
    print ("age",age)
print("Raj",21)

#keyword arguments
student(age=21,name='vashi')
#default argument
def greet (name='student'):
    print('hello', name)

greet()
greet('utsav')
