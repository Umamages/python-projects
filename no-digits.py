# Printing No of Digits

no=1234
count=0
while no>0:
    no=no//10
    count=count+1
print(count)

# Addition of Digits
no=1234
total=0
while no>0:
    rem=no%10
    total=total+rem
    no=no//10
print(total)
    