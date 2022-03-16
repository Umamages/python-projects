# Printing Nos in Reverse order
# ex. 1234 --> 4321

no=int(input("enter some number:"))
while no>0:
    rem=no%10
    print(rem, end=' ')
    no=no//10
