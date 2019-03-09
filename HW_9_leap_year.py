def is_it_a_leap_year(year):
    '''This function checks whether the provided year number is for a common or leap year and prints the result from check
    args:
    year = [Enter the year number you'd like to check'''
    if year%4 !=0:
        print(f"Year {year} is a common year")
    elif year%100 !=0:
        print(f"Year {year} is a common year")
    elif year%400 !=0:
        print(f"Year {year} is a common year")
    else:
        print(f"Year {year} is a leap year")

is_it_a_leap_year(2000)