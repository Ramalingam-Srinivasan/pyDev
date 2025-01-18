#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

#Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.


#In the Gregorian calendar, three conditions are used to identify leap years:

#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    leap = False

    # Write your logic here
    if not year % 4 and year % 100 or year % 400 == 0:
        leap = True
    return leap

if __name__ == "__main__":
    print(is_leap(2024))