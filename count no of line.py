with open('main.txt','r') as f:
    count=0
    while True:
       line= f.readline()
       count=count+1
       if not line:
           break
       print(count)