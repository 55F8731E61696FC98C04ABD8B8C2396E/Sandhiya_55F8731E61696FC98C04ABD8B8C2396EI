# how to check Leap Year
year = int(input("Enter the Year:"))

if (year % 400 == 0) and (year % 100 == 0):
  print(year, "is Leap year")

elif (year % 4 == 0) and (year % 100 != 0):
  print(year, "is Leap year")

else:
  print(year, "not a Leap Year ")
