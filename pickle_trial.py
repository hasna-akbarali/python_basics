import pickle

class Emp:
    def __init__(self,eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal
    
    def display(self):
        print(f'EID:{self.eid} NAME:{self.name} SAL:{self.sal}')



n = int(input('Enter the no. of Employees '))
f = open('employee_details','w+b')

for i in range(n):
    eid = input(f'Enter EID of {i+1} ')
    name = input(f'Enter NAME of {i+1} ')
    sal = input(f'Enter SAL of {i+1} ')
    e = Emp(eid,name,sal)
    pickle.dump(e,f)
