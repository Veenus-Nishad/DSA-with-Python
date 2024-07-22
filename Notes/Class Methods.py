#three types of class methods
# 1.Instance method
# 2.Static Method
# 3.Class Method

class Test():
  x=5
    # to make instance object method pehla argument must be self
  def f1(self):
    pass

  #to make static Method use decorator @staticmethod
  @staticmethod
  def f2():
    print("Hello")

  #to make class Method first aleast one argument usually cls and decorator @classmethod
  @classmethod
  def f3(cls):
    print(cls.x)

  #use of classmethod : implicit argument passed 
  Test.f3()   # output 5

  #use of static method : no impicit argument passed 
  Test.f2() 


  ## Q.Create a class Employee with attributes empid,name,salary and also define method to access properties of Employee
class Employee:
  def __init__(self,empId=None,name=None,salary=None):
    self.empId=empId
    self.name=name
    self.salary=salary

  # to further update the fields
  def setEmpId(self,empId):
    self.empId=empId

  def setName(self,name):
    self.name=name

  def setSalary(self,salary):
    self.salary=salary

  # to fetch the fields

  def getEmpId(self):
    return self.empId
  
  def getName(self):
    return self.name
  
  def getSalary(self):
    return self.salary
  
e1=Employee()
e2=Employee(1,"Rahul",400000)
e1.setEmpId(2)
e1.setName("Rajesh")
e1.setSalary(500000)
print(e1.getEmpId(),e1.getName(),e1.getSalary())