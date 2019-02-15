a= input("Enter number")
a= a.split()
b=[]
for x in a:
   b.append(int(x)) 

print(b)
l=len(b)
c=0
s=0
for i in range(l):
    s=len(b[:i])
    for j in range(s):
        
        if b[s]<b[j]:
            c=b[s]
            b.pop(s)
            b.insert(b.index(b[j]),c)
    print(b,b[:i],b[s])

