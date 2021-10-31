# This function checks if year is a leap year.
def isLeapYear(year):
    if year%100 == 0:
        return True if year%400 == 0 else False
    elif year%4 == 0:
        return True
    else:
        return False

# This function returns the number of days in a month
def monthDays(year, month):
    MONTHDAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if month == 2 and isLeapYear(year):
        return 29
    return MONTHDAYS[month-1]

# Returns the next day
def nextDay(year, month, day):
    if day == monthDays(year,month):
        if month == 12:
            return year+1, 1, 1
        else:
            return year, month+1, 1
    return year, month, day+1


# This is the main function
def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31 ?
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1 ?
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)    # 2016 3 1 ?
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1 ?

# call the main function
main()