
name=["manik","anjal","rohan","simran"]
count=0
for i in name:
    for char in i:
        if(char=="a" or char=="e" or char=="i" or char=="o" or char=="u" or char=="A" or char=="E" or char=="I" or char=="O" or char=="U"):
            count=count+1
print(f"number of vowel in {name} is {count}")


