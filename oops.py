l1=[]
class list_operation():
    def _init_(self):
        self.l1=[]
        
    def add_element(self,num,name):
        self.l1.append(num)
        self.l1.append(name)
               
    def print_list(self) :
        return self.l1        
    
obj = list_operation()
print (obj.print_list())
obj.add_element(1,"sivaranjani")
obj.add_element(2,"saranya")
obj.add_element(3,"manjula")
print (obj.print_list())


# particular index position  
user=int(input("enter the number"))
for i in l1:
    if i==l1(user):
        print(i)


# delete last element
l1.pop()
print(l1)


# size of list
a=len(l1)
print(a)

