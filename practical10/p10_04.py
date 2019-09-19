import datetime;
from datetime import date
class Person:
    def __init__(self,name='',bdate='15/10/2000',gender=''):
        self.name=name;
        format_str = '%d/%m/%Y' # The format
        self.datetime_obj = datetime.datetime.strptime(bdate, format_str)
     
        self.year=self.datetime_obj.strftime('%Y');
       
        self.bdate=bdate;
        self.gender=gender;
    def age(self):
         year1 = datetime.date.today().year;
         
         y=int(self.year);
       
         self.ag=year1  - y;
         return self.ag;
    def show(self):
        print("name=",self.name);
        print("bdate=",self.bdate);
        print("gender=",self.gender);
        print("age=",self.ag);
  
        
         

class Student(Person):
    def __init__(self,name='',bdate='15/10/2000',gender='',sem='',py='',java='',php=''):
        super().__init__(name,bdate,gender);
        self.sem=sem;
        self.py=py;
        self.java=java;
        self.php=php;

    def calc_total(self):
        self.total=self.py+self.java+self.php;
        return self.total;
    def calc_per(self):
        self.per=self.total/3;
        return self.per;
    def calc_grade(self):
        if(self.per>=70):
            return "distiction";
        elif(self.per>60 and self.per<70):
            return "first class";
        elif(self.per>50 and self.per<60):
            return "second class";
        elif(self.per>40 and self.per<50):
            return "third class";
        else:
            return "fail";
            
  

    def show(self):
        super().show();
        print("sem=",self.sem);
        print("python=",self.py);
        print("java=",self.java);
        print("php=",self.php);
        print("total=",self.total);
        print("percentage=",self.per);
        print("grade=",s1.calc_grade());
        
class Employee(Person):
    def __init__(self,name='',bdate='15/10/2000',gender='',sal=''):
        super().__init__(name,bdate,gender);
        super().age();
        self.sal=sal;
    def calc_DA(self):
        if(self.gender=='male'):
            self.da=self.sal*0.80;
            return self.da;
        else:
            self.da=self.sal*0.70;
            return self.da;
    def calc_HRA(self):
        if(self.gender=='male'):
            self.hra=self.sal*0.10;
            return self.hra;
        else:
            self.hra=self.sal*0.15;
            return self.hra;
    def calc_total(self):
        self.t=self.sal+self.da+self.hra;
        return self.t;
    
   
    def bonus(self):
        if(self.ag>60):
            self.bonus=self.sal*0.52;
            return self.bonus;
        else:
            self.bonus=self.sal*0.50;
            return self.bonus;
    def show(self):
        super().show();
        print("basic salary=",self.sal);
        print("da of employee=",self.da);
        print("hra of employee=",self.hra);
        print("total salary=",self.t);
        print("bonus=",self.bonus);
       
p1=Person("mansi","15/10/1997","female");
#p1.show();
p1.age();
s1=Student("mansi","15/10/1960","female",3,90,95,80);
#s1.calc_total();
#s1.calc_per();
#s1.show();
e1=Employee("mansi","15/2/1950","female",20000);
#p=Person();
#p.show();
e1.calc_DA();
e1.calc_HRA();
e1.calc_total();
e1.bonus();
e1.show();
