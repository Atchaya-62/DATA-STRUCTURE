class student :
    def __init__(self,name,dob,blood,dept,number):
        self.name=name
        self.dob=dob
        self.blood=blood
        self.dept=dept
        self.number=number
        self.cgpa=None
        
    def  setcgpa(self,cgpa):
        self.cgpa=cgpa
        
    def changedob(self,changed):
        self.dob=changed

    def changebg(self,changed):
        self.blood=changed

    def display(self):
        print("\n")
        print("Name : ",self.name)
        print("DOB : ",self.dob)
        print("Blood group :",self.blood)
        print("Department :",self.dept)
        print("Phone Number:",self.number)
        print("cGPA:",self.cgpa)
        

n=int(input("enter no of students"))
for i in range(n):
    a=input("enter name:")
    b=input("enter DOB:")
    c=input("enter blood group: ")
    e=input("enter dept :")
    f=input("enter number :")

    obj=student(a,b,c,e,f)
    d=float(input("enter cgpa"))
    obj.setcgpa(d)

    change=input("changed Dob")
    obj.changedob(change)
    bloo=input("changed blood group")
    obj.changebg(bloo)

    obj.display()
          
              
