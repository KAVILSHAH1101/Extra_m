class Person:
    count=0;
    def __init__(self):
        print("default constructor callled...");
        Person.count=Person.count+1;
    def input(self,name,age):
       
        self.name=name;
        self.age=age;
       
    def display(self):
        print("name=",self.name);
        print("age=",self.age);
      

    @classmethod
    def clmethod(cls):
        return ' number of objects=',format(Person.count);
    @staticmethod
    def stmethod():
        print("number of objects in class=",Person.count);

p1=Person();
p1.input("mansi",21);
print(p1.display());
p2=Person();
p2.input("priya",25);
print(p2.display());
print(Person.clmethod());
Person.stmethod();


