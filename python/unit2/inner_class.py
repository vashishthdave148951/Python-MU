class university:
    def __init__(self,university_name):
        self.university_name=university_name

    class Student:
        def __init__(self,name,Enroll,dept):
            self.name=name
            self.Enroll=Enroll
            self.dept=dept

        def show(self):
            print('S nm:',self.name)
            print('ER:',self.Enroll)
            print('DEPT:',self.dept)

uni=university('Marwadi University')
stud=uni.Student('Raj Patel', 92600565006,'CS')
stud.show()


