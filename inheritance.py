class student:
    
    def name1(self,name):
        print("hello ",name)

class teacher(student):
    def name(self,name,age):
        print("hello teacher name is ",name," and age is ",age)
    
t=teacher()
t.name1("gaurav")
t.name("sumyak",19)

#rest of the inheritance are just same as other languages
