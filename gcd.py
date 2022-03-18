# Greatest common divisors(GCD or HCF) of two numbers
 
no1=int(input("enter no:"))
no2=int(input("enter no:"))
small = no1 if no1<no2 else no2
day=1
gcd = 0
while day<=small:
    if no1%day == 0 and no2%day == 0:
        gcd = day
    day+=1
if gcd!=0:
    print(gcd)
else:
    print("no common divisor")