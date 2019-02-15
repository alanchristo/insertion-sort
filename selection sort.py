a= input("Enter number")
a= a.split()
b=[]
for i in a:
   b.append(int(i)) 

print(b)
l = len(b)
s=0
for j in range(l-1):
    m= min(b[s:])
    b[b.index(m)],b[s] = b[s],b[b.index(m)]
    s+=1
    print(b)
