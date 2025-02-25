##write a program to reverse a number

num=int(input("enter the number"))
ans=0
while(num!=0):
    rem=num%10
    ans=ans*rem+rem
    num=num/10

print(f"answer is {ans}")






