## write a program to count the no of digit present in number

num=int(input("enter the number"))
count=0
while(num>0):
    num=num/10
    count=count+1
print(count)
