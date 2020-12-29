f=[0,1]
x=int(input())
y=int(input())
for i in range(2,y+1):
    fn=f[i-1]+f[i-2]
    f.append(fn)
print(f[x:y+1])


   

