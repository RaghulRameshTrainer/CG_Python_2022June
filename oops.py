class Employee():
    hike=1.05
    def __init__(self,fname,lname,pay):    #constructor
        self.fname=fname
        self.lname=lname
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@gmail.com'

    def appraisal(self):
        #self.hike=hike_percent
        self.salary=int(self.salary*self.hike)

    def fullname(self):
        return "{}.{}".format(self.fname,self.lname)

    @classmethod
    def create_object(cls,in_str):
        fn,ln,sal=in_str.split('-')
        return cls(fn,ln,int(sal))

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "it's holiday"
        return "it's working day"


str1='Raghul-Ramesh-50000'
str2='Levin-Lenus-60000'

emp_1=Employee.create_object(str1)
emp_2=Employee.create_object(str2)

class Developer():
    def __init__(self,fname,lname,pay,tech):
        self.tech=tech
        super().__init__(fname,lname,pay)

    #Method overriding
    def fullname(self,title):
        self.title=title
        return '{} {}.{}'.format(self.title,self.fname,self.lname)

    # def project_details(self):
    #     return "Scope International"

    def project_details(self,*city):
        if len(city) > 0:
            if city[0]=='Chennai':
                return "Scope International"
            else:
                return "Jp Margon"
        else:
            return "Scope International"

class Manager(Employee,Developer):
    def fullname(self,title):
        self.title=title
        return super(Employee,self).fullname(self.title)

mgr_1=Manager('Dinesh','Kumar',100000)
mgr_2=Manager('Ankit','Kumar',200000)

print(mgr_1.fullname('Mr'))
print(mgr_1.project_details())
#print(help(mgr_1))

# dev_1=Developer('Malini','Sekar',10000,'Python')
# dev_2=Developer('Ramya','Rajesh',20000,'Java')
# print(dev_1.project_details())
# print(dev_1.fullname('Miss'))
# print(dev_2.fullname('Mrs'))
# print("Dev_1 email: {} and tech:{} ".format(dev_1.email,dev_1.tech))
# print("Dev_2 email: {} and tech:{} ".format(dev_2.email,dev_2.tech))
# import datetime
# tday=datetime.date(2022,7,4)
# print(Employee.is_workingday(tday))
# print("EMP 1:", emp_1.fullname())
# print("EMP 2:", emp_2.fullname())

# print("EMP-1 : ",emp_1.email)
# print("EMP-2 : ",emp_2.email)

# emp_1.hike=1.1
# print("Raghul's current salary:",emp_1.salary)
# emp_1.appraisal()
# print("Raghul's revised salary:",emp_1.salary)
#
# print("Levin's current salary:",emp_2.salary)
# emp_2.appraisal()
# print("Levin's revised salary:",emp_2.salary)

'''OOPS Features:
    Abstration
    Inheritance
    Polymorphism
    Encapsulation'''