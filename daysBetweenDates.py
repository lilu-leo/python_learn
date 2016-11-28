#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysOfMonth(year1, month1):
        if (month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12):
                            return 31
        else:
            if (month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11):
                return 30
            else:
                if (year1 % 4 == 0 and year1 % 100 != 0):
                     return 29
                else:
                     return 28
                                                                                                                            
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    print '------'
    sum = 0
    if year2 - year1 > 0:
        y = year1
        while year2 - y > 1:
            sum += 365
            print "year days : " + str(sum) + ", " + str(y)
            if (y % 4 == 0 and y % 100 != 0):
                sum += 1
            y += 1
        sum += daysOfMonth(year1, month1) - day1
        sum += day2
        while month1 < 12:
            month1 += 1
            sum += daysOfMonth(year1, month1)
        m = 1
        while m < month2:
            sum += daysOfMonth(year2, m)
            m += 1
    else:
        m = month2 - month1
        sum += daysOfMonth(year1, month1) - day1
        sum += day2
        if m > 1:
            while (month1 + 1 < month2):
                month1 += 1
                sum += daysOfMonth(year1, month1)
 
    print sum
    return sum

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                    ((2012,1,1,2012,3,1), 60),
                    ((2011,6,30,2012,6,30), 366),
                    ((2011,1,1,2012,8,8), 585 ),
                    ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
