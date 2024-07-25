# Write a program that calculates the day of the week for any particular date in the past or future.

# Example 1:

# Input:
# d = 28, m = 12, y = 1995
# Output:
# Thursday
# Explanation:
# 28 December 1995 was a Thursday.

# Example 2:

# Input:
# d = 30, m = 8, y = 2010
# Output:
# Monday
# Explanation:
# 30 August 2010 was a Monday.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function getDayOfWeek() which takes 3 Integers d, m and y denoting day, month and year as input and return a String denoting the answer.

# Expected Time Complexity: O(1)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= d <= 31
# 1 <= m <= 12
# 1 <= y <= 2100
def day_of_the_week(d, m, y):
    # 1.1.1 was a monday->1
    num_of_days=365*(y-1)
    leap_days=int(y/4)-int(y/100)+int(y/400)
    days_in_months=0
    match m:
        case 2:
            days_in_months=31
        case 3:
            days_in_months=59
        case 4:
            days_in_months=90
        case 5:
            days_in_months=120
        case 6:
            days_in_months=151
        case 7:
            days_in_months=181
        case 8:
            days_in_months=212
        case 9:
            days_in_months=243
        case 10:
            days_in_months=273
        case 11:
            days_in_months=304
        case 12:
            days_in_months=334
    num_of_days=num_of_days+leap_days+days_in_months+d
    result=num_of_days%7+1
    match result:
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case 1:
            return "Sunday"
    
 
    
    
    

if __name__=="__main__":
    print(day_of_the_week(30,8,2010))
    print(day_of_the_week(28,12,1998))
