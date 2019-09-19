class Account:
    rate=2.5;
    def input(self,p,n):
        self.p=p;
        self.n=n;
    def operation(self):
        interest=(self.p*Account.rate*self.n)/100;
        return interest;
    def modify(cls):
        Account.rate=3;
        

a1=Account();
a1.input(2000,2);
print("interst of a1 before modifying=",a1.operation());
a2=Account();
a2.input(3000,2);
a2.modify();
print("after modifying class variable interst of a2:");
print("interst=",a2.operation());
print("after modifying class variable interst of a1:");
print(a1.operation());
