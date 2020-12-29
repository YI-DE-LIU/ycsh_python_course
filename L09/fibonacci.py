f=[0,1]
x=int(input())
for i in range(2,x+1):
    fn=f[i-1]+f[i-2]
    f.append(fn)
print(f[x])