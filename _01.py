str=[]
n=int(input("ENTER THE NUMBER OF ELEMENTS IN A LIST : "))
for i in range(0,n):
    a=(input("ENTER THE ELEMENTS : "))
    str.append(a)
    
str.sort(key=lambda str:str[-2])
print(str)


