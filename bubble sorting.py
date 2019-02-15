a= input("Enter number")
a= a.split()
b=[]
for i in a:
   b.append(int(i)) 

print(b)
l = len(b)
swap=0
for j in range(l-1):
    swap=0
    for k in range(l-1):
        if(b[k]>b[k+1]):
            b[k],b[k+1]=b[k+1],b[k]
            swap+=1
    if swap==0:
            break
    print(b," cycle",j+1, "no. of swap=",swap)

