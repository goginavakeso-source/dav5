#3
import calendar
myinput = input("შეიყვანე წელი: ")
year = int(myinput)
if calendar.isleap(year):
    print("ნაკიანია")
else:
    print("არაა ნაკიანი")