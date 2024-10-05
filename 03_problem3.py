# Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

class employee:
    salary = 200
    increment = 40

    @property
    def salary_after_increment(self):
        return (self.salary+self.salary*(self.increment)/100)

    @salary_after_increment.setter
    def salary_after_increment(self,salary):
        self.increment= ((salary/self.salary)-1)*100

e = employee()
print(e.salary_after_increment)
e.salary_after_increment = 280
print(e.increment)