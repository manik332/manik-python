with open('main.txt','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        print(line)
   
        