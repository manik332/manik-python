l1={"name":"manik","roll_no":22,"class":"MCA"}
l2={"name":"manan","uid_no":22}

for a,b in zip(l1.items(),l2.items()):
    print(a,b)


dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)