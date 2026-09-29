class Student:
    def show(self, name, enroll, dept):
        self.name = name
        self.enroll = enroll
        self.dept = dept

    def cal_total(self, mark1, mark2, mark3):
        total = mark1 + mark2 + mark3
        return total


obj = Student()
# Call show
obj.show('Raj', 92600565006, 'CS')
# Call cal_total directly using the object
result = obj.cal_total(85, 90, 88)
print("Total Marks:", result)