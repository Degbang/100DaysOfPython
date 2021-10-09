# leap year calculation

year = int(input("enter the year "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 100 == 0:
      print("leap")
    else:
        print("not leap")
  else:
   print("leap")
else:
 print("not a leap year")