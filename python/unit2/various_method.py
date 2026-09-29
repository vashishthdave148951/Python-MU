class student:
    university = 'marwadi university'

    def __init__(self, name, enrol, marks):
        self.name = name
        self.enrol = enrol
        self.marks = marks

    def show(self):
        print('SNM:', self.name)
        print('EN:', self.enrol)
        print('MK:', self.marks)

    @classmethod
    def display(cls):
        print('university:', cls.university)

    @staticmethod
    def check_rs(marks):
        if marks >= 40:
            return 'pass'
        else:
            return 'fail'

stud = student('Raj', 5006, 90)

print('--- Instance Method ---')
stud.show()

print('\n--- Class Method ---')
stud.display()

print('\n--- Static Method ---')
result = stud.check_rs(stud.marks)
print('Result:', result)