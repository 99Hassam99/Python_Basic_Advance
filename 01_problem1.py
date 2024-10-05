# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class programmer:
    company="Microsoft"

    def __init__(self,name,language,salary,pincode):
        self.name=name
        self.language=language
        self.salary=salary
        self.pincode=pincode

hassam =programmer("hassam","python",230000 ,9123)
print(hassam.name,hassam.language,hassam.pincode,hassam.salary,hassam.company)

ahmad =programmer("ahmad","javascript",200000,9233)
print(ahmad.name,ahmad.language,ahmad.pincode,ahmad.salary,ahmad.company)