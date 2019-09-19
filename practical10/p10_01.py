class String:
    def __init__(self):
        print("\n default constructor caled...");
    def __init__(self,str1=""):
        self.str1=str1;
    def set(self,str1):
        self.str1=str1;
    def display(self):
        return self.str1;
    def length(self):
        return len(self.str1);
    def join(self,str2):
        return self.str1 + str2;
    def compare(self,str2):
        if(self.str1==str2):
            return "same";
        else:
            return "different";
    def reverse(self):
        return self.str1[::-1];
    def palindrome(self):
        a=self.str1[::-1];
        if(a==self.str1):
            return "palindrome";
        else:
            return "not palindrome";
    def find_word(self,str2):
        c=str2 in self.str1;
        if(c==1):
            return "matched";
        else:
            return "not matched";
            

s1=String();
s2=String("ddu");
s1.set("hello world hii");
print(s1.display());
print(s2.display());
print(s1.length());
print(s1.join("nuknai"));
print(s1.compare("mansi"));
print(s1.reverse());
print(s1.palindrome());
print(s1.find_word("am"));

        
    
