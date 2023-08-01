month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):

    #return True for leap year and False for non-leap year
    return year % 4 ==0 and (year %100 !=0 or year % 400 == 0)

def days_in_month(year,month):
    #return no of days in that month of the year
    if not 1 <= month <= 12:
        return 'Invalid Month'
    elif month ==2 and is_leap(year):
        return 29
    else:
        return month_days[month]
    
print(is_leap(2023))
print(days_in_month(2024,2))