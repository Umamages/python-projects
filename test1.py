no1=int(input("enter no:"))
no2=int(input("enter no:"))
small = no1 if no1<no2 else no2
day=1
last= 0
while day<=small:
  if no1%day == 0 and no2%day == 0:
    last = day
  day+=1
if last!=0:
  print(last)
else:
  print("no common divisor") 
