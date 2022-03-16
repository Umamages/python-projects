import ssl


f=1
s=1
i=1
while i<8:
    print(f)
    t=f+s
    f=s
    s=t
    i=i+1



n = int(input( "enter no"))
ls = [0,1]
for x in range(n):
    if len(ls) < n:
        ls.append(ls[-1] + ls[-2])
print(ls)
     



