def singleton(cls):
        def innerFunc(*args, **keywordargs):
            if not innerFunc.instance:
                innerFunc.instance=cls(*args,**keywordargs)
            return innerFunc.instance
        innerFunc.instance=None
        return innerFunc

@singleton
class Employee:
    def __init__(self,p1,p2,p3):
        self.empId=p1
        self.empName=p2
        self.salary=p3

    def setDetails(self,p1,p2,p3):
        self.empId=p1
        self.empName=p2
        self.salary=p3

tom=Employee(101,"tom",798)
print("Toms empId",tom.empId)

george=Employee(102,"george",6666)
print("Tom's details",tom)
print("George's empId",george)
george.salary=0
print(tom.salary)
