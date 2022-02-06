# # Enter your code here. Read input from STDIN. Print output to STDOUT
# class Subject:
#     def _init_(self, Code, Name, Credit, Teacher, subAvg):
#         self.Code=Code
#         self.Name=Name
#         self.Credit=Credit
#         self.Teacher=Teacher
#         self.subAvg=subAvg
        
# class Grade:
#     def _init_(self, grade, subjectCollection):
#         self.grade= grade 
#         self.subjectCollection=subjectCollection   
        
#     def findMaximumSubjectByCredit(self):
#         if(self.subjectCollection==0):
#             return None
#         else:
#             maxi=max(self.subjectColection,key=lambda x:x.Cred)
#             return maxi
        
#     def sortSubjectByAvg(self):
#         if(self.subjectCollection==0) :
#             return None 
#         else:
#             l=[]
#             for i in self.subjectCollection:
#                 l.append(i.subAvg)
#                 l.sort()
#             return l

#     if "__name__" == 'main_':
#         num=int(input())
#         subject=[]
#         for i in range(num):
#             Code=input()
#             Name=input()
#             Credit=int(input())
#             Teacher=input()
#             subAvg=float(input())
#             subject.append(Subject(Code,Name,Credit,Teacher,subAvg)

#             object1 = Grade("XYZ",subject)
#             r1=obj.findMaximumByCredit()
#             r2=obj.sortSubjectBysubAvg()
#             if(r1==0):
#                 print("No data found")
#             else:
#                    print(r1.Code)
#                 print(r1.Name)
#                 print(r1.Credit)
#                 print(r1.Teacher)
#                 print(r1.subAvg)

#             if(r2==0):
#                 print("No data found")
#             else:
#                 for i in r2:
#                     print(i)



class subject:
    def __init__(self,code,name,credit,teacher,subavg):
        self.code=code
        self.name=name
        self.credit=credit
        self.teacher =teacher
        self.subavg=subavg

class Grade :
    def __init__ (self,grade,subjectcollection):
        self.grade=grade
        self.subjectcollection =subjectcollection

    def findmax(self):
        if len(self.subjectcollection)==0:
            return None
        m=max(self.subjectcollection, key=lambda x:x.credit)
        return m
    def sort(self):
        l=[]
        for i in subjectcollection:
            l.append(i.subavg)
        l.sort()
        if len(l)==0:
            return None
        else:
            return l

n=int(input())
subjectcollection=[]
for i in range(n):
    code=input('c')
    name=input('n')
    credit=int(input('cr'))
    teacher=input('t')
    subavg=float(input('sbavg'))
    subjectcollection.append(subject(code,name,credit,teacher,subavg))
obj=Grade("xyz",subjectcollection)
x=obj.findmax()
y=obj.sort()
if x:
    print(x.code,x.name,x.credit,x.teacher,x.subavg,sep="\n")
else:
    print("No Data Found")

if y:
    for i in y:
        print(i)
else:
    print("No Data Found")
        