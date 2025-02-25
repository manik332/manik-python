class default:
     def __init__(self,name,age):
          self.name=name
          self.age=age
     def show(self):
          print(f"{self.name} is of {self.age}")

user1=default("manik",23)
user2=default("manan",24)
user3=default("anjali",25)
user4=default("riya",26)
user5=default("rohan",27)


user1.show()
user2.show()
user3.show()
user4.show()
user5.show()

